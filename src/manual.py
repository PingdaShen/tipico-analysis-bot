"""Hand-entered fixtures and odds for competitions with no odds feed.

football-data.co.uk covers domestic leagues only. European club competitions
and national-team matches have no free fixture-and-odds feed, and the value
framework cannot work without market prices: the market is the anchor, and
`min_odds` is meaningless without it. So for those competitions the prices
are typed into `manual_fixtures.csv` by hand.

One row per match:

    comp,date,time,home,away,neutral,ref_h,ref_d,ref_a,tip_h,tip_d,tip_a,
    ref_o25,ref_u25,tip_o25,tip_u25

    comp     CL / EL / UECL / INT (see manual_competitions in config.yaml)
    date     YYYY-MM-DD
    neutral  1 for a neutral venue (finals, most tournament matches)
    ref_*    reference market odds — Pinnacle if you have them, otherwise the
             market average. This is what the model is measured against, so it
             must NOT be Tipico's own price, or the edge is circular.
    tip_*    Tipico's own price for the same outcome. Leave blank if you have
             not looked it up; the market best is then unknown and the match
             is evaluated but cannot become a pick.

Leave any market you do not care about blank. A row needs a complete set of
reference odds for a market before that market is evaluated at all.

Internally the rows are relabelled to football-data.co.uk column names, so
`market.py` and `value.py` treat them exactly like a league fixture.
"""
from __future__ import annotations

import difflib
from pathlib import Path

import pandas as pd

from .aliases import normalize

COLUMNS = ["comp", "date", "time", "home", "away", "neutral",
           "ref_h", "ref_d", "ref_a", "tip_h", "tip_d", "tip_a",
           "ref_o25", "ref_u25", "tip_o25", "tip_u25"]

# hand-entered column -> football-data.co.uk column. The reference odds take
# Pinnacle's names so market_probs() treats them as the sharp anchor, and the
# Tipico prices get their own columns rather than pretending to be "market
# best": they are the price actually available to the user.
ODDS_MAP = {
    "ref_h": "PSH", "ref_d": "PSD", "ref_a": "PSA",
    "ref_o25": "P>2.5", "ref_u25": "P<2.5",
    "tip_h": "TipicoH", "tip_d": "TipicoD", "tip_a": "TipicoA",
    "tip_o25": "Tipico>2.5", "tip_u25": "Tipico<2.5",
}

TEMPLATE = (
    "# 手填赛程和赔率：欧战和国家队没有免费的赔率源，这些价格只能你自己填。\n"
    "# comp: CL=欧冠 EL=欧联 UECL=欧协联 INT=国家队（见 config.yaml 的 manual_competitions）\n"
    "# date: YYYY-MM-DD  neutral: 中立场填 1，主客场填 0\n"
    "# ref_*: 参考市场赔率（有 Pinnacle 用 Pinnacle，否则用市场平均）——不要填 Tipico 自己的价格，\n"
    "#        否则等于拿 Tipico 和自己比，算不出任何优势。\n"
    "# tip_*: Tipico 的赔率。不填也可以，但不填就无法判断这注能不能下。\n"
    "# 不关心的盘口留空即可。一个盘口的 ref 赔率必须填齐才会被评估。\n"
    "#\n"
    "# 球队名要用模型认识的写法（欧战用 football-data.co.uk 的写法，如 Ath Madrid；\n"
    "# 国家队用英文国名，如 Germany）。写错时报告会提示最接近的候选，不会整体失败。\n"
    "#\n"
    + ",".join(COLUMNS) + "\n"
    "# 下面两行是例子，把行首的 # 去掉就会生效：\n"
    "# CL,2026-10-21,21:00,Real Madrid,Juventus,0,1.75,3.90,4.60,1.80,4.00,4.75,1.85,1.95,1.90,2.00\n"
    "# INT,2026-11-14,20:45,Germany,Netherlands,0,2.10,3.40,3.30,2.20,3.50,3.40,,,,\n"
)


def write_template(path: str | Path) -> Path:
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(TEMPLATE, encoding="utf-8")
    return path


