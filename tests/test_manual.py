"""Hand-entered fixtures and odds."""
import pandas as pd
import pytest

from src.config import load_config
from src.manual import (COLUMNS, TEMPLATE, load, resolve_team, to_fixture_rows,
                        write_template)
from src.market import market_probs
from src.value import available_odds, evaluate_fixture

ROW_CL = ("CL,2026-10-21,21:00,Real Madrid,Juventus,0,"
          "1.75,3.90,4.60,1.80,4.00,4.75,1.85,1.95,1.90,2.00")
ROW_INT = "INT,2026-11-14,20:45,Germany,Netherlands,1,2.10,3.40,3.30,2.20,3.50,3.40,,,,"


def _file(tmp_path, *rows):
    p = tmp_path / "manual_fixtures.csv"
    p.write_text(TEMPLATE + "".join(r + "\n" for r in rows), encoding="utf-8")
    return p


def test_template_alone_parses_as_zero_rows(tmp_path):
    p = _file(tmp_path)
    df = load(p)
    assert df.empty
    assert list(df.columns) == COLUMNS       # an empty read must keep its shape


def test_missing_file_is_not_an_error(tmp_path):
    assert load(tmp_path / "nope.csv").empty


def test_write_template_does_not_clobber(tmp_path):
    p = tmp_path / "sub" / "manual_fixtures.csv"
    write_template(p)
    p.write_text(p.read_text(encoding="utf-8") + ROW_CL + "\n", encoding="utf-8")
    write_template(p)
    assert len(load(p)) == 1


def test_load_and_relabel(tmp_path):
    fx = to_fixture_rows(load(_file(tmp_path, ROW_CL, ROW_INT)))
    assert len(fx) == 2
    cl = fx.iloc[0]
    assert cl["div"] == "CL" and cl["Time"] == "21:00"
    assert cl["date"] == pd.Timestamp("2026-10-21")
    assert cl["neutral"] is False or cl["neutral"] == False     # noqa: E712
    # reference odds land on Pinnacle's names so they become the sharp anchor
    assert (cl["PSH"], cl["PSD"], cl["PSA"]) == (1.75, 3.90, 4.60)
    assert (cl["TipicoH"], cl["TipicoD"], cl["TipicoA"]) == (1.80, 4.00, 4.75)
    probs, source = market_probs(cl, "1X2")
    assert source == "pinnacle"
    assert sum(probs.values()) == pytest.approx(1.0)

    intl_row = fx.iloc[1]
    assert bool(intl_row["neutral"]) is True
    assert pd.isna(intl_row["P>2.5"])        # that market was left blank


def test_blank_market_is_skipped_not_guessed(tmp_path):
    fx = to_fixture_rows(load(_file(tmp_path, ROW_INT)))
    assert market_probs(fx.iloc[0], "OU25") == (None, None)


def test_comment_and_blank_comp_rows_are_ignored(tmp_path):
    p = _file(tmp_path, "# " + ROW_CL, ROW_INT, ",,,,,,,,,,,,,,,")
    assert len(load(p)) == 1


def test_tipico_price_beats_market_max():
    cfg = load_config()
    cfg["value"]["markets"] = ["1X2"]

    class Fake:
        def predict(self, h, a, neutral=False):
            return {"H": 0.55, "D": 0.25, "A": 0.20, "O25": 0.5, "U25": 0.5}

    base = {"div": "CL", "date": pd.Timestamp("2026-10-06"), "home": "A", "away": "B",
            "PSH": 2.0, "PSD": 3.8, "PSA": 4.6, "MaxH": 2.15, "MaxD": 3.9, "MaxA": 4.8}
    league = pd.Series(base)
    entered = pd.Series({**base, "TipicoH": 1.95, "TipicoD": 3.7, "TipicoA": 4.5})

    assert available_odds(league, "1X2")[1] == "market_max"
    assert available_odds(entered, "1X2")[1] == "tipico"

    h_league = {r["outcome"]: r for r in evaluate_fixture(league, Fake(), cfg)}["H"]
    h_entered = {r["outcome"]: r for r in evaluate_fixture(entered, Fake(), cfg)}["H"]
    assert h_league["min_odds"] == pytest.approx(h_entered["min_odds"])
    # the market best clears the bar, Tipico's real price does not
    assert h_league["best_odds"] == 2.15 and h_league["is_candidate"]
    assert h_entered["best_odds"] == 1.95 and not h_entered["is_candidate"]


