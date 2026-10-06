"""Closing odds entered by hand.

CLV is the project's main metric, and nothing supplies a closing line for
European or international matches: football-data.co.uk has no such fixtures
and both results feeds carry results only. Typing the line in at kick-off is
the only way those picks can ever be judged on anything but profit and loss.
"""
import pandas as pd
import pytest

from src import ledger
from src.config import load_config
from src.ledger import COLUMNS, closing_for_outcome, devigged_close, set_closing, summarize


@pytest.fixture()
def cfg(tmp_path):
    import copy
    c = copy.deepcopy(load_config())
    c["paths"]["ledger"] = str(tmp_path / "bets/ledger.csv")
    c["paths"]["paper_ledger"] = str(tmp_path / "bets/paper_ledger.csv")
    return c


def _row(pick_id="p1", outcome="H", market="1X2", odds=4.23, label="主胜 A", status="open"):
    return {"id": pick_id, "created": "2026-10-06", "date": pd.Timestamp("2026-10-06"),
            "div": "INT", "home": "A", "away": "B", "market": market, "outcome": outcome,
            "label": label, "odds": odds, "stake": 1.0, "p_final": 0.24, "status": status,
            "result": "", "pnl": None, "close_odds": None, "clv": None, "clv_novig": None,
            "close_source": ""}


def _write(cfg, tmp_path, paper, rows):
    path = ledger.ledger_path(cfg, tmp_path, paper)
    ledger.save(ledger._append(pd.DataFrame(columns=COLUMNS), rows), path)
    return path


def test_closing_for_outcome_prefers_the_single_value():
    assert closing_for_outcome("1X2", "H", {"close": 4.2, "close_h": 9.9}) == 4.2
    assert closing_for_outcome("1X2", "D", {"close_h": 4.2, "close_d": 3.3}) == 3.3
    assert closing_for_outcome("OU25", "U25", {"close_u25": 1.9}) == 1.9
    assert closing_for_outcome("1X2", "A", {"close_h": 4.2}) is None


def test_devigged_close_needs_a_complete_market():
    assert devigged_close({"close_h": 4.2, "close_d": 3.3}) is None
    p = devigged_close({"close_h": 4.2, "close_d": 3.25, "close_a": 1.92})
    assert set(p) == {"H", "D", "A"} and sum(p.values()) == pytest.approx(1.0)
    assert p["A"] > p["H"]
    assert devigged_close({"close_o25": 1.85, "close_u25": 1.95}) is not None
    assert devigged_close({"close_h": 1.0, "close_d": 3.3, "close_a": 2.0}) is None


def test_set_closing_updates_both_ledgers(cfg, tmp_path):
    """The real bet and the paper bet share a match but not a price."""
    real = _write(cfg, tmp_path, False, [_row(odds=4.50)])
    paper = _write(cfg, tmp_path, True, [_row(odds=4.23)])
    assert set_closing("p1", {"close_h": 4.20, "close_d": 3.25, "close_a": 1.92},
                       cfg, tmp_path) == 2

    r, p = ledger.load(real).iloc[0], ledger.load(paper).iloc[0]
    assert r["close_odds"] == 4.20 and p["close_odds"] == 4.20
    assert r["clv"] == pytest.approx(round(4.50 / 4.20 - 1, 4))
    assert p["clv"] == pytest.approx(round(4.23 / 4.20 - 1, 4))
    assert r["close_source"] == "pinnacle"


def test_set_closing_picks_the_bet_s_own_outcome(cfg, tmp_path):
    path = _write(cfg, tmp_path, True, [_row(pick_id="away", outcome="A", odds=5.00)])
    set_closing("away", {"close_h": 4.20, "close_d": 3.25, "close_a": 1.92}, cfg, tmp_path)
    assert ledger.load(path).iloc[0]["close_odds"] == 1.92


def test_source_decides_whether_it_counts_as_sharp(cfg, tmp_path):
    path = _write(cfg, tmp_path, True, [_row()])
    set_closing("p1", {"close": 4.20}, cfg, tmp_path, source="average")
    d = summarize(ledger.load(path))
    assert d["avg_clv"] is not None
    assert d["sharp_clv"] is None and d["sharp_n"] == 0

    set_closing("p1", {"close": 4.20}, cfg, tmp_path, source="pinnacle")
    assert summarize(ledger.load(path))["sharp_n"] == 1


def test_clv_counts_before_the_match_is_settled(cfg, tmp_path):
    """CLV is fixed at kick-off; waiting for the result wastes its advantage."""
    path = _write(cfg, tmp_path, True, [_row(status="open")])
    set_closing("p1", {"close": 4.00}, cfg, tmp_path)
    d = summarize(ledger.load(path))
    assert d["settled"] == 0 and d["open"] == 1
    assert d["sharp_n"] == 1 and d["sharp_clv"] == pytest.approx(round(4.23 / 4.00 - 1, 4))
    assert "对 Pinnacle 收盘" in ledger.format_summary("模拟投注", d)


