"""Champions League fixtures and results from openligadb.

football-data has no European competitions at all and openfootball publishes
a season only once it is over, so without this the pooled model's links stop
a season short and a bet placed this week cannot be settled. openligadb
carries the current season live and needs no API key — but it has no odds, so
prices still come from manual_fixtures.csv.
"""
import json

import pandas as pd
import pytest
import requests

from src import openligadb

PAYLOAD = [
    {"team1": {"teamName": "FC Brügge"}, "team2": {"teamName": "Aston Villa"},
     "matchDateTimeUTC": "2026-09-08T19:00:00Z", "matchIsFinished": True,
     "matchResults": [{"resultName": "Halbzeit", "pointsTeam1": 1, "pointsTeam2": 3,
                       "resultOrderID": 1},
                      {"resultName": "Endergebnis", "pointsTeam1": 2, "pointsTeam2": 3,
                       "resultOrderID": 2}]},
    {"team1": {"teamName": "Inter Mailand"}, "team2": {"teamName": "FC Brügge"},
     "matchDateTimeUTC": "2026-10-13T19:00:00Z", "matchIsFinished": False,
     "matchResults": []},
    {"team1": {"teamName": "AS Rom"}, "team2": {"teamName": "Real Madrid"},
     "matchDateTimeUTC": "2026-10-14T19:00:00Z", "matchIsFinished": False,
     "matchResults": []},
    {"team1": {"teamName": "Kaputt"}, "matchDateTimeUTC": "2026-10-13T19:00:00Z"},
]


def test_parse_takes_the_full_time_score_not_half_time():
    df = openligadb.parse(PAYLOAD)
    assert len(df) == 3, "缺字段的行要丢掉"
    played = df[df["finished"]].iloc[0]
    assert (played["hg"], played["ag"]) == (2, 3), "要取 Endergebnis 不是 Halbzeit"
    assert played["home"] == "FC Brügge" and played["time"] == "19:00"
    assert df["date"].is_monotonic_increasing
    assert not df["neutral"].any()


def test_an_unplayed_match_has_no_score():
    df = openligadb.parse(PAYLOAD)
    future = df[~df["finished"]]
    assert len(future) == 2
    assert future["hg"].isna().all()


def test_score_falls_back_to_the_highest_order_result():
    one = [{"team1": {"teamName": "A"}, "team2": {"teamName": "B"},
            "matchDateTimeUTC": "2026-09-08T19:00:00Z", "matchIsFinished": True,
            "matchResults": [{"resultName": "?", "pointsTeam1": 1, "pointsTeam2": 0,
                              "resultOrderID": 1}]}]
    assert openligadb.parse(one).iloc[0]["hg"] == 1


def test_results_returns_only_played_matches():
    r = openligadb.results(openligadb.parse(PAYLOAD))
    assert len(r) == 1
    assert r["hg"].dtype.kind == "i"
    assert list(r.columns) == ["div", "date", "home", "away", "hg", "ag", "neutral"]
    assert openligadb.results(pd.DataFrame()).empty


def test_fixtures_respects_the_window():
    df = openligadb.parse(PAYLOAD)
    assert len(openligadb.fixtures(df, "2026-10-13", 1)) == 1
    assert len(openligadb.fixtures(df, "2026-10-13", 2)) == 2
    assert openligadb.fixtures(df, "2026-10-20", 2).empty
    # a played match is never a fixture
    assert "FC Brügge" not in set(openligadb.fixtures(df, "2026-09-08", 1)["home"])


def test_load_offline(tmp_path):
    def fetcher(url, cache_file, max_age):
        assert url.endswith("/getmatchdata/ucl/2026")
        return json.dumps(PAYLOAD).encode()

    df = openligadb.load(2026, tmp_path, fetcher=fetcher)
    assert len(df) == 3 and set(df["div"]) == {"CL"}


def test_load_survives_a_dead_endpoint(tmp_path):
    def boom(url, cache_file, max_age):
        raise requests.RequestException("down")

    assert openligadb.load(2026, tmp_path, fetcher=boom).empty


def test_load_survives_junk(tmp_path):
    assert openligadb.load(2026, tmp_path, fetcher=lambda *a: b"not json").empty
    assert openligadb.load(2026, tmp_path, fetcher=lambda *a: b'{"msg":"nope"}').empty


def test_season_for_uses_the_starting_year():
    assert openligadb.season_for("2026-10-13") == 2026
    assert openligadb.season_for("2027-03-01") == 2026


def test_shipped_aliases_cover_the_german_names():
    """openligadb is a third naming convention after football-data and
    openfootball — Inter Mailand, FC Brügge, AS Rom."""
    from src.aliases import load_table
    from src.config import ROOT
    table = load_table(ROOT)
    for german, expected in (("Inter Mailand", "Inter"), ("FC Brügge", "Club Brugge"),
                             ("AS Rom", "Roma"), ("Atletico Madrid", "Ath Madrid"),
                             ("Paris St. Germain", "Paris SG")):
        assert table.get(german) == expected, f"{german} 的别名不对"
    # teams from countries with no domestic data stay their own node
    for unmapped in ("Sabah", "Shakhtar Donetsk", "Slavia Prag", "Slovan Bratislava"):
        assert table.get(unmapped) == "", f"{unmapped} 应当映射为空"
