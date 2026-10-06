"""Odds column maps (football-data.co.uk) and market helpers."""
from __future__ import annotations

import math

OUTCOMES = {"1X2": ["H", "D", "A"], "OU25": ["O25", "U25"]}

SHARP_PRE = {"1X2": ["PSH", "PSD", "PSA"], "OU25": ["P>2.5", "P<2.5"]}
SHARP_CLOSE = {"1X2": ["PSCH", "PSCD", "PSCA"], "OU25": ["PC>2.5", "PC<2.5"]}
AVG_PRE = {"1X2": ["AvgH", "AvgD", "AvgA"], "OU25": ["Avg>2.5", "Avg<2.5"]}
AVG_CLOSE = {"1X2": ["AvgCH", "AvgCD", "AvgCA"], "OU25": ["AvgC>2.5", "AvgC<2.5"]}
MAX_PRE = {"1X2": ["MaxH", "MaxD", "MaxA"], "OU25": ["Max>2.5", "Max<2.5"]}
SOFT_PRE = {"1X2": ["B365H", "B365D", "B365A"], "OU25": ["B365>2.5", "B365<2.5"]}


def get_odds(row, cols: list[str]) -> list[float] | None:
    vals = []
    for c in cols:
        try:
            v = float(row.get(c))
        except (TypeError, ValueError):
            return None
        if not math.isfinite(v) or v <= 1.0:
            return None
        vals.append(v)
    return vals


def odds_dict(row, table: dict, market: str) -> dict | None:
    odds = get_odds(row, table[market])
    return dict(zip(OUTCOMES[market], odds)) if odds else None


def devig(odds: list[float]) -> list[float]:
    inv = [1 / o for o in odds]
    s = sum(inv)
    return [i / s for i in inv]


def market_probs(row, market: str) -> tuple[dict | None, str | None]:
    """De-vigged market probabilities: Pinnacle first, market average as fallback."""
    for name, table in (("pinnacle", SHARP_PRE), ("average", AVG_PRE)):
        odds = get_odds(row, table[market])
        if odds:
            return dict(zip(OUTCOMES[market], devig(odds))), name
    return None, None


def closing_odds(row, market: str, outcome: str) -> float | None:
    for table in (SHARP_CLOSE, AVG_CLOSE):
        d = odds_dict(row, table, market)
        if d:
            return d[outcome]
    return None


def outcome_won(outcome: str, hg: int, ag: int) -> bool:
    return {
        "H": hg > ag,
        "D": hg == ag,
        "A": hg < ag,
        "O25": hg + ag > 2,
        "U25": hg + ag <= 2,
    }[outcome]
