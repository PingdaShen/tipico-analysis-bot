"""Map UEFA (openfootball) team names onto football-data.co.uk names.

The two sources name the same clubs differently ("Club Atlético de Madrid"
vs "Ath Madrid"), and openfootball is not even consistent with itself across
seasons ("Inter" and "FC Internazionale Milano", "Real Madrid" and "Real
Madrid CF"). The European matches are only useful as cross-league links if
both sides resolve to the same team as the domestic data, so every UEFA name
has to be resolved before the pooled model is fitted.

`data/uefa_aliases.yaml` holds the curated mapping. It is a hand-maintained
data file rather than something inferred at runtime: a wrong guess silently
merges two clubs and corrupts their ratings, which is worse than dropping the
match. `suggest_aliases` only proposes candidates for a human to confirm, and
`python -m src.aliases check` lists the names a new season has introduced.

A UEFA name that resolves to nothing is kept as its own team rather than
dropped: clubs from countries with no odds data (Ukraine, Croatia, Serbia...)
still carry information as links between the leagues they play against, and
`min_team_matches` stops them being recommended.
"""
from __future__ import annotations

import argparse
import difflib
import re
import unicodedata
from pathlib import Path

import pandas as pd
import yaml

from .config import ROOT, load_config

ALIAS_FILE = "data/uefa_aliases.yaml"

# club-form noise that carries no identity: dropped before comparing.
# "sporting" and "real" stay — they distinguish real clubs.
_NOISE = {
    "fc", "cf", "ac", "as", "sc", "cd", "ud", "sv", "sk", "fk", "nk", "hnk",
    "gnk", "bk", "if", "il", "ff", "kv", "kaa", "krc", "rsc", "afc", "bsc",
    "vfb", "vfl", "tsg", "cs", "csm", "acf", "ogc", "hsc", "osc", "aa", "ca",
    "club", "clube", "de", "del", "the", "1", "1846", "1893", "1899", "1909",
    "04", "05", "1900", "1907", "1913", "1919", "1921",
}
_TRANSLIT = str.maketrans({
    "ß": "ss", "ø": "o", "æ": "ae", "å": "a", "đ": "d", "ð": "d", "þ": "th",
    "ł": "l", "ı": "i", "ʼ": "", "’": "", "'": "", "/": " ", "-": " ", ".": " ",
})


def normalize(name: str) -> str:
    """Accent-free, noise-free token string used only for comparison."""
    s = str(name).lower().translate(_TRANSLIT)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s)
    tokens = [t for t in s.split() if t not in _NOISE]
    return " ".join(tokens) or s.strip()


def div_countries(cfg: dict) -> dict[str, str]:
    """div code -> UEFA 3-letter country code, from config.yaml."""
    return dict(cfg.get("div_country") or {})


def build_index(universe: dict[str, list[str]], cfg: dict) -> dict[str, dict[str, str]]:
    """country code -> {normalized domestic name: original domestic name}."""
    dc = div_countries(cfg)
    index: dict[str, dict[str, str]] = {}
    for div, names in universe.items():
        cc = dc.get(div)
        if not cc:
            continue
        bucket = index.setdefault(cc, {})
        for n in names:
            bucket.setdefault(normalize(n), n)
    return index


def _token_score(a: str, b: str) -> float:
    """Similarity that rewards shared tokens and common prefixes."""
    ta, tb = a.split(), b.split()
    if not ta or not tb:
        return 0.0
    hits = 0.0
    for x in ta:
        best = 0.0
        for y in tb:
            if x == y:
                best = 1.0
            elif len(x) >= 3 and len(y) >= 3 and (x.startswith(y) or y.startswith(x)):
                best = max(best, 0.8)
            else:
                best = max(best, difflib.SequenceMatcher(None, x, y).ratio() * 0.7)
        hits += best
    coverage = hits / max(len(ta), len(tb))
    return 0.6 * coverage + 0.4 * difflib.SequenceMatcher(None, a, b).ratio()