def test_neutral_flag_reaches_the_model():
    cfg = load_config()
    cfg["value"]["markets"] = ["1X2"]
    seen = {}

    class Spy:
        def predict(self, h, a, neutral=False):
            seen["neutral"] = neutral
            return {"H": 0.4, "D": 0.3, "A": 0.3, "O25": 0.5, "U25": 0.5}

    row = pd.Series({"div": "INT", "date": pd.Timestamp("2026-10-06"), "home": "A",
                     "away": "B", "PSH": 2.5, "PSD": 3.3, "PSA": 3.0})
    evaluate_fixture(row, Spy(), cfg, neutral=True)
    assert seen["neutral"] is True


def test_resolve_team():
    known = {"Ath Madrid", "Real Madrid", "Bayern Munich"}
    aliases = {"Club Atlético de Madrid": "Ath Madrid"}
    assert resolve_team("Real Madrid", known, aliases) == ("Real Madrid", "")
    assert resolve_team("Club Atlético de Madrid", known, aliases) == ("Ath Madrid", "")
    # a different spelling still resolves through normalization
    assert resolve_team("bayern munich", known, aliases)[0] == "Bayern Munich"
    name, hint = resolve_team("Real Madrdi", known, aliases)
    assert name is None and hint.startswith("Real Madrid")   # closest first
    assert resolve_team("Nowhere United", known, aliases) == (None, "")


def test_resolve_team_does_not_use_an_alias_the_model_lacks():
    known = {"Real Madrid"}
    aliases = {"Club Atlético de Madrid": "Ath Madrid"}
    assert resolve_team("Club Atlético de Madrid", known, aliases)[0] is None


def test_short_name_resolves_when_unambiguous():
    """"Czech" is unambiguously Czech Republic — the dataset's own spelling."""
    known = {"Czech Republic", "Belarus", "Finland"}
    assert resolve_team("Czech", known, {}) == ("Czech Republic", "")
    assert resolve_team("czech", known, {}) == ("Czech Republic", "")


def test_ambiguous_short_name_is_not_guessed():
    """Guessing here would silently price the wrong team."""
    known = {"South Korea", "North Korea", "Belarus"}
    name, hint = resolve_team("Korea", known, {})
    assert name is None
    assert "South Korea" in hint and "North Korea" in hint


def test_exact_name_wins_over_a_longer_one():
    known = {"Guinea", "Guinea-Bissau", "Equatorial Guinea"}
    assert resolve_team("Guinea", known, {}) == ("Guinea", "")


def test_misspelling_hints_without_matching():
    known = {"Belarus", "Finland"}
    name, hint = resolve_team("Belarusia", known, {})
    assert name is None and hint == "Belarus"
    assert resolve_team("Nowhere", known, {}) == (None, "")


# --- which price counts as "available" ----------------------------------------

def test_price_source_defaults_to_the_market_average():
    """Max* sat 4.0% above the average over one weekend while min_edge is 3%,
    so ranking on it sourced the whole claimed edge from holding the best
    price in the market — which Tipico, a soft book, will rarely be."""
    row = pd.Series({"MaxH": 2.15, "MaxD": 3.9, "MaxA": 4.8,
                     "AvgH": 1.95, "AvgD": 3.6, "AvgA": 4.3,
                     "B365H": 2.00, "B365D": 3.7, "B365A": 4.4})
    assert available_odds(row, "1X2") == ({"H": 1.95, "D": 3.6, "A": 4.3}, "market_avg")
    assert available_odds(row, "1X2", "max")[1] == "market_max"
    assert available_odds(row, "1X2", "b365")[0]["H"] == 2.00
    assert available_odds(row, "1X2", "nonsense")[1] == "market_avg"


def test_hand_entered_tipico_price_always_wins():
    row = pd.Series({"MaxH": 2.15, "MaxD": 3.9, "MaxA": 4.8,
                     "AvgH": 1.95, "AvgD": 3.6, "AvgA": 4.3,
                     "TipicoH": 2.05, "TipicoD": 3.8, "TipicoA": 4.5})
    for src in ("max", "avg", "b365"):
        assert available_odds(row, "1X2", src) == (
            {"H": 2.05, "D": 3.8, "A": 4.5}, "tipico")


def test_price_source_falls_back_rather_than_dropping_a_fixture():
    row = pd.Series({"MaxH": 2.15, "MaxD": 3.9, "MaxA": 4.8})
    odds, src = available_odds(row, "1X2", "avg")
    assert src == "market_max" and odds["H"] == 2.15
    assert available_odds(pd.Series({"x": 1}), "1X2") == ({}, "none")


