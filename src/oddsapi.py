"""Fixtures and market odds for European and international competitions.

the-odds-api.com is the only source found that carries both the schedule and
prices for these competitions, and crucially it carries **Pinnacle** — which
the user cannot reach directly from Germany. That makes a sharp anchor and an
automatic CLV possible for matches that until now had neither.

The key lives in the ODDS_API_KEY environment variable (a GitHub Secret in
CI). It is never read from config.yaml and never written anywhere.

Two things shape the design:

* **Quota.** The free tier allows 500 requests a month and each request costs
  one credit per market. So a poll of one competition for 1X2 and over/under
  costs 2, and the caller is expected to poll only when that competition
  actually has a match in the window. Responses are cached like every other
  feed.
* **Which book for which market.** Pinnacle quotes 1X2 on every match but
  publishes only its own main total — over one Champions League round it
  offered the 2.5 line on 1 match out of 18, its main line being 3.0. So 1X2
  takes Pinnacle and over/under 2.5 falls back to whichever books quote that
  line (Betsson, Nordic Bet, William Hill did, for all 18). The over/under
  anchor for these competitions is therefore softer than the 1X2 one, and
  `market_source` records which was used.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import pandas as pd
import requests

BASE_URL = "https://api.the-odds-api.com/v4"
KEY_ENV = "ODDS_API_KEY"

# competition code -> the-odds-api sport key
SPORTS = {
    "CL": "soccer_uefa_champs_league",
    "EL": "soccer_uefa_europa_league",
    "UECL": "soccer_uefa_europa_conference_league",
    "INT": "soccer_uefa_nations_league",
}
SHARP_BOOK = "pinnacle"
TOTALS_LINE = 2.5


def api_key() -> str | None:
    key = os.environ.get(KEY_ENV, "").strip()
    return key or None


def _get(path: str, params: dict, cache: Path, max_age_hours: float,
         fetcher=None) -> list | None:
    """One cached GET. Returns None when the call could not be made."""
    from .data import fetch

    key = api_key()
    if not key:
        return None
    fetcher = fetcher or fetch
    query = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
    url = f"{BASE_URL}/{path}?{query}&apiKey={key}"
    try:
        raw = fetcher(url, cache, max_age_hours)
    except requests.RequestException as e:
        # never let the key reach a log line
        print(f"[warn] the-odds-api {path}: {type(e).__name__}")
        return None
    try:
        payload = json.loads(raw.decode("utf-8", "replace"))
    except json.JSONDecodeError:
        print(f"[warn] the-odds-api {path}: 返回的不是 JSON")
        return None
    return payload if isinstance(payload, list) else None


def fetch_events(div: str, cache_dir: str | Path, markets=("h2h", "totals"),
                 regions: str = "eu", max_age_hours: float = 3,
                 fetcher=None) -> list:
    """Raw events for one competition. Costs one credit per market."""
    sport = SPORTS.get(div)
    if sport is None:
        return []
    name = "-".join(markets)
    out = _get(f"sports/{sport}/odds",
               {"regions": regions, "markets": ",".join(markets),
                "oddsFormat": "decimal"},
               Path(cache_dir) / f"oddsapi_{div}_{name}.json", max_age_hours, fetcher)
    return out or []


def _h2h(event: dict, home: str, away: str) -> tuple[dict | None, str | None]:
    """1X2 prices, preferring Pinnacle."""
    wanted = {home: "H", "Draw": "D", away: "A"}
    best = None
    for book in event.get("bookmakers", []):
        for market in book.get("markets", []):
            if market.get("key") != "h2h":
                continue
            prices = {}
            for o in market.get("outcomes", []):
                slot = wanted.get(o.get("name"))
                if slot and isinstance(o.get("price"), (int, float)):
                    prices[slot] = float(o["price"])
            if len(prices) == 3:
                if book.get("key") == SHARP_BOOK:
                    return prices, "pinnacle"
                best = best or (prices, book.get("title") or "market")
    return best if best else (None, None)


def _totals(event: dict, line: float = TOTALS_LINE) -> tuple[dict | None, str | None]:
    """Over/under prices at one line, from whichever book quotes it.

    Pinnacle publishes only its main total, which for these competitions is
    usually 3.0, so this is normally a softer book than the 1X2 anchor.
    """
    best = None
    for book in event.get("bookmakers", []):
        for market in book.get("markets", []):
            if market.get("key") != "totals":
                continue
            prices = {}
            for o in market.get("outcomes", []):
                if o.get("point") != line:
                    continue
                slot = {"Over": "O25", "Under": "U25"}.get(o.get("name"))
                if slot and isinstance(o.get("price"), (int, float)):
                    prices[slot] = float(o["price"])
            if len(prices) == 2:
                if book.get("key") == SHARP_BOOK:
                    return prices, "pinnacle"
                best = best or (prices, book.get("title") or "market")
    return best if best else (None, None)


def _spread(event: dict, home: str, away: str, line: float = TOTALS_LINE) -> dict:
    """Average and best price across every book that quotes each outcome.

    The anchor says what the market thinks; this says what the user could
    plausibly get. Without it a fixture has a probability but no price to
    compare `min_odds` against, so it could never become a pick — the league
    path gets the same two columns from football-data.
    """
    wanted = {home: "H", "Draw": "D", away: "A"}
    collected: dict[str, list[float]] = {}
    for book in event.get("bookmakers", []):
        for market in book.get("markets", []):
            for o in market.get("outcomes", []):
                price = o.get("price")
                if not isinstance(price, (int, float)) or price <= 1:
                    continue
                if market.get("key") == "h2h":
                    slot = wanted.get(o.get("name"))
                elif market.get("key") == "totals" and o.get("point") == line:
                    slot = {"Over": "O25", "Under": "U25"}.get(o.get("name"))
                else:
                    slot = None
                if slot:
                    collected.setdefault(slot, []).append(float(price))
    cols = {}
    for slot, prices in collected.items():
        avg_col = {"H": "AvgH", "D": "AvgD", "A": "AvgA",
                   "O25": "Avg>2.5", "U25": "Avg<2.5"}[slot]
        max_col = {"H": "MaxH", "D": "MaxD", "A": "MaxA",
                   "O25": "Max>2.5", "U25": "Max<2.5"}[slot]
        cols[avg_col] = round(sum(prices) / len(prices), 3)
        cols[max_col] = max(prices)
    return cols


def to_fixture_rows(events: list, div: str, offset_hours: int = 0) -> pd.DataFrame:
    """Events as football-data-shaped rows, so market.py can read them as-is.

    The anchor prices go into Pinnacle's column names (PSH/PSD/PSA, P>2.5,
    P<2.5) because that is what `market_probs` reads first; `anchor_1x2` and
    `anchor_ou25` record which book each actually came from.
    """
    rows = []
    for e in events:
        home, away = e.get("home_team"), e.get("away_team")
        start = pd.to_datetime(e.get("commence_time"), errors="coerce", utc=True)
        if not home or not away or pd.isna(start):
            continue
        h2h, h_src = _h2h(e, home, away)
        tot, t_src = _totals(e)
        if h2h is None and tot is None:
            continue
        local = start + pd.Timedelta(hours=offset_hours)
        row = {"div": div, "date": pd.Timestamp(start.date()),
               "Time": local.strftime("%H:%M"), "home": home, "away": away,
               "neutral": False, "anchor_1x2": h_src, "anchor_ou25": t_src}
        if h2h:
            row.update({"PSH": h2h["H"], "PSD": h2h["D"], "PSA": h2h["A"]})
        if tot:
            row.update({"P>2.5": tot["O25"], "P<2.5": tot["U25"]})
        row.update(_spread(e, home, away))
        rows.append(row)
    return pd.DataFrame(rows)


def load(div: str, cache_dir: str | Path, today=None, horizon_days: int = 2,
         offset_hours: int = 0, fetcher=None) -> pd.DataFrame:
    """Priced fixtures for one competition inside the report's window."""
    df = to_fixture_rows(fetch_events(div, cache_dir, fetcher=fetcher), div, offset_hours)
    if df.empty or today is None:
        return df
    today = pd.Timestamp(today).normalize()
    end = today + pd.Timedelta(days=horizon_days)
    return df[(df["date"] >= today) & (df["date"] < end)].reset_index(drop=True)
