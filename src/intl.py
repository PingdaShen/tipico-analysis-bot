"""National-team model (Nations League, World Cup / Euro qualifying, finals).

Results come from martj42/international_results, which carries no odds at
all, so international picks depend entirely on the prices entered by hand in
manual_fixtures.csv.

Two things differ from a league model:

* Venue. A large share of international matches are played on neutral ground
  (tournaments, and some qualifiers moved for safety reasons). The source
  flags them, and the model drops the home term for those — see
  `DixonColes._home_vector`.
* Sample size. A national team plays roughly ten competitive matches a year,
  so the window spans years rather than seasons and the decay is slower.
  Friendlies are excluded by default (`international.tournaments`): lineups
  and intensity make them poor evidence about a competitive match.
"""
from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from .data import load_international
from .model import DixonColes


def window_start(cfg: dict, today=None) -> date:
    years = cfg["international"]["history_years"]
    today = pd.Timestamp(today).date() if today is not None else date.today()
    return today - timedelta(days=365 * years)


def load(cfg: dict, cache: str | Path, today=None, loader=load_international,
         fresh: bool = False) -> pd.DataFrame:
    """Competitive national-team results inside the configured window."""
    ic = cfg["international"]
    return loader(cache, since=window_start(cfg, today),
                  tournaments=ic.get("tournaments"), fresh=fresh)


def fit(matches: pd.DataFrame, cfg: dict, ref_date) -> DixonColes:
    ic, m = cfg["international"], cfg["model"]
    return DixonColes(xi=ic["xi"], ridge=ic.get("ridge", m["ridge"]),
                      max_goals=m["max_goals"],
                      min_team_matches=ic["min_team_matches"]).fit(matches, ref_date)
