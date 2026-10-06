"""Parse UEFA club results from the openfootball/champions-league text files.

football-data.co.uk has no European club competitions at all, so these files
are the only free source of cross-league results. They matter because domestic
leagues never play each other: without the European matches the Dixon-Coles
ratings of two leagues are on unrelated scales and a Real Madrid vs Arsenal
price is meaningless. Those matches are the links that put every team on one
scale.

Available files per season directory (e.g. "2025-26"):
  cl.txt     Champions League league phase, playoffs, knockout
  clq.txt    Champions League qualifying
  elq.txt    Europa League qualifying
  confq.txt  Conference League qualifying
The repo carries no Europa/Conference League main stage, and the current
season only appears once it has been played.

Line shapes:
  = UEFA Champions League 2025/26
  # Date       Tue Sep 16 2025 - Sat May 30 2026 (256d)
  ▪ League, Matchday 1
    Tue Sep 16 2025
      18:45  FC Bayern München (GER) v GNK Dinamo Zagreb (CRO)  9-2 (3-0)
    Wed Sep 17
             Real Madrid CF (ESP)    v VfB Stuttgart (GER)      3-1 (0-0)

Scores are reported as the result that decided the match, so a tie settled in
extra time reads "3-3 a.e.t. (2-3, 1-1)" — after extra time 3-3, after 90
minutes 2-3, at half time 1-1. The model is fitted on 90-minute goals, so the
parser always returns the 90-minute score.
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import pandas as pd
import requests

REPO_URL = ("https://raw.githubusercontent.com/openfootball/champions-league"
            "/master/{season}/{file}.txt")
FILES = ("cl", "clq", "elq", "confq")

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}

_DATE_RE = re.compile(
    r"^\s+(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+([A-Z][a-z]{2})\s+(\d{1,2})(?:\s+(\d{4}))?\s*$")
_STAGE_RE = re.compile(r"^\s*▪\s*(.+?)\s*$")
_MATCH_RE = re.compile(r"^\s+(?:(\d{1,2}:\d{2})\s+)?(\S.*?)\s+v\s+(\S.*?)\s{2,}(\S.*?)\s*$")
_SCORE_RE = re.compile(r"(\d+)-(\d+)")
_TEAM_RE = re.compile(r"^(.*?)\s*\(([A-Z]{3})\)\s*$")
_FINAL_RE = re.compile(r"(?:^|,\s*)Final$")

COLUMNS = ["div", "date", "home", "away", "hg", "ag", "neutral",
           "home_country", "away_country", "stage"]


def season_dir(start_year: int) -> str:
    """2025 -> '2025-26', matching the directory names in the repo."""
    return f"{start_year}-{(start_year + 1) % 100:02d}"


def split_team(raw: str) -> tuple[str, str]:
    """'FC Bayern München (GER)' -> ('FC Bayern München', 'GER')."""
    m = _TEAM_RE.match(raw)
    return (m.group(1).strip(), m.group(2)) if m else (raw.strip(), "")


def ninety_minute_score(raw: str) -> tuple[int, int] | None:
    """The score after 90 minutes, ignoring extra time and penalties."""
    s = raw.split("pen.", 1)[1] if "pen." in raw else raw
    parens = re.findall(r"\(([^)]*)\)", s)
    if "a.e.t." in s:
        # after extra time: the bracket lists (90 minutes, half time)
        inner = _SCORE_RE.search(parens[0]) if parens else None
        if inner is None:
            return None                     # no 90' score reported, unusable
        return int(inner.group(1)), int(inner.group(2))
    head = s.split("(", 1)[0]
    m = _SCORE_RE.search(head)
    return (int(m.group(1)), int(m.group(2))) if m else None


def parse(text: str, div: str) -> pd.DataFrame:
    """Parse one openfootball competition file into match rows."""
    rows: list[dict] = []
    stage, year, cur = "", None, None
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith(("#", "=")):
            continue
        m = _STAGE_RE.match(line)
        if m:
            stage = m.group(1)
            continue
        m = _DATE_RE.match(line)
        if m:
            mon, day, yr = m.group(1), int(m.group(2)), m.group(3)
            year = int(yr) if yr else year
            if year is None or mon not in MONTHS:
                cur = None
                continue
            cur = date(year, MONTHS[mon], day)
            continue
        m = _MATCH_RE.match(line)
        if m is None or cur is None:
            continue
        score = ninety_minute_score(m.group(4))
        if score is None:
            continue                        # fixture not played yet, or odd line
        home, hc = split_team(m.group(2))
        away, ac = split_team(m.group(3))
        if not home or not away:
            continue
        rows.append({
            "div": div, "date": pd.Timestamp(cur), "home": home, "away": away,
            "hg": score[0], "ag": score[1],
            # a one-off final is played at a neutral venue; everything else is a
            # real home game (two-legged ties included)
            "neutral": bool(_FINAL_RE.search(stage)),
            "home_country": hc, "away_country": ac, "stage": stage,
        })
    return pd.DataFrame(rows, columns=COLUMNS)


def load_uefa_history(seasons: list[int], cache_dir: str | Path, files=FILES,
                      fresh: bool = False, fetcher=None) -> pd.DataFrame:
    """UEFA club results for the given season start years, oldest first."""
    from .data import fetch

    fetcher = fetcher or fetch
    cache_dir = Path(cache_dir)
    frames = []
    for year in sorted(seasons):
        sd = season_dir(year)
        for f in files:
            url = REPO_URL.format(season=sd, file=f)
            try:
                content = fetcher(url, cache_dir / f"uefa_{sd}_{f}.txt", 1 if fresh else 24)
            except requests.RequestException:
                continue                    # season or file not published yet
            frames.append(parse(content.decode("utf-8", "replace"), f.upper()))
    if not frames:
        return pd.DataFrame(columns=COLUMNS)
    df = pd.concat(frames, ignore_index=True)
    return df.sort_values("date").reset_index(drop=True)
