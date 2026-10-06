"""Bet ledgers (real + paper): add, auto-settle from results, summarize.

Usage:
  python -m src.ledger add <PICK_ID> --odds 2.10 --stake 1
  python -m src.ledger settle
  python -m src.ledger summary
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import pandas as pd

from . import intl, manual
from .aliases import load_table
from .config import ROOT, load_config
from .data import current_season_start, load_history, recent_seasons
from .market import closing_odds, outcome_won
from .openfootball import load_uefa_history

COLUMNS = ["id", "created", "date", "div", "home", "away", "market", "outcome", "label",
           "odds", "stake", "p_final", "status", "result", "pnl", "close_odds", "clv",
           "close_source"]


def ledger_path(cfg: dict, root: Path, paper: bool) -> Path:
    return Path(root) / cfg["paths"]["paper_ledger" if paper else "ledger"]


TEXT_COLUMNS = ["id", "created", "div", "home", "away", "market", "outcome", "label",
                "status", "result", "close_source"]
NUM_COLUMNS = ["odds", "stake", "p_final", "pnl", "close_odds", "clv"]


def load(path: Path) -> pd.DataFrame:
    if not Path(path).exists():
        return pd.DataFrame(columns=COLUMNS)
    df = pd.read_csv(path, dtype={c: object for c in TEXT_COLUMNS})
    for c in COLUMNS:                       # tolerate ledgers written before a column existed
        if c not in df.columns:
            df[c] = None
    df["date"] = pd.to_datetime(df["date"])
    for c in TEXT_COLUMNS:
        df[c] = df[c].astype(object).where(df[c].notna(), "")
    for c in NUM_COLUMNS:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype(float)
    return df


def save(df: pd.DataFrame, path: Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df[COLUMNS].to_csv(path, index=False)


def _row_from_pick(p, odds: float, stake: float, today) -> dict:
    return {
        "id": p["pick_id"], "created": str(today), "date": pd.Timestamp(p["date"]),
        "div": p["div"], "home": p["home"], "away": p["away"],
        "market": p["market"], "outcome": p["outcome"], "label": p["label"],
        "odds": round(float(odds), 2), "stake": float(stake),
        "p_final": round(float(p["p_final"]), 4), "status": "open",
        "result": "", "pnl": None, "close_odds": None, "clv": None,
        "close_source": "",
    }


def _append(df: pd.DataFrame, rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return df
    new = pd.DataFrame(rows, columns=COLUMNS)
    return new if df.empty else pd.concat([df, new], ignore_index=True)


def append_paper(picks: pd.DataFrame, cfg: dict, root: Path, today) -> int:
    """Log every recommended pick as a paper bet at its minimum acceptable odds."""
    path = ledger_path(cfg, root, paper=True)
    df = load(path)
    known = set(df["id"])
    rows = [_row_from_pick(p, p["min_odds"], p["stake"], today)
            for _, p in picks.iterrows() if p["pick_id"] not in known]
    save(_append(df, rows), path)
    return len(rows)


def add(pick_id: str, odds: float, stake: float, cfg: dict, root: Path = ROOT) -> None:
    files = sorted((Path(root) / cfg["paths"]["reports"]).glob("*_picks.csv"))
    picks = pd.concat([pd.read_csv(f) for f in files], ignore_index=True) if files else pd.DataFrame()
    match = picks[picks["pick_id"] == pick_id] if not picks.empty else picks
    if match.empty:
        raise SystemExit(f"找不到 ID {pick_id}，请从每日报告里复制。")
    p = match.iloc[-1]
    if odds < p["min_odds"] - 1e-9:
        print(f"[提醒] 你的赔率 {odds} 低于建议最低赔率 {p['min_odds']:.2f}，按规则本该跳过。")
    path = ledger_path(cfg, root, paper=False)
    df = load(path)
    if pick_id in set(df["id"]):
        raise SystemExit("这注已经记录过了。")
    save(_append(df, [_row_from_pick(p, odds, stake, date.today())]), path)
    print(f"已记录：{p['label']} @ {odds}，注额 €{stake}")


def results_for_div(div: str, cfg: dict, cache: Path, today=None,
                    history_loader=load_history, intl_loader=intl.load,
                    uefa_loader=load_uefa_history, root: Path = ROOT) -> pd.DataFrame:
    """Finished matches for one competition code.

    Leagues come from football-data.co.uk with closing odds attached, so those
    bets also get a CLV. The hand-entered competitions have no odds source at
    all: national-team results come from international_results and European
    results from openfootball, both results-only, so those bets settle for
    profit and loss but carry no CLV. openfootball also publishes a season
    late, so a recent European bet may simply stay open for a while.
    """
    if div in cfg["leagues"]:
        return history_loader(div, recent_seasons(2, today), cache, today=today, fresh=True)
    spec = (cfg.get("manual_competitions") or {}).get(div) or {}
    kind = spec.get("model")
    if kind is None:
        return pd.DataFrame(columns=["div", "date", "home", "away", "hg", "ag"])

    if kind == "international":
        base = intl_loader(cfg, cache, today=today, fresh=True)
    else:
        start = current_season_start(pd.Timestamp(today).date() if today else None)
        base = uefa_loader([start - 1, start], cache, fresh=True)
        if not base.empty:
            from .aliases import resolve_names
            base = resolve_names(base, load_table(root))[0]
    # a bet can only be settled from a result we have, and for these
    # competitions the hand-entered file is often the only place it exists yet
    merged, _ = manual.apply_results(
        base, Path(root) / cfg["paths"]["manual_results"], [div])
    return merged


def settle(cfg: dict, root: Path = ROOT, history_loader=load_history, today=None,
           **loaders) -> None:
    cache = Path(root) / cfg["paths"]["cache"]
    for paper in (False, True):
        path = ledger_path(cfg, root, paper)
        df = load(path)
        if df.empty:
            continue
        open_rows = df[df["status"] == "open"]
        for div in open_rows["div"].unique():
            hist = results_for_div(div, cfg, cache, today=today,
                                   history_loader=history_loader, root=root, **loaders)
            if hist.empty:
                n = int((open_rows["div"] == div).sum())
                print(f"[提示] {div}：找不到赛果，{n} 注先留着未结算。")
                continue
            for idx, r in open_rows[open_rows["div"] == div].iterrows():
                m = hist[(hist["home"] == r["home"]) & (hist["away"] == r["away"])
                         & ((hist["date"] - r["date"]).abs() <= pd.Timedelta(days=3))]
                if m.empty:
                    continue
                g = m.iloc[0]
                won = outcome_won(r["outcome"], int(g["hg"]), int(g["ag"]))
                close, close_source = closing_odds(g, r["market"], r["outcome"])
                df.loc[idx, "status"] = "settled"
                df.loc[idx, "result"] = f"{int(g['hg'])}-{int(g['ag'])} {'赢' if won else '输'}"
                df.loc[idx, "pnl"] = round(r["stake"] * (r["odds"] - 1) if won else -r["stake"], 2)
                if close:
                    df.loc[idx, "close_odds"] = close
                    df.loc[idx, "clv"] = round(r["odds"] / close - 1, 4)
                    df.loc[idx, "close_source"] = close_source
        save(df, path)


def summarize(df: pd.DataFrame) -> dict:
    """Totals for one ledger.

    sharp_clv counts only bets measured against Pinnacle's closing line. That
    is the honest number: a CLV computed against the market average close is
    beating a 4-6% margin line and means much less. See market.closing_odds.
    """
    s = df[df["status"] == "settled"]
    staked = float(s["stake"].sum()) if not s.empty else 0.0
    pnl = float(pd.to_numeric(s["pnl"]).sum()) if not s.empty else 0.0
    clv = pd.to_numeric(s["clv"], errors="coerce").dropna() if not s.empty else pd.Series(dtype=float)
    sharp = (pd.to_numeric(s.loc[s["close_source"] == "pinnacle", "clv"], errors="coerce").dropna()
             if not s.empty else pd.Series(dtype=float))
    return {
        "settled": len(s),
        "open": int((df["status"] == "open").sum()),
        "staked": staked,
        "pnl": pnl,
        "roi": pnl / staked if staked else None,
        "hit_rate": float((pd.to_numeric(s["pnl"]) > 0).mean()) if not s.empty else None,
        "avg_clv": float(clv.mean()) if not clv.empty else None,
        "sharp_clv": float(sharp.mean()) if not sharp.empty else None,
        "sharp_n": int(len(sharp)),
        "no_clv": int(len(s) - len(clv)),
    }


def format_summary(name: str, d: dict) -> str:
    def pct(v):
        return "—" if v is None else f"{v:+.1%}"
    hit = "—" if d["hit_rate"] is None else f"{d['hit_rate']:.0%}"
    extra = ""
    if d["no_clv"]:
        extra += f"，{d['no_clv']} 注没有收盘赔率（欧战/国家队）"
    return (f"{name}：已结算 {d['settled']} 注，未结算 {d['open']} 注，"
            f"投入 €{d['staked']:.2f}，盈亏 €{d['pnl']:+.2f}，ROI {pct(d['roi'])}，"
            f"命中率 {hit}，对锐价收盘的 CLV {pct(d['sharp_clv'])}"
            f"（{d['sharp_n']} 注）{extra}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Bet ledger")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("pick_id")
    a.add_argument("--odds", type=float, required=True)
    a.add_argument("--stake", type=float, required=True)
    sub.add_parser("settle")
    sub.add_parser("summary")
    args = ap.parse_args()
    cfg = load_config()
    if args.cmd == "add":
        add(args.pick_id, args.odds, args.stake, cfg)
    elif args.cmd == "settle":
        settle(cfg)
        print("结算完成。")
    else:
        for paper, name in ((False, "真实投注"), (True, "模拟投注")):
            print(format_summary(name, summarize(load(ledger_path(cfg, ROOT, paper)))))


if __name__ == "__main__":
    main()