def load(path: str | Path) -> pd.DataFrame:
    """Read the hand-entered file; returns an empty frame if it has no rows."""
    path = Path(path)
    if not path.exists():
        return pd.DataFrame(columns=COLUMNS)
    df = pd.read_csv(path, comment="#", dtype=str, keep_default_na=False)
    df.columns = [str(c).strip() for c in df.columns]
    missing = [c for c in ("comp", "date", "home", "away") if c not in df.columns]
    if missing:
        raise ValueError(f"{path} 缺少必需的列：{missing}")
    for c in COLUMNS:
        if c not in df.columns:
            df[c] = ""
    # a plain list comprehension here would be an empty list for an empty file,
    # which pandas reads as "select no columns" rather than "select no rows"
    df = df[df["comp"].astype(str).str.strip() != ""]
    return df[COLUMNS].reset_index(drop=True)


def to_fixture_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Relabel hand-entered rows to football-data.co.uk column names."""
    if df.empty:
        return pd.DataFrame(columns=["div", "date", "Time", "home", "away", "neutral"])
    out = pd.DataFrame({
        "div": df["comp"].astype(str).str.strip().str.upper(),
        "date": pd.to_datetime(df["date"], errors="coerce"),
        "Time": df["time"].astype(str).str.strip(),
        "home": df["home"].astype(str).str.strip(),
        "away": df["away"].astype(str).str.strip(),
        "neutral": df["neutral"].astype(str).str.strip().isin(("1", "true", "True", "yes", "Y")),
    })
    for src, dst in ODDS_MAP.items():
        out[dst] = pd.to_numeric(df[src].replace("", pd.NA), errors="coerce")
    return out.dropna(subset=["date", "home", "away"]).reset_index(drop=True)


def resolve_team(name: str, known: set[str], aliases: dict[str, str]) -> tuple[str | None, str]:
    """Match a hand-typed team name to a name the model knows.

    Returns (resolved name, hint). The hint names the closest candidates when
    nothing matched, so the report can say what to write instead.

    A shortened name is accepted only when it points at exactly one team:
    "Czech" is unambiguously "Czech Republic", while "Korea" matches both
    Koreas and has to come back as a question rather than a guess.
    """
    name = str(name).strip()
    if name in known:
        return name, ""
    mapped = aliases.get(name)
    if mapped and mapped in known:
        return mapped, ""
    norm = {normalize(k): k for k in known}
    key = normalize(name)
    hit = norm.get(key)
    if hit:
        return hit, ""

    prefixed = sorted(orig for n, orig in norm.items() if n.startswith(key))
    if len(prefixed) == 1:
        return prefixed[0], ""
    if prefixed:
        return None, "、".join(prefixed[:4])

    close = difflib.get_close_matches(key, list(norm), n=3, cutoff=0.6)
    return None, "、".join(norm[c] for c in close) if close else ""


# ---------------------------------------------------------------------------
# Hand-entered results.
#
# Both results feeds lag. openfootball publishes a European season once it is
# over, and international_results trails the latest international window by
# weeks — on 2026-10-06 its newest competitive match was 2026-07-19, so the
# whole September window was missing for every national team. The model is not
# wrong when it has not seen those matches, it is just blind to them, and the
# effect is not symmetric: filling in only one team's results moves the price
# the wrong way. Belarus vs Finland went 0.276 -> 0.282 on Belarus's three
# matches alone, and 0.276 -> 0.259 once Finland's were added too.
#
# So results go in as a block, per window, and drop out again automatically
# once the upstream feed catches up.
# ---------------------------------------------------------------------------

RESULT_COLUMNS = ["comp", "date", "home", "away", "hg", "ag", "neutral", "tournament"]

RESULT_TEMPLATE = (
    "# 手录赛果：数据源落后时，把它还没收录的比赛补进来。\n"
    "# comp: INT=国家队  CL/EL/UECL=欧战（见 config.yaml 的 manual_competitions）\n"
    "# date: YYYY-MM-DD   hg/ag: 主队/客队进球   neutral: 中立场填 1\n"
    "# 比分用 90 分钟的，不要用加时或点球后的比分。\n"
    "#\n"
    "# tournament: 只对 INT 有意义。填了就必须是 config.yaml 的 international.tournaments\n"
    "#   里的名字，否则这场会被跳过并在报告里说明。留空表示强制计入。\n"
    "#   默认不收友谊赛：阵容和强度都不足以作为正式比赛的证据，录进来会让模型变差。\n"
    "#\n"
    "# 球队名要用模型认识的写法（国家队用英文国名如 Czech Republic；\n"
    "# 欧战用 football-data.co.uk 的写法如 Ath Madrid）。\n"
    "# 数据源追上之后，这里的重复行会自动忽略，不用手工删。\n"
    "#\n"
    + ",".join(RESULT_COLUMNS) + "\n"
    "# 例（把行首的 # 去掉就会生效）：\n"
    "# INT,2026-09-26,Albania,Belarus,2,0,0,UEFA Nations League\n"
    "# INT,2026-09-29,Finland,Belarus,0,0,0,UEFA Nations League\n"
)


def write_result_template(path: str | Path) -> Path:
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(RESULT_TEMPLATE, encoding="utf-8")
    return path


def load_results(path: str | Path, divs: list[str] | None = None) -> pd.DataFrame:
    """Hand-entered results, in the same shape as the automatic feeds."""
    path = Path(path)
    empty = pd.DataFrame(columns=["div", "date", "home", "away", "hg", "ag",
                                  "neutral", "tournament"])
    if not path.exists():
        return empty
    df = pd.read_csv(path, comment="#", dtype=str, keep_default_na=False)
    df.columns = [str(c).strip() for c in df.columns]
    for c in RESULT_COLUMNS:
        if c not in df.columns:
            df[c] = ""
    out = pd.DataFrame({
        "div": df["comp"].astype(str).str.strip().str.upper(),
        "date": pd.to_datetime(df["date"], errors="coerce"),
        "home": df["home"].astype(str).str.strip(),
        "away": df["away"].astype(str).str.strip(),
        "hg": pd.to_numeric(df["hg"].replace("", pd.NA), errors="coerce"),
        "ag": pd.to_numeric(df["ag"].replace("", pd.NA), errors="coerce"),
        "neutral": df["neutral"].astype(str).str.strip().isin(("1", "true", "True", "yes", "Y")),
        "tournament": df["tournament"].astype(str).str.strip(),
    })
    out = out.dropna(subset=["date", "hg", "ag"])
    out = out[(out["home"] != "") & (out["away"] != "") & (out["div"] != "")]
    if divs is not None:
        out = out[out["div"].isin(divs)]
    if out.empty:
        return empty
    out["hg"] = out["hg"].astype(int)
    out["ag"] = out["ag"].astype(int)
    return out.sort_values("date").reset_index(drop=True)


def merge_results(base: pd.DataFrame, extra: pd.DataFrame,
                  within_days: int = 3) -> tuple[pd.DataFrame, int]:
    """Add hand-entered results the automatic feed does not have yet.

    A hand-entered row is dropped once the feed carries the same fixture, so
    the file never has to be cleaned up by hand. Dates are matched loosely
    because the two sources can disagree by a day over time zones.
    """
    if extra.empty:
        return base, 0
    if base.empty:
        return extra.reset_index(drop=True), len(extra)
    keep = []
    for row in extra.itertuples():
        same = base[(base["home"] == row.home) & (base["away"] == row.away)]
        if same.empty or ((same["date"] - row.date).abs()
                          > pd.Timedelta(days=within_days)).all():
            keep.append(row.Index)
    if not keep:
        return base, 0
    added = extra.loc[keep]
    merged = pd.concat([base, added], ignore_index=True)
    return merged.sort_values("date").reset_index(drop=True), len(added)


def apply_results(base: pd.DataFrame, path: str | Path, divs: list[str],
                  tournaments: list[str] | None = None,
                  label: str = "") -> tuple[pd.DataFrame, list[str]]:
    """Merge the hand-entered results for these competitions into a feed.

    `tournaments` guards the national-team filter: a row naming a tournament
    the config excludes is skipped rather than quietly overriding the setting,
    because a friendly entered by accident makes the model worse. A row with
    the column left blank is taken as a deliberate override and goes in.
    """
    extra = load_results(path, divs)
    notes: list[str] = []
    if extra.empty:
        return base, notes
    if tournaments is not None:
        named = extra["tournament"].astype(str).str.strip()
        bad = extra[(named != "") & (~named.isin(tournaments))]
        for r in bad.itertuples():
            notes.append(f"手录赛果里的「{r.home} vs {r.away}」赛事名 "
                         f"「{r.tournament}」不在 international.tournaments 里，没有计入。")
        extra = extra.drop(bad.index)
    if extra.empty:
        return base, notes
    merged, added = merge_results(base, extra)
    if added:
        notes.append(f"{label}已合并 {added} 场手录赛果"
                     f"（数据源已经收录的重复行自动忽略）。")
    return merged, notes


def append_result(path: str | Path, values: dict) -> None:
    """Append one hand-entered result, keeping the file's comments intact."""
    path = write_result_template(path)
    row = [str(values.get(c, "") or "").strip().replace(",", " ") for c in RESULT_COLUMNS]
    for i, c in enumerate(RESULT_COLUMNS):
        if c in ("comp", "date", "home", "away", "hg", "ag") and not row[i]:
            raise SystemExit(f"{c} 是必填的。")
    with open(path, "a", encoding="utf-8") as f:
        f.write(",".join(row) + "\n")
    print(f"已加入 {Path(path).name}：{row[0]} {row[1]} {row[2]} {row[4]}-{row[5]} {row[3]}")


