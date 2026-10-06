"""Cross-league pooled dataset for European club competitions.

A Dixon-Coles fitted on one league puts that league's teams on their own
scale. Two leagues never meet domestically, so their attack/defence values
are not comparable and "Real Madrid vs Arsenal" cannot be priced by putting
two separate models side by side — the difference between the scales is
unidentifiable.

The fix is to fit one model over every domestic match plus the European
matches. The European matches are the only edges between leagues, so they are
what makes a single scale identifiable. There are not many of them, which is
why `uefa.history_seasons` reaches further back than the league models and
`uefa.xi` decays more slowly: with the league models' decay the links would
carry almost no weight.

The pooled model is used only for European fixtures. Domestic picks keep
using the per-league models, which stay better calibrated for their own
league and are unaffected by this module.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .aliases import load_table, resolve_names
from .data import current_season_start, load_extra_history, load_history, season_code
from .model import DixonColes
from .openfootball import load_uefa_history

POOL_COLUMNS = ["div", "date", "home", "away", "hg", "ag", "neutral"]


def _as_date(today):
    """The loaders take a datetime.date; accept anything pandas understands."""
    return None if today is None else pd.Timestamp(today).date()


def pool_seasons(cfg: dict, today=None) -> list[int]:
    """Season start years covered by the pooled model."""
    n = cfg["uefa"]["history_seasons"]
    start = current_season_start(_as_date(today))
    return list(range(start - n + 1, start + 1))


def domestic_universe(cfg: dict, cache: str | Path, today=None,
                      history_loader=load_history,
                      extra_loader=load_extra_history) -> dict[str, list[str]]:
    """div code -> team names seen in that division's pooled window."""
    frames = load_domestic(cfg, cache, today, history_loader, extra_loader)
    return {div: sorted(set(g["home"]) | set(g["away"]))
            for div, g in frames.groupby("div")} if not frames.empty else {}


def load_domestic(cfg: dict, cache: str | Path, today=None,
                  history_loader=load_history,
                  extra_loader=load_extra_history) -> pd.DataFrame:
    """Every domestic match in the pooled window, main leagues and extra countries."""
    today = _as_date(today)
    years = pool_seasons(cfg, today)
    seasons = [season_code(y) for y in years]
    cutoff = pd.Timestamp(f"{years[0]}-07-01")
    frames = []
    for div in cfg["leagues"]:
        h = history_loader(div, seasons, cache, today=today)
        if not h.empty:
            frames.append(h[["div", "date", "home", "away", "hg", "ag"]])
    for country in cfg.get("extra_countries") or {}:
        h = extra_loader(country, cache, today=today)
        if not h.empty:
            h = h[h["date"] >= cutoff]
            frames.append(h[["div", "date", "home", "away", "hg", "ag"]])
    if not frames:
        return pd.DataFrame(columns=POOL_COLUMNS)
    df = pd.concat(frames, ignore_index=True)
    df["neutral"] = False
    return df[POOL_COLUMNS]


def load_pool(cfg: dict, cache: str | Path, today=None, root: Path | None = None,
              history_loader=load_history, extra_loader=load_extra_history,
              uefa_loader=load_uefa_history) -> tuple[pd.DataFrame, dict]:
    """Domestic + European matches on one team-name scale, plus a resolution report."""
    from .config import ROOT

    domestic = load_domestic(cfg, cache, today, history_loader, extra_loader)
    uefa = uefa_loader(pool_seasons(cfg, today), cache)
    info = {"domestic": len(domestic), "uefa": len(uefa), "unresolved": []}
    if uefa.empty:
        return domestic, info

    table = load_table(root or ROOT)
    uefa, unresolved = resolve_names(uefa, table)
    known = set(domestic["home"]) | set(domestic["away"])
    # a UEFA name we could not map is kept as its own team: it still links the
    # leagues it played against, and min_team_matches keeps it out of picks
    info["unresolved"] = [n for n in unresolved if n not in known]
    info["linked_teams"] = len((set(uefa["home"]) | set(uefa["away"])) & known)
    pool = pd.concat([domestic, uefa[POOL_COLUMNS]], ignore_index=True)
    return pool.sort_values("date").reset_index(drop=True), info


def fit_pool(pool: pd.DataFrame, cfg: dict, ref_date) -> DixonColes:
    """Fit the pooled model.

    It uses its own ridge rather than model.ridge: with ~900 teams and only a
    few hundred cross-league links the league models' near-zero ridge leaves
    the ratings badly over-dispersed, which showed up out of sample as an
    over-confident model barely better than the base rate.
    """
    u, m = cfg["uefa"], cfg["model"]
    return DixonColes(xi=u["xi"], ridge=u.get("ridge", m["ridge"]),
                      max_goals=m["max_goals"],
                      min_team_matches=u["min_team_matches"]).fit(pool, ref_date)
