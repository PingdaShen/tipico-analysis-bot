"""Same-match combinations (1X2 + over/under 2.5).

The whole point is that these cannot be priced by multiplying the two
markets. A draw is usually low scoring, so "draw and over 2.5" is far rarer
than P(draw) x P(over) implies — on a typical fixture the naive product puts
its fair odds near 8 when the real figure is above 20.
"""
import numpy as np
import pandas as pd
import pytest

from src import daily
from src.config import load_config
from src.model import DixonColes
from src.value import (COMBOS, evaluate_combos, fit_joint, joint_table)
from tests.synthetic import loaders, make_league


@pytest.fixture(scope="module")
def model():
    hist_raw, fix_raw, today, _ = make_league(div="E0", n_teams=12, seasons=3, seed=1)
    history_loader, _ = loaders(hist_raw, fix_raw)
    return DixonColes(xi=0.001).fit(history_loader("E0", [], None, today=today), today)


def test_predict_returns_a_consistent_joint_table(model):
    p = model.predict("Team00", "Team01")
    assert set(COMBOS) <= set(p)
    assert sum(p[c] for c in COMBOS) == pytest.approx(1.0)
    # the joint table has to agree with both sets of marginals
    for r in ("H", "D", "A"):
        assert p[f"{r}&O25"] + p[f"{r}&U25"] == pytest.approx(p[r])
    for o in ("O25", "U25"):
        assert sum(p[f"{r}&{o}"] for r in "HDA") == pytest.approx(p[o])


def test_draw_and_over_is_rarer_than_the_product(model):
    """The dependence the whole feature exists for."""
    p = model.predict("Team00", "Team01")
    assert p["D&O25"] < p["D"] * p["O25"] * 0.75
    assert p["D&U25"] > p["D"] * p["U25"] * 1.1


def test_fit_joint_matches_the_target_marginals(model):
    p = model.predict("Team00", "Team01")
    joint = {c: p[c] for c in COMBOS}
    target_1x2 = {"H": 0.50, "D": 0.25, "A": 0.25}
    target_ou = {"O25": 0.60, "U25": 0.40}
    out = fit_joint(joint, target_1x2, target_ou)

    assert sum(out.values()) == pytest.approx(1.0)
    for r in ("H", "D", "A"):
        assert out[f"{r}&O25"] + out[f"{r}&U25"] == pytest.approx(target_1x2[r], abs=1e-6)
    for o in ("O25", "U25"):
        assert sum(out[f"{r}&{o}"] for r in "HDA") == pytest.approx(target_ou[o], abs=1e-6)
    # the model's dependence survives the rescaling
    assert out["D&O25"] < target_1x2["D"] * target_ou["O25"]


def test_fit_joint_is_identity_on_its_own_marginals(model):
    p = model.predict("Team00", "Team01")
    joint = {c: p[c] for c in COMBOS}
    out = fit_joint(joint, {k: p[k] for k in "HDA"},
                    {k: p[k] for k in ("O25", "U25")})
    for c in COMBOS:
        assert out[c] == pytest.approx(joint[c], abs=1e-9)


def test_fit_joint_survives_a_degenerate_table():
    joint = dict.fromkeys(COMBOS, 0.0)
    out = fit_joint(joint, {"H": 0.4, "D": 0.3, "A": 0.3}, {"O25": 0.5, "U25": 0.5})
    assert len(out) == len(COMBOS)
    assert not any(np.isnan(v) for v in out.values())


def _row(**extra):
    base = {"div": "E0", "date": pd.Timestamp("2026-10-06"), "home": "Team00",
            "away": "Team01", "PSH": 1.83, "PSD": 3.29, "PSA": 4.56,
            "P>2.5": 2.05, "P<2.5": 1.80}
    return pd.Series({**base, **extra})


