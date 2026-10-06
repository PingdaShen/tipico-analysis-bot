"""Turn model + market probabilities into bet candidates and stakes."""
from __future__ import annotations

import math
import re

import numpy as np

from .market import AVG_PRE, MAX_PRE, OUTCOMES, TIPICO_PRE, market_probs, odds_dict


def blend(p_model: dict, p_market: dict, w: float) -> dict:
    return {k: w * p_model[k] + (1 - w) * p_market[k] for k in p_market}


def outcome_label(outcome: str, home: str, away: str) -> str:
    return {
        "H": f"主胜 {home}",
        "D": "平局",
        "A": f"客胜 {away}",
        "O25": "大于 2.5 球",
        "U25": "小于 2.5 球",
    }[outcome]


def make_pick_id(date, div: str, home: str, away: str, outcome: str) -> str:
    raw = f"{date:%Y%m%d}-{div}-{home}-{away}-{outcome}"
    return re.sub(r"[^A-Za-z0-9\-]", "", raw.replace(" ", ""))


def stake_for(p: float, odds: float, staking: dict) -> float:
    bankroll = staking["bankroll"]
    if staking["mode"] == "kelly":
        edge = p * odds - 1
        s = max(edge, 0) / (odds - 1) * staking["kelly_fraction"] * bankroll
    else:
        s = staking["flat_stake"]
    s = min(s, staking["max_stake_pct"] * bankroll)
    step = staking["stake_step"]
    s = math.floor(s / step + 1e-9) * step
    return round(max(s, staking["min_stake"]), 2)


def available_odds(row, market: str) -> tuple[dict, str]:
    """The price the user can actually take, and where it came from.

    A hand-entered row carries Tipico's own price, which is exactly the number
    the rules are about. League fixtures only have the market best (Max*),
    which is a proxy: it says the price exists somewhere, not at Tipico.
    """
    tip = odds_dict(row, TIPICO_PRE, market)
    if tip:
        return tip, "tipico"
    return odds_dict(row, MAX_PRE, market) or {}, "market_max"


def evaluate_fixture(row, model, cfg: dict, neutral: bool = False) -> list[dict]:
    """Evaluate every outcome of one fixture; each row carries an is_candidate flag."""
    vcfg, w = cfg["value"], cfg["blend"]["model_weight"]
    p_model = model.predict(row["home"], row["away"], neutral=neutral)
    if p_model is None:
        return []

    out = []
    for market in vcfg["markets"]:
        p_market, source = market_probs(row, market)
        if p_market is None:
            continue
        p_final = blend(p_model, p_market, w)
        best, price_source = available_odds(row, market)
        avg = odds_dict(row, AVG_PRE, market) or {}
        for o in OUTCOMES[market]:
            p = p_final[o]
            min_needed = (1 + vcfg["min_edge"]) / p
            min_odds = max(min_needed, vcfg["min_odds"])
            best_o = best.get(o)
            edge_best = p * best_o - 1 if best_o else None
            is_candidate = (
                p_model[o] > p_market[o]
                and min_odds <= vcfg["max_odds"]
                and best_o is not None
                and best_o >= min_odds
            )
            out.append({
                "pick_id": make_pick_id(row["date"], row["div"], row["home"], row["away"], o),
                "div": row["div"],
                "date": row["date"],
                "time": row.get("Time", ""),
                "home": row["home"],
                "away": row["away"],
                "market": market,
                "outcome": o,
                "label": outcome_label(o, row["home"], row["away"]),
                "p_model": p_model[o],
                "p_market": p_market[o],
                "p_final": p,
                "market_source": source,
                "price_source": price_source,
                "fair_odds": 1 / p,
                "min_odds": min_odds,
                "best_odds": best_o,
                "avg_odds": avg.get(o),
                "edge_best": edge_best,
                "stake": stake_for(p, min_odds, cfg["staking"]),
                "is_candidate": is_candidate,
            })
    return out