def append_row(path: str | Path, values: dict) -> None:
    """Append one hand-entered fixture, keeping the file's comments intact."""
    path = write_template(path)
    row = [str(values.get(c, "") or "").strip().replace(",", " ") for c in COLUMNS]
    if not row[COLUMNS.index("comp")] or not row[COLUMNS.index("date")]:
        raise SystemExit("comp 和 date 是必填的。")
    with open(path, "a", encoding="utf-8") as f:
        f.write(",".join(row) + "\n")
    print(f"已加入 {Path(path).name}：{row[0]} {row[1]} {row[3]} vs {row[4]}")


def main() -> None:
    import argparse

    from .config import ROOT, load_config

    ap = argparse.ArgumentParser(description="手填赛程和赔率")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="生成空模板（赛程和赛果各一份）")
    sub.add_parser("list", help="列出已填的赛程和赛果")
    r = sub.add_parser("result", help="追加一场已结束比赛的比分（数据源还没收录时用）")
    r.add_argument("--comp", required=True, help="INT / CL / EL / UECL")
    r.add_argument("--date", required=True, help="YYYY-MM-DD")
    r.add_argument("--home", required=True)
    r.add_argument("--away", required=True)
    r.add_argument("--hg", required=True, help="主队进球（90 分钟）")
    r.add_argument("--ag", required=True, help="客队进球（90 分钟）")
    r.add_argument("--neutral", default="0", help="中立场填 1")
    r.add_argument("--tournament", default="", help="仅 INT 需要，如 UEFA Nations League")
    a = sub.add_parser("add", help="追加一场比赛")
    a.add_argument("--comp", required=True, help="CL / EL / UECL / INT")
    a.add_argument("--date", required=True, help="YYYY-MM-DD")
    a.add_argument("--home", required=True)
    a.add_argument("--away", required=True)
    a.add_argument("--time", default="")
    a.add_argument("--neutral", default="0", help="中立场填 1")
    for k in ("ref_h", "ref_d", "ref_a", "tip_h", "tip_d", "tip_a",
              "ref_o25", "ref_u25", "tip_o25", "tip_u25"):
        a.add_argument(f"--{k.replace('_', '-')}", dest=k, default="")
    args = ap.parse_args()

    cfg = load_config()
    path = Path(ROOT) / cfg["paths"]["manual_fixtures"]
    rpath = Path(ROOT) / cfg["paths"]["manual_results"]
    if args.cmd == "init":
        write_template(path)
        write_result_template(rpath)
        print(f"赛程模板 {path}\n赛果模板 {rpath}")
    elif args.cmd == "list":
        df = load(path)
        print("== 手填赛程 ==")
        print(df.to_string(index=False) if not df.empty else "（空）")
        rs = load_results(rpath)
        print("\n== 手录赛果 ==")
        print(rs.to_string(index=False) if not rs.empty else "（空）")
    elif args.cmd == "result":
        append_result(rpath, vars(args))
    else:
        append_row(path, vars(args))


if __name__ == "__main__":
    main()