def suggest(uefa_name: str, country: str, index: dict[str, dict[str, str]],
            cutoff: float = 0.6) -> tuple[str | None, float]:
    """Best domestic name for one UEFA name, restricted to its own country."""
    bucket = index.get(country)
    if not bucket:
        return None, 0.0
    key = normalize(uefa_name)
    if key in bucket:
        return bucket[key], 1.0
    best, score = None, 0.0
    for norm, original in bucket.items():
        s = _token_score(key, norm)
        if s > score:
            best, score = original, s
    return (best, score) if score >= cutoff else (None, score)


def load_table(root: Path = ROOT) -> dict[str, str]:
    """Curated UEFA name -> domestic name. Empty value means 'no domestic team'."""
    path = Path(root) / ALIAS_FILE
    if not path.exists():
        return {}
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(k): ("" if v is None else str(v)) for k, v in (raw.get("aliases") or {}).items()}


def resolve_names(df: pd.DataFrame, table: dict[str, str]) -> tuple[pd.DataFrame, list[str]]:
    """Rename UEFA teams to their domestic names; report the ones not in the table."""
    df = df.copy()
    unresolved = sorted((set(df["home"]) | set(df["away"])) - set(table))
    for col in ("home", "away"):
        df[col] = df[col].map(lambda n: table.get(n) or n)
    return df, unresolved


def uefa_name_countries(uefa: pd.DataFrame) -> dict[str, str]:
    """UEFA team name -> the country code openfootball tags it with."""
    pairs = pd.concat([
        uefa[["home", "home_country"]].rename(columns={"home": "team", "home_country": "cc"}),
        uefa[["away", "away_country"]].rename(columns={"away": "team", "away_country": "cc"}),
    ])
    return dict(pairs.drop_duplicates("team").set_index("team")["cc"])


def suggest_aliases(uefa: pd.DataFrame, universe: dict[str, list[str]], cfg: dict,
                    table: dict[str, str] | None = None) -> pd.DataFrame:
    """One row per UEFA name that the table does not cover yet."""
    table = table or {}
    index = build_index(universe, cfg)
    counts = pd.concat([uefa["home"], uefa["away"]]).value_counts()
    rows = []
    for name, cc in sorted(uefa_name_countries(uefa).items()):
        if name in table:
            continue
        match, score = suggest(name, cc, index)
        rows.append({"uefa_name": name, "country": cc, "matches": int(counts.get(name, 0)),
                     "suggestion": match or "", "score": round(score, 3),
                     "has_domestic_data": cc in index})
    return pd.DataFrame(rows).sort_values(["has_domestic_data", "score"],
                                          ascending=[False, False]).reset_index(drop=True)


def main() -> None:
    from .pool import domestic_universe
    from .openfootball import load_uefa_history

    ap = argparse.ArgumentParser(description="UEFA team-name alias table")
    ap.add_argument("cmd", choices=["check", "suggest"],
                    help="check: names a new season added; suggest: candidate matches")
    ap.add_argument("--seasons", type=int, default=None, help="UEFA seasons to scan")
    args = ap.parse_args()

    cfg = load_config()
    cache = Path(ROOT) / cfg["paths"]["cache"]
    n = args.seasons or cfg["uefa"]["history_seasons"]
    from .data import current_season_start
    years = list(range(current_season_start() - n + 1, current_season_start() + 1))
    uefa = load_uefa_history(years, cache)
    universe = domestic_universe(cfg, cache)
    table = load_table()
    out = suggest_aliases(uefa, universe, cfg, table)
    missing = out[out["has_domestic_data"]]
    if args.cmd == "check":
        if missing.empty:
            print(f"别名表完整：{len(uefa)} 场欧战比赛的队名都已覆盖。")
        else:
            print(f"有 {len(missing)} 个队名还没进 {ALIAS_FILE}（这些国家我们有国内数据，"
                  f"不补上就会被当成独立球队）：")
            print(missing.to_string(index=False))
    else:
        print(out.to_string(index=False))


if __name__ == "__main__":
    main()