def test_config_ships_the_conservative_default():
    assert load_config()["value"]["price_source"] == "avg"


# --- partial Tipico entries and feed overlay ----------------------------------

def test_a_single_tipico_price_is_used_for_that_outcome():
    """Only one outcome is compared against min_odds, so demanding the whole
    market would silently fall back to the proxy for a row where the user
    entered just the side they care about."""
    row = pd.Series({"AvgH": 2.00, "AvgD": 3.60, "AvgA": 3.57, "TipicoA": 3.80})
    odds, src = available_odds(row, "1X2")
    assert odds["A"] == 3.80 and src == "tipico_partial"
    assert odds["H"] == 2.00                      # the rest stays on the proxy


def test_a_complete_tipico_market_is_labelled_plainly():
    row = pd.Series({"AvgH": 2.00, "AvgD": 3.60, "AvgA": 3.57,
                     "TipicoH": 2.05, "TipicoD": 3.70, "TipicoA": 3.80})
    assert available_odds(row, "1X2") == ({"H": 2.05, "D": 3.70, "A": 3.80}, "tipico")


def test_partial_over_under_entry():
    row = pd.Series({"Avg>2.5": 1.51, "Avg<2.5": 2.46, "Tipico>2.5": 1.45})
    odds, src = available_odds(row, "OU25")
    assert odds == {"O25": 1.45, "U25": 2.46} and src == "tipico_partial"


def test_a_tipico_price_below_the_minimum_removes_the_pick():
    """The real reason to enter it: West Ham vs QPR cleared on the market
    proxy at 1.51 but Tipico showed 1.45, under the 1.50 minimum."""
    cfg = load_config()
    cfg["value"]["markets"] = ["OU25"]

    class Fake:
        def predict(self, h, a, neutral=False):
            return {"H": 0.4, "D": 0.3, "A": 0.3, "O25": 0.72, "U25": 0.28}

    # chosen so min_odds lands at 1.47, between Tipico's 1.45 and the proxy 1.51
    base = {"div": "E1", "date": pd.Timestamp("2026-10-09"), "home": "West Ham",
            "away": "QPR", "P>2.5": 1.42, "P<2.5": 3.20,
            "Avg>2.5": 1.51, "Avg<2.5": 2.46}
    proxy = {r["outcome"]: r for r in evaluate_fixture(pd.Series(base), Fake(), cfg)}["O25"]
    real = {r["outcome"]: r
            for r in evaluate_fixture(pd.Series({**base, "Tipico>2.5": 1.45}), Fake(), cfg)}["O25"]
    assert 1.45 < proxy["min_odds"] < 1.51, "这组数字要卡在两个价格之间才测得到东西"
    assert proxy["is_candidate"] and proxy["best_odds"] == 1.51
    assert not real["is_candidate"] and real["best_odds"] == 1.45


def test_overlay_replaces_feed_odds_instead_of_duplicating_the_match():
    from src.manual import overlay
    day = pd.Timestamp("2026-10-09")
    feed = pd.DataFrame([
        {"div": "F2", "date": day, "home": "Nancy", "away": "Guingamp",
         "AvgA": 3.57, "TipicoA": None},
        {"div": "D2", "date": day, "home": "X", "away": "Y", "AvgA": 2.0, "TipicoA": None},
    ])
    entered = pd.DataFrame([
        {"div": "F2", "date": day, "home": "Nancy", "away": "Guingamp", "TipicoA": 3.80},
        {"div": "CL", "date": day, "home": "Real Madrid", "away": "Juventus", "TipicoA": 4.0},
    ])
    merged, leftover = overlay(feed, entered)
    assert len(merged) == 2, "不能把同一场比赛变成两行"
    assert merged.loc[merged["home"] == "Nancy", "TipicoA"].iloc[0] == 3.80
    assert merged.loc[merged["home"] == "Nancy", "AvgA"].iloc[0] == 3.57   # 未填的列保留
    assert list(leftover["home"]) == ["Real Madrid"]


def test_overlay_is_a_no_op_on_empty_inputs():
    from src.manual import overlay
    feed = pd.DataFrame([{"div": "E0", "date": pd.Timestamp("2026-10-09"),
                          "home": "A", "away": "B"}])
    assert overlay(feed, pd.DataFrame())[0].equals(feed)
    assert overlay(pd.DataFrame(), feed)[1].equals(feed)
