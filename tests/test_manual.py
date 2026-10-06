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
    assert name is None and hint == "Real Madrid"
    assert resolve_team("Nowhere United", known, aliases) == (None, "")


def test_resolve_team_does_not_use_an_alias_the_model_lacks():
    known = {"Real Madrid"}
    aliases = {"Club Atlético de Madrid": "Ath Madrid"}
    assert resolve_team("Club Atlético de Madrid", known, aliases)[0] is None