def test_overwriting_an_earlier_entry(cfg, tmp_path):
    path = _write(cfg, tmp_path, True, [_row()])
    set_closing("p1", {"close": 5.20}, cfg, tmp_path)
    set_closing("p1", {"close": 4.70}, cfg, tmp_path)
    assert ledger.load(path).iloc[0]["close_odds"] == 4.70


def test_unknown_id_and_missing_price_are_refused(cfg, tmp_path):
    _write(cfg, tmp_path, True, [_row()])
    with pytest.raises(SystemExit, match="找不到"):
        set_closing("nope", {"close": 4.2}, cfg, tmp_path)
    with pytest.raises(SystemExit, match="没给出"):
        set_closing("p1", {"close_d": 3.25}, cfg, tmp_path)      # wrong outcome given
    with pytest.raises(SystemExit, match="不合理"):
        set_closing("p1", {"close": 0.9}, cfg, tmp_path)


def test_settling_a_league_bet_still_overrides_a_hand_entry(cfg, tmp_path):
    """Where an automatic closing line exists it is authoritative."""
    row = _row(status="open")
    row["div"] = "E0"
    path = _write(cfg, tmp_path, True, [row])
    set_closing("p1", {"close": 9.99}, cfg, tmp_path, source="average")

    played = pd.DataFrame([{"div": "E0", "date": pd.Timestamp("2026-10-06"), "home": "A",
                            "away": "B", "hg": 2, "ag": 1,
                            "PSCH": 4.00, "PSCD": 3.50, "PSCA": 1.95}])
    ledger.settle(cfg, root=tmp_path, today=pd.Timestamp("2026-10-07").date(),
                  history_loader=lambda *a, **k: played,
                  intl_loader=lambda *a, **k: pd.DataFrame(),
                  uefa_loader=lambda *a, **k: pd.DataFrame())
    out = ledger.load(path).iloc[0]
    assert out["close_odds"] == 4.00 and out["close_source"] == "pinnacle"


# --- de-vigged CLV ------------------------------------------------------------

def test_novig_clv_is_recorded_when_the_market_is_complete(cfg, tmp_path):
    """Comparable across closing lines; the raw CLV is not."""
    path = _write(cfg, tmp_path, True, [_row(odds=4.23)])
    set_closing("p1", {"close_h": 3.94, "close_d": 3.25, "close_a": 1.99},
                cfg, tmp_path, source="average")
    row = ledger.load(path).iloc[0]
    assert row["clv"] == pytest.approx(round(4.23 / 3.94 - 1, 4))
    # the soft line carries ~6.5% margin, so de-vigging costs most of that
    assert row["clv_novig"] == pytest.approx(0.009, abs=0.002)
    assert row["clv_novig"] < row["clv"] - 0.05


def test_novig_clv_is_absent_when_only_one_price_is_given(cfg, tmp_path):
    path = _write(cfg, tmp_path, True, [_row(odds=4.23)])
    set_closing("p1", {"close": 3.94}, cfg, tmp_path)
    row = ledger.load(path).iloc[0]
    assert pd.notna(row["clv"]) and pd.isna(row["clv_novig"])


def test_novig_makes_two_lines_agree(cfg, tmp_path):
    """Same implied probability, different margin: raw CLV differs, no-vig does not."""
    sharp = {"close_h": 4.04, "close_d": 3.33, "close_a": 2.04}      # ~2% margin
    soft = {"close_h": 3.94, "close_d": 3.25, "close_a": 1.99}       # ~6.5% margin
    out = []
    for i, market in enumerate((sharp, soft)):
        path = _write(cfg, tmp_path, True, [_row(pick_id=f"p{i}", odds=4.23)])
        set_closing(f"p{i}", market, cfg, tmp_path)
        out.append(ledger.load(path).iloc[0])
    assert abs(out[0]["clv"] - out[1]["clv"]) > 0.02
    assert abs(out[0]["clv_novig"] - out[1]["clv_novig"]) < 0.015


def test_settle_fills_the_novig_clv_too(cfg, tmp_path):
    row = _row(status="open")
    row["div"] = "E0"
    path = _write(cfg, tmp_path, True, [row])
    played = pd.DataFrame([{"div": "E0", "date": pd.Timestamp("2026-10-06"), "home": "A",
                            "away": "B", "hg": 2, "ag": 1,
                            "PSCH": 4.00, "PSCD": 3.50, "PSCA": 1.95}])
    ledger.settle(cfg, root=tmp_path, today=pd.Timestamp("2026-10-07").date(),
                  history_loader=lambda *a, **k: played,
                  intl_loader=lambda *a, **k: pd.DataFrame(),
                  uefa_loader=lambda *a, **k: pd.DataFrame())
    out = ledger.load(path).iloc[0]
    assert pd.notna(out["clv_novig"])
    assert out["clv_novig"] < out["clv"]