# ---------------------------------------------------------------------------
# Same-match combinations (1X2 + over/under 2.5).
#
# These cannot be priced by multiplying the two markets. A draw is usually low
# scoring, so "draw and over 2.5" is roughly 65% rarer than P(draw) x P(over),
# and "draw and under 2.5" about 30% more common. The score matrix carries the
# dependence, so the model side is read straight off it (see DixonColes.predict).
#
# The market side is the problem: no feed quotes combinations. What a feed does
# give is the two sets of marginals, so the joint is rebuilt by stretching the
# model's table until its margins match the market's, which keeps the market as
# the anchor for *how likely each outcome is* while the model supplies only the
# dependence between them. That is the same division of labour as the rest of
# the pipeline.
# ---------------------------------------------------------------------------

RESULTS = ("H", "D", "A")
GOALS = ("O25", "U25")
COMBOS = [f"{r}&{o}" for r in RESULTS for o in GOALS]

COMBO_LABELS = {"O25": "大于 2.5 球", "U25": "小于 2.5 球"}


def combo_label(combo: str, home: str, away: str) -> str:
    r, o = combo.split("&")
    return f"{outcome_label(r, home, away)} + {COMBO_LABELS[o]}"


def joint_table(p: dict) -> np.ndarray:
    return np.array([[p[f"{r}&{o}"] for o in GOALS] for r in RESULTS], dtype=float)


def fit_joint(model_joint: dict, p_1x2: dict, p_ou: dict, iters: int = 200) -> dict:
    """Rescale the model's joint table to the given marginals (IPF).

    Returns the model's own table unchanged when it cannot be fitted, which is
    better than inventing a number.
    """
    m = joint_table(model_joint)
    rows = np.array([p_1x2[r] for r in RESULTS], dtype=float)
    cols = np.array([p_ou[o] for o in GOALS], dtype=float)
    if m.sum() <= 0 or rows.sum() <= 0 or cols.sum() <= 0:
        return dict(zip(COMBOS, m.ravel()))
    m = np.clip(m, 1e-12, None)
    rows, cols = rows / rows.sum(), cols / cols.sum()
    for _ in range(iters):
        m *= (rows / m.sum(1))[:, None]
        m *= (cols / m.sum(0))[None, :]
        if np.abs(m.sum(1) - rows).max() < 1e-12:
            break
    m /= m.sum()
    return dict(zip(COMBOS, m.ravel()))


def evaluate_combos(row, model, cfg: dict, neutral: bool = False) -> list[dict]:
    """Price every 1X2 + over/under combination for one fixture.

    No feed quotes a price for these, so they never carry `best_odds` and
    cannot become candidates on their own. What the report can say is the
    minimum odds worth taking, which is what the user checks in the app.
    """
    vcfg, w = cfg["value"], cfg["blend"]["model_weight"]
    p_model = model.predict(row["home"], row["away"], neutral=neutral)
    if p_model is None or f"{RESULTS[0]}&{GOALS[0]}" not in p_model:
        return []
    p_mkt_1x2, source = market_probs(row, "1X2")
    p_mkt_ou, _ = market_probs(row, "OU25")
    if p_mkt_1x2 is None or p_mkt_ou is None:
        return []

    model_joint = {c: p_model[c] for c in COMBOS}
    market_joint = fit_joint(model_joint, p_mkt_1x2, p_mkt_ou)
    final_joint = fit_joint(model_joint,
                            blend(p_model, p_mkt_1x2, w), blend(p_model, p_mkt_ou, w))

    out = []
    for c in COMBOS:
        p = final_joint[c]
        if p <= 0:
            continue
        min_odds = max((1 + vcfg["min_edge"]) / p, vcfg["min_odds"])
        out.append({
            "pick_id": make_pick_id(row["date"], row["div"], row["home"], row["away"],
                                    c.replace("&", "")),
            "div": row["div"], "date": row["date"], "time": row.get("Time", ""),
            "home": row["home"], "away": row["away"],
            "market": "1X2+OU25", "outcome": c,
            "label": combo_label(c, row["home"], row["away"]),
            "p_model": model_joint[c], "p_market": market_joint[c], "p_final": p,
            "market_source": source, "price_source": None,
            "fair_odds": 1 / p, "min_odds": min_odds,
            "best_odds": None, "avg_odds": None, "edge_best": None,
            "naive_odds": 1 / (blend(p_model, p_mkt_1x2, w)[c.split("&")[0]]
                               * blend(p_model, p_mkt_ou, w)[c.split("&")[1]]),
            "stake": stake_for(p, min_odds, cfg["staking"]),
            "is_candidate": False,
        })
    return out
