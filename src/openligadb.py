"""UEFA Champions League fixtures and results from api.openligadb.de.

openfootball publishes a European season only once it is over, so the pooled
model's cross-league links stop a season short and a bet placed this week
cannot be settled. openligadb is a community-maintained German database that
carries the current season live, needs no API key, and gives both the
schedule and the scores — which is exactly the half that football-data.co.uk
does not cover at all.

What it does not carry is odds. Those still come from manual_fixtures.csv.

Only the Champions League is usable: the `uel`, `uecl` and `unl` shortcuts all
return an empty list, and `ucl2026` is an unmaintained stub (32 rows, every
one dated 2026-09-08). The working endpoint is `/getmatchdata/ucl/<year>`.

Team names are German ("Inter Mailand", "FC Brügge", "AS Rom") — a third
naming convention after football-data and openfootball — so they go through
the same alias table before use.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pandas as pd
import requests

BASE_URL = "https://api.openligadb.de"
COLUMNS = ["div", "date", "time", "home", "away", "hg", "ag", "neutral", "finished"]
FULL_TIME = "Endergebnis"


def _score(match: dict) -> tuple[int, int] | None:
    """Full-time score, or None when the match has not been played."""
    results = match.get("matchResults") or []
    chosen = next((r for r in results if r.get("resultName") == FULL_TIME), None)
    if chosen is None:
        # some rows carry only one unnamed result; take the highest order
        chosen = max(results, key=lambda r: r.get("resultOrderID", 0), default=None)
    if chosen is None:
        return None
    try:
        return int(chosen["pointsTeam1"]), int(chosen["pointsTeam2"])
    except (KeyError, TypeError, ValueError):
        return None


def parse(payload: list[dict], div: str = "CL") -> pd.DataFrame:
    """Turn the API payload into the frame shape the rest of the code uses."""
    rows = []
    for m in payload:
        t1 = (m.get("team1") or {}).get("teamName")
        t2 = (m.get("team2") or {}).get("teamName")
        stamp = m.get("matchDateTimeUTC") or m.get("matchDateTime")
        if not (t1 and t2 and stamp):
            continue
        when = pd.to_datetime(stamp, errors="coerce", utc=True)
        if pd.isna(when):
            continue
        score = _score(m)
        rows.append({
            "div": div,
            "date": pd.Timestamp(when.date()),
            "time": when.strftime("%H:%M"),
            "home": str(t1).strip(), "away": str(t2).strip(),
            "hg": score[0] if score else None,
            "ag": score[1] if score else None,
            # the final is at a neutral venue, but openligadb does not say so;
            # the knockout rounds are not published yet either, so leave it off
            "neutral": False,
            "finished": bool(m.get("matchIsFinished")) and score is not None,
        })
    return pd.DataFrame(rows, columns=COLUMNS).sort_values("date").reset_index(drop=True)


def load(season: int, cache_dir: str | Path, shortcut: str = "ucl", div: str = "CL",
         max_age_hours: float = 6, fetcher=None) -> pd.DataFrame:
    """Every match of one Champions League season, played or not."""
    from .data import fetch

    fetcher = fetcher or fetch
    url = f"{BASE_URL}/getmatchdata/{shortcut}/{season}"
    try:
        raw = fetcher(url, Path(cache_dir) / f"openligadb_{shortcut}_{season}.json",
                      max_age_hours)
    except requests.RequestException as e:
        print(f"[warn] {url}: {e}")
        return pd.DataFrame(columns=COLUMNS)
    try:
        payload = json.loads(raw.decode("utf-8", "replace"))
    except json.JSONDecodeError as e:
        print(f"[warn] {url}: 返回的不是 JSON（{e}）")
        return pd.DataFrame(columns=COLUMNS)
    if not isinstance(payload, list):
        return pd.DataFrame(columns=COLUMNS)
    return parse(payload, div)


def results(df: pd.DataFrame) -> pd.DataFrame:
    """Played matches only, in the shape the models and settlement expect."""
    if df.empty:
        return pd.DataFrame(columns=["div", "date", "home", "away", "hg", "ag", "neutral"])
    out = df[df["finished"]].copy()
    if out.empty:
        return pd.DataFrame(columns=["div", "date", "home", "away", "hg", "ag", "neutral"])
    out["hg"] = out["hg"].astype(int)
    out["ag"] = out["ag"].astype(int)
    return out[["div", "date", "home", "away", "hg", "ag", "neutral"]].reset_index(drop=True)


def fixtures(df: pd.DataFrame, today, horizon_days: int) -> pd.DataFrame:
    """Upcoming matches inside the report's window, without any odds."""
    if df.empty:
        return df
    today = pd.Timestamp(today).normalize()
    end = today + pd.Timedelta(days=horizon_days)
    out = df[(~df["finished"]) & (df["date"] >= today) & (df["date"] < end)]
    return out.reset_index(drop=True)


def season_for(today=None) -> int:
    """openligadb labels a season by the year it starts."""
    from .data import current_season_start
    return current_season_start(pd.Timestamp(today).date() if today is not None else None)