def test_evaluate_combos_prices_all_six(model):
    cfg = load_config()
    rows = evaluate_combos(_row(), model, cfg)
    assert len(rows) == 6
    assert sum(r["p_final"] for r in rows) == pytest.approx(1.0)
    for r in rows:
        assert r["market"] == "1X2+OU25"
        assert r["min_odds"] >= cfg["value"]["min_odds"]
        assert r["min_odds"] == pytest.approx(
            max((1 + cfg["value"]["min_edge"]) / r["p_final"], cfg["value"]["min_odds"]))
        # no feed quotes these, so they can never be candidates on their own
        assert r["best_odds"] is None and r["is_candidate"] is False
    labels = {r["label"] for r in rows}
    assert "平局 + 大于 2.5 球" in labels
    assert any("Team00" in l and "大于" in l for l in labels)


def test_naive_product_is_reported_and_differs(model):
    rows = {r["outcome"]: r for r in evaluate_combos(_row(), model, load_config())}
    draw_over = rows["D&O25"]
    assert draw_over["naive_odds"] < draw_over["fair_odds"] * 0.8


def test_combos_need_both_markets(model):
    cfg = load_config()
    assert evaluate_combos(_row(**{"P>2.5": None, "P<2.5": None}), model, cfg) == []
    assert evaluate_combos(_row(PSH=None, PSD=None, PSA=None), model, cfg) == []


def test_combos_respect_the_config_switch(model, tmp_path):
    cfg = load_config()
    cfg["value"]["combos"] = False
    picks = pd.DataFrame([{"date": pd.Timestamp("2026-10-06"), "home": "Team00",
                           "away": "Team01"}])
    all_df = pd.DataFrame(evaluate_combos(_row(), model, load_config()))
    assert daily._combo_section(picks, all_df, cfg) == []


def test_combo_section_only_covers_picked_matches(model):
    cfg = load_config()
    all_df = pd.DataFrame(evaluate_combos(_row(), model, cfg))
    other = pd.DataFrame([{"date": pd.Timestamp("2026-10-06"), "home": "Team04",
                           "away": "Team05"}])
    assert daily._combo_section(other, all_df, cfg) == []

    picked = pd.DataFrame([{"date": pd.Timestamp("2026-10-06"), "home": "Team00",
                            "away": "Team01"}])
    lines = daily._combo_section(picked, all_df, cfg)
    assert lines and "同场组合参考" in lines[0]
    assert "不是推荐" in "\n".join(lines)
    body = [l for l in lines if l.startswith("| Team00")]
    assert 0 < len(body) <= cfg["value"]["max_combo_rows"]


def test_combo_section_is_empty_without_picks(model):
    cfg = load_config()
    all_df = pd.DataFrame(evaluate_combos(_row(), model, cfg))
    assert daily._combo_section(pd.DataFrame(), all_df, cfg) == []
    assert daily._combo_section(pd.DataFrame([{"date": 1, "home": "a", "away": "b"}]),
                                pd.DataFrame(), cfg) == []


def test_combos_never_enter_the_picks(model, tmp_path):
    """A combination has no verifiable price, so it must not be recommended."""
    hist_raw, fix_raw, today, _ = make_league(div="E0", n_teams=12, seasons=3, seed=1)
    hl, fl = loaders(hist_raw, fix_raw)
    cfg = load_config()
    cfg["leagues"] = {"E0": "x"}
    cfg["value"]["min_edge"] = -0.5          # force plenty of candidates
    for k in ("cache", "reports"):
        cfg["paths"][k] = str(tmp_path / k)
    cfg["paths"]["ledger"] = str(tmp_path / "bets/ledger.csv")
    cfg["paths"]["paper_ledger"] = str(tmp_path / "bets/paper_ledger.csv")
    cfg["paths"]["manual_fixtures"] = "manual_fixtures.csv"
    cfg["paths"]["manual_results"] = "manual_results.csv"

    all_df, picks, _ = daily.analyze(cfg, today, root=tmp_path, history_loader=hl,
                                     fixtures_loader=fl)
    assert (all_df["market"] == "1X2+OU25").any(), "组合应当被评估"
    assert not picks.empty
    assert (picks["market"] != "1X2+OU25").all(), "组合不能进入推荐"
