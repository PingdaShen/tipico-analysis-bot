"""Fixtures and prices for European and international competitions.

the-odds-api is the only source found that carries both the schedule and the
odds for these, and it carries Pinnacle — which the user cannot reach from
Germany. The key lives in ODDS_API_KEY and must never reach config, a log or
a commit.
"""
import json

import pandas as pd
import pytest
import requests

from src import oddsapi

EVENT = {
    "id": "abc", "sport_key": "soccer_uefa_champs_league",
    "commence_time": "2026-10-13T19:00:00Z",
    "home_team": "Inter Milan", "away_team": "Club Brugge",
    "bookmakers": [
        {"key": "marathonbet", "title": "Marathon Bet", "markets": [
            {"key": "h2h", "outcomes": [
                {"name": "Inter Milan", "price": 1.30},
                {"name": "Club Brugge", "price": 10.0},
                {"name": "Draw", "price": 6.0}]},
            {"key": "totals", "outcomes": [
                {"name": "Over", "price": 1.30, "point": 2.5},
                {"name": "Under", "price": 3.40, "point": 2.5}]}]},
        {"key": "pinnacle", "title": "Pinnacle", "markets": [
            {"key": "h2h", "outcomes": [
                {"name": "Inter Milan", "price": 1.25},
                {"name": "Club Brugge", "price": 11.64},
                {"name": "Draw", "price": 6.32}]},
            # Pinnacle publishes only its own main line, 3.0 here
            {"key": "totals", "outcomes": [
                {"name": "Over", "price": 1.97, "point": 3.0},
                {"name": "Under", "price": 1.93, "point": 3.0}]}]},
        {"key": "betsson", "title": "Betsson", "markets": [
            {"key": "totals", "outcomes": [
                {"name": "Over", "price": 1.34, "point": 2.5},
                {"name": "Under", "price": 3.32, "point": 2.5}]}]},
    ],
}


def test_1x2_prefers_pinnacle():
    df = oddsapi.to_fixture_rows([EVENT], "CL")
    row = df.iloc[0]
    assert (row["PSH"], row["PSD"], row["PSA"]) == (1.25, 6.32, 11.64)
    assert row["anchor_1x2"] == "pinnacle"


def test_over_under_falls_back_when_pinnacle_lacks_the_line():
    """Over one Champions League round Pinnacle quoted 2.5 on 1 match of 18."""
    row = oddsapi.to_fixture_rows([EVENT], "CL").iloc[0]
    assert (row["P>2.5"], row["P<2.5"]) == (1.30, 3.40)
    assert row["anchor_ou25"] == "Marathon Bet"


def test_pinnacle_is_used_for_totals_when_it_does_quote_the_line():
    event = json.loads(json.dumps(EVENT))
    for b in event["bookmakers"]:
        if b["key"] == "pinnacle":
            b["markets"][1]["outcomes"] = [
                {"name": "Over", "price": 1.80, "point": 2.5},
                {"name": "Under", "price": 2.05, "point": 2.5}]
    row = oddsapi.to_fixture_rows([event], "CL").iloc[0]
    assert row["anchor_ou25"] == "pinnacle" and row["P<2.5"] == 2.05


def test_spread_gives_a_price_the_user_could_take():
    """Without these a fixture has a probability but nothing to compare
    min_odds against, so it could never become a pick."""
    row = oddsapi.to_fixture_rows([EVENT], "CL").iloc[0]
    assert row["MaxH"] == 1.30                      # best across books
    assert row["AvgH"] == pytest.approx((1.30 + 1.25) / 2)
    assert row["Max<2.5"] == 3.40
    assert row["Avg<2.5"] == pytest.approx((3.40 + 3.32) / 2)


def test_kickoff_is_shifted_and_the_date_is_utc():
    row = oddsapi.to_fixture_rows([EVENT], "CL", offset_hours=2).iloc[0]
    assert row["Time"] == "21:00"
    assert row["date"] == pd.Timestamp("2026-10-13")


def test_rows_without_usable_prices_are_dropped():
    bare = {"home_team": "A", "away_team": "B",
            "commence_time": "2026-10-13T19:00:00Z", "bookmakers": []}
    assert oddsapi.to_fixture_rows([bare], "CL").empty
    assert oddsapi.to_fixture_rows([{"home_team": "A"}], "CL").empty


def test_load_filters_to_the_window(tmp_path, monkeypatch):
    monkeypatch.setenv(oddsapi.KEY_ENV, "dummy")
    payload = json.dumps([EVENT]).encode()
    df = oddsapi.load("CL", tmp_path, today="2026-10-13", horizon_days=1,
                      fetcher=lambda *a: payload)
    assert len(df) == 1
    assert oddsapi.load("CL", tmp_path, today="2026-10-20", horizon_days=2,
                        fetcher=lambda *a: payload).empty


def test_nothing_happens_without_a_key(tmp_path, monkeypatch):
    monkeypatch.delenv(oddsapi.KEY_ENV, raising=False)
    assert oddsapi.api_key() is None
    assert oddsapi.fetch_events("CL", tmp_path) == []
    assert oddsapi.load("CL", tmp_path, today="2026-10-13").empty


def test_the_key_never_reaches_a_log_line(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv(oddsapi.KEY_ENV, "SUPERSECRET")

    def boom(url, cache, age):
        raise requests.RequestException(f"failed for {url}")

    assert oddsapi.fetch_events("CL", tmp_path, fetcher=boom) == []
    assert "SUPERSECRET" not in capsys.readouterr().out


def test_unknown_competition_is_ignored(tmp_path, monkeypatch):
    monkeypatch.setenv(oddsapi.KEY_ENV, "dummy")
    assert oddsapi.fetch_events("E0", tmp_path) == []


def test_junk_payload_is_survived(tmp_path, monkeypatch):
    monkeypatch.setenv(oddsapi.KEY_ENV, "dummy")
    assert oddsapi.fetch_events("CL", tmp_path, fetcher=lambda *a: b"nope") == []
    assert oddsapi.fetch_events("CL", tmp_path, fetcher=lambda *a: b'{"x":1}') == []


def test_every_manual_competition_has_a_sport_key():
    from src.config import load_config
    comps = load_config()["manual_competitions"]
    assert set(comps) == set(oddsapi.SPORTS), "manual_competitions 和 SPORTS 要对上"
