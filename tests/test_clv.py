"""CLV must say which closing line it was measured against.

Pinnacle's close carries ~2% margin, the market average 4-6%. Beating the
average close by 3% says little; beating Pinnacle's close is the real test.
In the 22-league backtest the mixed figure read +0.7% while the Pinnacle-only
figure was -0.6%, so the distinction decides whether the model looks good.
"""
import numpy as np
import pandas as pd
import pytest

from src.backtest import summarize as bt_summarize
from src.ledger import COLUMNS, format_summary, summarize

SHARP = pd.Series({"PSCH": 2.00, "PSCD": 3.50, "PSCA": 4.00,
                   "AvgCH": 1.90, "AvgCD": 3.40, "AvgCA": 3.80})
AVG_ONLY = pd.Series({"AvgCH": 1.90, "AvgCD": 3.40, "AvgCA": 3.80})


def test_closing_odds_reports_its_source():
    from src.market import closing_odds
    assert closing_odds(SHARP, "1X2", "H") == (2.00, "pinnacle")
    assert closing_odds(AVG_ONLY, "1X2", "H") == (1.90, "average")
    assert closing_odds(pd.Series({"x": 1}), "1X2", "H") == (None, None)


def test_backtest_summary_separates_sharp_clv():
    bets = pd.DataFrame({
        "div": ["E0"] * 4,
        "pnl": [1.0, -1.0, 1.0, -1.0],
        "won": [True, False, True, False],
        "clv": [-0.01, -0.01, 0.05, 0.05],
        "close_source": ["pinnacle", "pinnacle", "average", "average"],
    })
    out = bt_summarize(bets)
    row = out.loc["ALL"]
    assert row["avg_clv"] == pytest.approx(0.02)       # the flattering mix
    assert row["sharp_clv"] == pytest.approx(-0.01)    # the honest number
    assert row["sharp_n"] == 2


def test_backtest_summary_without_the_column():
    """Old backtest_bets.csv files have no close_source; do not crash."""
    bets = pd.DataFrame({"div": ["E0"], "pnl": [1.0], "won": [True], "clv": [0.01]})
    out = bt_summarize(bets)
    assert np.isnan(out.loc["ALL", "sharp_clv"])
    assert out.loc["ALL", "sharp_n"] == 0


def _ledger(rows):
    df = pd.DataFrame(rows, columns=COLUMNS)
    df["date"] = pd.to_datetime(df["date"])
    return df


def test_ledger_summary_separates_sharp_clv():
    base = dict(id="x", created="2026-01-01", date="2026-01-02", div="E0", home="A",
                away="B", market="1X2", outcome="H", label="l", odds=2.0, stake=1.0,
                p_final=0.5, status="settled", result="1-0 赢", pnl=1.0)
    df = _ledger([
        {**base, "id": "a", "close_odds": 2.02, "clv": -0.01, "close_source": "pinnacle"},
        {**base, "id": "b", "close_odds": 1.90, "clv": 0.05, "close_source": "average"},
        # a European bet: settled for P&L but no closing odds exist at all
        {**base, "id": "c", "div": "CL", "close_odds": None, "clv": None, "close_source": ""},
    ])
    d = summarize(df)
    assert d["settled"] == 3
    assert d["avg_clv"] == pytest.approx(0.02)
    assert d["sharp_clv"] == pytest.approx(-0.01)
    assert d["sharp_n"] == 1
    assert d["no_clv"] == 1

    text = format_summary("模拟投注", d)
    assert "对锐价收盘的 CLV" in text and "-1.0%" in text
    assert "没有收盘赔率" in text


def test_ledger_summary_with_no_clv_at_all():
    base = dict(id="c", created="2026-01-01", date="2026-01-02", div="CL", home="A",
                away="B", market="1X2", outcome="H", label="l", odds=2.0, stake=1.0,
                p_final=0.5, status="settled", result="1-0 赢", pnl=1.0,
                close_odds=None, clv=None, close_source="")
    d = summarize(_ledger([base]))
    assert d["sharp_clv"] is None and d["avg_clv"] is None and d["no_clv"] == 1
    assert "—" in format_summary("模拟投注", d)


def test_ledger_load_tolerates_a_missing_column(tmp_path):
    """A ledger written before close_source existed must still load."""
    from src import ledger
    old = [c for c in COLUMNS if c != "close_source"]
    p = tmp_path / "ledger.csv"
    p.write_text(",".join(old) + "\n"
                 "a,2026-01-01,2026-01-02,E0,A,B,1X2,H,l,2.0,1.0,0.5,settled,1-0 赢,1.0,2.02,-0.01\n",
                 encoding="utf-8")
    df = ledger.load(p)
    assert "close_source" in df.columns
    assert summarize(df)["settled"] == 1
