import copy

import numpy as np
import pandas as pd
import pytest

from src import backtest, daily, ledger
from src.config import load_config
from src.data import recent_seasons, season_code
from src.market import devig, outcome_won
from src.model import DixonColes
from src.value import evaluate_fixture, stake_for
from tests.synthetic import loaders, make_league


@pytest.fixture(scope="module")
def league():
    return make_league(div="E0", n_teams=12, seasons=3, seed=1)


@pytest.fixture()
def cfg(tmp_path):
    c = copy.deepcopy(load_config())
    c["leagues"] = {"E0": "Premier League"}
    for k in ("cache", "reports"):
        c["paths"][k] = str(tmp_path / k)
    c["paths"]["ledger"] = str(tmp_path / "bets/ledger.csv")
    c["paths"]["paper_ledger"] = str(tmp_path / "bets/paper_ledger.csv")
    c["paths"]["manual_fixtures"] = str(tmp_path / "manual_fixtures.csv")
    return c


def test_season_codes():
    assert season_code(2026) == "2627"
    assert recent_seasons(3, pd.Timestamp("2026-10-06").date()) == ["2425", "2526", "2627"]
    assert recent_seasons(1, pd.Timestamp("2027-03-01").date()) == ["2627"]


def test_devig_and_outcomes():
    p = devig([2.0, 3.5, 4.0])
    assert abs(sum(p) - 1) < 1e-12
    assert outcome_won("H", 2, 1) and outcome_won("O25", 2, 1) and not outcome_won("U25", 2, 1)


def test_model_recovers_strengths(league):
    hist_raw, fix_raw, today, truth = league
    history_loader, _ = loaders(hist_raw, fix_raw)
    hist = history_loader("E0", [], None, today=today)
    m = DixonColes(xi=0.001).fit(hist, today)
    order = [m.teams[t] for t in truth["teams"]]
    assert np.corrcoef(m.attack[order], truth["att"])[0, 1] > 0.8
    assert abs(m.home_adv - truth["home"]) < 0.12
    p = m.predict("Team00", "Team01")
    assert abs(p["H"] + p["D"] + p["A"] - 1) < 1e-9
    assert abs(p["O25"] + p["U25"] - 1) < 1e-9
    assert m.predict("Team00", "Unknown FC") is None


def test_no_lookahead(league):
    hist_raw, fix_raw, today, _ = league
    history_loader, _ = loaders(hist_raw, fix_raw)
    hist = history_loader("E0", [], None)
    cut = hist["date"].iloc[len(hist) // 2]
    a = DixonColes().fit(hist, cut)
    b = DixonColes().fit(hist[hist["date"] < cut], cut)
    assert np.allclose(a.attack, b.attack)


def test_stake_rules(cfg):
    s = cfg["staking"]
    assert stake_for(0.5, 2.2, s) == 1.0
    k = dict(s, mode="kelly", bankroll=1000, max_stake_pct=0.05)
    assert stake_for(0.55, 2.0, k) == 25.0      # 0.25 * 0.1 * 1000, step 0.5
    assert stake_for(0.40, 2.0, k) == k["min_stake"]


def test_candidate_logic(cfg):
    class Fake:
        def predict(self, h, a, neutral=False):
            return {"H": 0.55, "D": 0.25, "A": 0.20, "O25": 0.5, "U25": 0.5}

    row = pd.Series({"div": "E0", "date": pd.Timestamp("2026-10-06"), "home": "A", "away": "B",
                     "PSH": 2.0, "PSD": 3.8, "PSA": 4.6, "MaxH": 2.15, "MaxD": 3.9, "MaxA": 4.8,
                     "AvgH": 1.95, "AvgD": 3.6, "AvgA": 4.3})
    cfg["value"]["markets"] = ["1X2"]
    res = {r["outcome"]: r for r in evaluate_fixture(row, Fake(), cfg)}
    h = res["H"]
    assert h["is_candidate"]
    assert h["min_odds"] >= cfg["value"]["min_odds"]
    assert h["best_odds"] >= h["min_odds"]
    assert not res["A"]["is_candidate"]            # model below market


def test_daily_end_to_end(league, cfg, tmp_path):
    hist_raw, fix_raw, today, _ = league
    hl, fl = loaders(hist_raw, fix_raw)
    picks = daily.run(cfg, today=today, root=tmp_path, history_loader=hl, fixtures_loader=fl)
    report = (tmp_path / cfg["paths"]["reports"] / "latest.md").read_text(encoding="utf-8")
    assert "今日投注建议" in report
    assert len(picks) <= cfg["value"]["max_picks"]
    for _, p in picks.iterrows():
        assert p["best_odds"] >= p["min_odds"] >= cfg["value"]["min_odds"]
        assert p["p_model"] > p["p_market"]
    assert picks.drop_duplicates(subset=["home", "away"]).shape[0] == len(picks)

    if not picks.empty:
        paper = ledger.load(tmp_path / cfg["paths"]["paper_ledger"])
        assert len(paper) == len(picks)
        # rerun does not duplicate paper bets
        daily.run(cfg, today=today, root=tmp_path, history_loader=hl, fixtures_loader=fl)
        assert len(ledger.load(tmp_path / cfg["paths"]["paper_ledger"])) == len(picks)


def test_ledger_add_and_settle(league, cfg, tmp_path):
    hist_raw, fix_raw, today, _ = league
    # play the fixtures: give them results so settle can find them
    played = fix_raw.copy()
    played["FTHG"], played["FTAG"] = 2, 1
    hl, fl = loaders(hist_raw, fix_raw)
    cfg["value"]["min_edge"] = -0.5                  # force picks for this test
    picks = daily.run(cfg, today=today, root=tmp_path, history_loader=hl, fixtures_loader=fl)
    assert not picks.empty
    p = picks.iloc[0]
    ledger.add(p["pick_id"], odds=round(p["min_odds"] + 0.1, 2), stake=1.0, cfg=cfg, root=tmp_path)

    hl_after, _ = loaders(pd.concat([hist_raw, played], ignore_index=True), fix_raw)
    ledger.settle(cfg, root=tmp_path, history_loader=hl_after, today=today.date())
    real = ledger.load(tmp_path / cfg["paths"]["ledger"])
    assert (real["status"] == "settled").all()
    expected_win = outcome_won(p["outcome"], 2, 1)
    assert (real["pnl"].iloc[0] > 0) == expected_win
    assert pd.notna(real["clv"].iloc[0])
    s = ledger.summarize(real)
    assert s["settled"] == 1


def test_backtest_runs(league, cfg, tmp_path):
    hist_raw, fix_raw, today, _ = league
    hl, _ = loaders(hist_raw, fix_raw)
    cfg["history_seasons"] = 1
    summary = backtest.run(cfg, n_test_seasons=1, history_loader=hl, root=tmp_path,
                           today=(today + pd.Timedelta(days=200)).date())
    assert summary.empty or "roi" in summary.columns
