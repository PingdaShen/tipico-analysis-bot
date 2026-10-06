"""Turn model + market probabilities into bet candidates and stakes."""
from __future__ import annotations

import math
import re

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
