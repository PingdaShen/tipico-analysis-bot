"""Load historical results/odds and upcoming fixtures from football-data.co.uk."""
from __future__ import annotations

import io
import time
from datetime import date
from pathlib import Path

import pandas as pd
import requests

BASE_URL = "https://www.football-data.co.uk"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; tipico-value-model)"}
BASE_COLUMNS = ["div", "date", "home", "away", "hg", "ag"]


def season_code(start_year: int) -> str:
    return f"{start_year % 100:02d}{(start_year + 1) % 100:02d}"


def current_season_start(today: date | None = None) -> int:
    today = today or date.today()
    return today.year if today.month >= 7 else today.year - 1


def recent_seasons(n: int, today: date | None = None) -> list[str]:
    """Season codes for the last n seasons, oldest first, including the current one."""
    start = current_season_start(today)
    return [season_code(y) for y in range(start - n + 1, start + 1)]


def parse_csv(content: bytes) -> pd.DataFrame:
    df = None
    for enc in ("utf-8-sig", "latin-1"):
        try:
            df = pd.read_csv(io.BytesIO(content), encoding=enc, on_bad_lines="skip")
            break
        except UnicodeDecodeError:
            continue
    if df is None:
        raise ValueError("could not decode CSV")
    df.columns = [str(c).strip().lstrip("\ufeff") for c in df.columns]
    return df.dropna(how="all")


def fetch(url: str, cache_file: Path, max_age_hours: float) -> bytes:
    if cache_file.exists():
        age_h = (time.time() - cache_file.stat().st_mtime) / 3600
        if age_h < max_age_hours:
            return cache_file.read_bytes()
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_bytes(resp.content)
    return resp.content


def standardize(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={"Div": "div", "HomeTeam": "home", "AwayTeam": "away",
                            "FTHG": "hg", "FTAG": "ag"}).copy()
    df["date"] = pd.to_datetime(df["Date"], dayfirst=True, format="mixed", errors="coerce")
    df = df.dropna(subset=["date", "home", "away"])
    df["home"] = df["home"].astype(str).str.strip()
    df["away"] = df["away"].astype(str).str.strip()
    return df


def load_history(div: str, seasons: list[str], cache_dir: str | Path,
                 today: date | None = None, fresh: bool = False) -> pd.DataFrame:
    """Played matches for one league across seasons, sorted by date."""
    cache_dir = Path(cache_dir)
    current = season_code(current_season_start(today))
    frames = []
    for s in seasons:
        url = f"{BASE_URL}/mmz4281/{s}/{div}.csv"
        max_age = (1 if fresh else 12) if s == current else 24 * 365
        try:
            content = fetch(url, cache_dir / f"{div}_{s}.csv", max_age)
        except requests.RequestException as e:
            print(f"[warn] {url}: {e}")
            continue
        frames.append(standardize(parse_csv(content)))
    if not frames:
        return pd.DataFrame(columns=BASE_COLUMNS)
    df = pd.concat(frames, ignore_index=True)
    df = df.dropna(subset=["hg", "ag"])
    df["hg"] = df["hg"].astype(int)
    df["ag"] = df["ag"].astype(int)
    return df.sort_values("date").reset_index(drop=True)


def load_fixtures(divs: list[str], cache_dir: str | Path) -> pd.DataFrame:
    """Upcoming fixtures with pre-match odds for the given leagues."""
    content = fetch(f"{BASE_URL}/fixtures.csv", Path(cache_dir) / "fixtures.csv", 3)
    df = standardize(parse_csv(content))
    return df[df["div"].isin(divs)].reset_index(drop=True)
