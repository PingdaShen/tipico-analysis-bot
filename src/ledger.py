"""Bet ledgers (real + paper): add, auto-settle from results, summarize.

Usage:
  python -m src.ledger add <PICK_ID> --odds 2.10 --stake 1
  python -m src.ledger settle
  python -m src.ledger summary
"""
from __future__ import annotations

import argparse
import hashlib
import math
from datetime import date
from itertools import combinations
from pathlib import Path

import pandas as pd

from . import intl, manual
from .aliases import load_table
from .config import ROOT, load_config
from .data import current_season_start, load_history, recent_seasons
from .market import closing_odds, closing_probs, devig, outcome_won
from .openfootball import load_uefa_history

COLUMNS = ["id", "created", "date", "div", "home", "away", "market", "outcome", "label",
           "odds", "stake", "p_final", "status", "result", "pnl", "close_odds", "clv",
           "clv_novig", "close_source", "kind", "system_id"]

# A system bet ("Systemwette", e.g. 5 aus 2 = every 2-leg combination of five
# selections) cannot be stored as its own legs: a double only pays when both
# legs win, so per-leg profit is not defined. Its legs are still written to the
# ledger because CLV is a per-leg quantity and stays perfectly meaningful — but
# they carry stake 0 and no pnl, and the money is accounted for on the system
# row instead. See systems_path / add_system / settle.
SYSTEM_COLUMNS = ["id", "created", "kind", "k", "legs", "stake", "status", "result", "pnl"]
SINGLE, SYSTEM_LEG = "single", "system_leg"


def ledger_path(cfg: dict, root: Path, paper: bool) -> Path:
    return Path(root) / cfg["paths"]["paper_ledger" if paper else "ledger"]


def systems_path(cfg: dict, root: Path = ROOT) -> Path:
    return Path(root) / cfg["paths"].get("systems", "bets/systems.csv")


def load_systems(path: Path) -> pd.DataFrame:
    if not Path(path).exists():
        return pd.DataFrame(columns=SYSTEM_COLUMNS)
    df = pd.read_csv(path, dtype={c: object for c in
                                  ("id", "created", "kind", "legs", "status", "result")})
    for c in SYSTEM_COLUMNS:
        if c not in df.columns:
            df[c] = None
    for c in ("k", "stake", "pnl"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df[SYSTEM_COLUMNS]


def save_systems(df: pd.DataFrame, path: Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df[SYSTEM_COLUMNS].to_csv(path, index=False)


TEXT_COLUMNS = ["id", "created", "div", "home", "away", "market", "outcome", "label",
                "status", "result", "close_source", "kind", "system_id"]
NUM_COLUMNS = ["odds", "stake", "p_final", "pnl", "close_odds", "clv", "clv_novig"]


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
        "clv_novig": None, "close_source": "", "kind": SINGLE, "system_id": "",
    }


def _append(df: pd.DataFrame, rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return df
    new = pd.DataFrame(rows, columns=COLUMNS)
    return new if df.empty else pd.concat([df, new], ignore_index=True)


def append_paper(picks: pd.DataFrame, cfg: dict, root: Path, today) -> int:
    """Log every recommended pick as a paper bet at its minimum acceptable odds.

    Deduplication is by match, not by pick id. A rerun can pick a different
    outcome for the same fixture — changing `value.price_source` flipped
    Shrewsbury vs Exeter from the draw to under 2.5 — and keying on the id
    alone let both land in the ledger, breaking the one-bet-per-match rule the
    picks themselves enforce.
    """
    path = ledger_path(cfg, root, paper=True)
    df = load(path)
    known_ids = set(df["id"])
    played = {(pd.Timestamp(d).date(), h, a)
              for d, h, a in zip(df["date"], df["home"], df["away"])}
    rows = []
    for _, p in picks.iterrows():
        match = (pd.Timestamp(p["date"]).date(), p["home"], p["away"])
        if p["pick_id"] in known_ids or match in played:
            continue
        rows.append(_row_from_pick(p, p["min_odds"], p["stake"], today))
        played.add(match)
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


# --------------------------------------------------------------------------
# Closing odds entered by hand.
#
# CLV is the project's main metric, and for European and international
# competitions nothing supplies a closing line: football-data.co.uk has no
# such matches, and the two results feeds carry results only. Without it those
# picks can only ever be judged on profit and loss, which is far too noisy to
# say anything at the volumes involved here.
#
# The closing line only exists at kick-off, so it has to be written down then.
# One number per bet is enough; the whole market is accepted too because it is
# easier to copy three prices than to pick out the right one.
# --------------------------------------------------------------------------

MARKET_FLAGS = {"1X2": {"H": "close_h", "D": "close_d", "A": "close_a"},
                "OU25": {"O25": "close_o25", "U25": "close_u25"}}


def closing_for_outcome(market: str, outcome: str, values: dict) -> float | None:
    """Pick the closing price for one outcome out of a whole market."""
    if values.get("close") is not None:
        return float(values["close"])
    flag = MARKET_FLAGS.get(market, {}).get(outcome)
    v = values.get(flag) if flag else None
    return float(v) if v is not None else None


def devigged_close(values: dict) -> dict | None:
    """De-vigged closing probabilities, for whichever market was given in full.

    Shown back to the user so they can see what the closing line actually
    implied, which is more informative than the CLV percentage on its own.
    """
    for flags in MARKET_FLAGS.values():
        odds = [values.get(f) for f in flags.values()]
        if any(o is None for o in odds):
            continue
        try:
            odds = [float(o) for o in odds]
        except (TypeError, ValueError):
            continue
        if any(o <= 1.0 for o in odds):
            continue
        return dict(zip(flags, devig(odds)))
    return None


def set_closing(pick_id: str, values: dict, cfg: dict, root: Path = ROOT,
                source: str = "pinnacle") -> int:
    """Record closing odds for one pick in both ledgers and recompute its CLV."""
    touched = 0
    for paper, name in ((False, "真实投注"), (True, "模拟投注")):
        path = ledger_path(cfg, root, paper)
        df = load(path)
        if df.empty:
            continue
        hit = df.index[df["id"] == pick_id]
        if hit.empty:
            continue
        for idx in hit:
            row = df.loc[idx]
            close = closing_for_outcome(row["market"], row["outcome"], values)
            if close is None:
                raise SystemExit(f"没给出 {row['label']} 的收盘赔率。"
                                 f"用 --close，或把整个盘口都填上。")
            if close <= 1.0:
                raise SystemExit(f"收盘赔率 {close} 不合理。")
            old = row["close_odds"]
            clv = round(float(row["odds"]) / close - 1, 4)
            df.loc[idx, "close_odds"] = close
            df.loc[idx, "clv"] = clv
            df.loc[idx, "close_source"] = source
            fair = devigged_close(values)
            novig = None
            if fair and row["outcome"] in fair:
                novig = round(float(row["odds"]) * fair[row["outcome"]] - 1, 4)
            df.loc[idx, "clv_novig"] = novig
            was = f"（原来是 {old:.2f}，已覆盖）" if pd.notna(old) else ""
            extra = f"，去水后 {novig:+.1%}" if novig is not None else "（只给了一个赔率，算不了去水 CLV）"
            print(f"{name}：{row['label']} 下注 {row['odds']:.2f} / 收盘 {close:.2f} "
                  f"-> CLV {clv:+.1%}{extra}{was}")
            touched += 1
        save(df, path)
    if not touched:
        raise SystemExit(f"两个账本里都找不到 ID {pick_id}。")
    fair = devigged_close(values)
    if fair:
        pct = "  ".join(f"{k} {v:.1%}" for k, v in fair.items())
        print(f"去水后的收盘概率：{pct}")
    return touched



def system_payout(k: int, stake: float, legs: list[tuple[float, bool | None]]
                  ) -> tuple[float | None, int, int]:
    """Payout of an n-choose-k system bet, or None while a leg is undecided.

    The stake is split evenly across every combination, and a combination pays
    only when all of its legs won — which is exactly why the money cannot be
    attributed to individual legs.
    """
    if any(won is None for _, won in legs):
        return None, 0, 0
    combos = list(combinations(range(len(legs)), k))
    per = stake / len(combos)
    payout, hit = 0.0, 0
    for c in combos:
        if all(legs[i][1] for i in c):
            payout += per * math.prod(legs[i][0] for i in c)
            hit += 1
    return payout, hit, len(combos)


def add_system(k: int, stake: float, legs: dict[str, float], cfg: dict,
               root: Path = ROOT, paper: bool = False, today=None) -> str:
    """Record one system bet: the system row plus its legs, which carry no money."""
    n = len(legs)
    if not 1 <= k <= n:
        raise SystemExit(f"k 必须在 1 和 {n} 之间，收到 {k}。")
    if n < 2:
        raise SystemExit("系统投注至少要两条腿。")
    today = pd.Timestamp(today).date() if today is not None else date.today()

    files = sorted((Path(root) / cfg["paths"]["reports"]).glob("*_picks.csv"))
    picks = pd.concat([pd.read_csv(f) for f in files], ignore_index=True) if files else pd.DataFrame()
    path = ledger_path(cfg, root, paper)
    df = load(path)

    rows = []
    # hashlib, not hash(): Python randomises string hashing per process, so the
    # id would differ between runs and the duplicate check would never fire
    digest = hashlib.sha1(" ".join(sorted(legs)).encode()).hexdigest()[:4]
    sid = f"SYS-{today:%Y%m%d}-{k}of{n}-{digest}"
    if sid in set(load_systems(systems_path(cfg, root))["id"]):
        raise SystemExit(f"系统投注 {sid} 已经记录过了。")
    for pick_id, odds in legs.items():
        # the same pick may legitimately appear as a single and inside a
        # system, so leg rows are identified by (id, system_id) rather than id
        match = picks[picks["pick_id"] == pick_id] if not picks.empty else picks
        if match.empty:
            raise SystemExit(f"找不到 ID {pick_id}，请从报告里复制。")
        row = _row_from_pick(match.iloc[-1], odds, 0.0, today)
        row.update(kind=SYSTEM_LEG, system_id=sid)
        rows.append(row)
    save(_append(df, rows), path)

    spath = systems_path(cfg, root)
    systems = load_systems(spath)
    combos = math.comb(n, k)
    systems = pd.concat([systems, pd.DataFrame([{
        "id": sid, "created": str(today), "kind": f"{n}/{k}", "k": k,
        "legs": " ".join(legs), "stake": float(stake), "status": "open",
        "result": "", "pnl": None,
    }], columns=SYSTEM_COLUMNS)], ignore_index=True)
    save_systems(systems, spath)
    print(f"已记录系统投注 {sid}：{n} 选 {k}，共 {combos} 注，"
          f"总投入 €{stake:.2f}（每注 €{stake/combos:.3f}）")
    for pick_id, odds in legs.items():
        print(f"   {pick_id} @ {odds}")
    return sid


def settle_systems(cfg: dict, root: Path, paper: bool) -> None:
    """Close out any system whose legs have all been decided."""
    spath = systems_path(cfg, root)
    systems = load_systems(spath)
    if systems.empty:
        return
    df = load(ledger_path(cfg, root, paper))
    if df.empty:
        return
    changed = False
    for idx, sysrow in systems[systems["status"] == "open"].iterrows():
        sid, ids = sysrow["id"], str(sysrow["legs"]).split()
        mine = df[df["system_id"] == sid]
        if not set(ids) <= set(mine["id"]):
            continue                       # this ledger does not hold the system
        legs = []
        for i in ids:
            r = mine[mine["id"] == i].iloc[0]
            won = None if r["status"] != "settled" else ("赢" in str(r["result"]))
            legs.append((float(r["odds"]), won))
        payout, hit, combos = system_payout(int(sysrow["k"]), float(sysrow["stake"]), legs)
        if payout is None:
            continue
        won_legs = sum(1 for _, w in legs if w)
        systems.loc[idx, "status"] = "settled"
        systems.loc[idx, "pnl"] = round(payout - float(sysrow["stake"]), 2)
        systems.loc[idx, "result"] = (f"{len(legs)} 中 {won_legs}，{combos} 注中 {hit} 注")
        changed = True
    if changed:
        save_systems(systems, spath)



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
                cp, _ = closing_probs(g, r["market"])
                df.loc[idx, "status"] = "settled"
                df.loc[idx, "result"] = f"{int(g['hg'])}-{int(g['ag'])} {'赢' if won else '输'}"
                # a system leg carries no money of its own; the system row does
                df.loc[idx, "pnl"] = (None if r["kind"] == SYSTEM_LEG else
                                      round(r["stake"] * (r["odds"] - 1) if won else -r["stake"], 2))
                if close:
                    df.loc[idx, "close_odds"] = close
                    df.loc[idx, "clv"] = round(r["odds"] / close - 1, 4)
                    df.loc[idx, "close_source"] = close_source
                    if cp:
                        df.loc[idx, "clv_novig"] = round(r["odds"] * cp[r["outcome"]] - 1, 4)
        save(df, path)
        settle_systems(cfg, root, paper)


def summarize(df: pd.DataFrame, systems: pd.DataFrame | None = None) -> dict:
    """Totals for one ledger.

    clv_novig is the headline: it divides by a de-vigged closing probability,
    so a bet priced against a soft line means the same as one priced against
    Pinnacle. The raw avg_clv does not — the two lines differ by about 3
    points of margin across these leagues. sharp_clv keeps the raw formula but
    counts only Pinnacle-priced bets. See market.closing_probs.
    """
    singles = df[df["kind"].fillna(SINGLE) != SYSTEM_LEG]
    s = singles[singles["status"] == "settled"]
    staked = float(s["stake"].sum()) if not s.empty else 0.0
    pnl = float(pd.to_numeric(s["pnl"], errors="coerce").sum()) if not s.empty else 0.0

    # system bets keep their money on their own row, but their legs still carry
    # a CLV, so they add to staked/pnl without disturbing the CLV columns
    sys_settled = sys_open = 0
    if systems is not None and not systems.empty:
        done = systems[systems["status"] == "settled"]
        sys_settled, sys_open = len(done), int((systems["status"] == "open").sum())
        staked += float(pd.to_numeric(done["stake"], errors="coerce").sum())
        pnl += float(pd.to_numeric(done["pnl"], errors="coerce").sum())
    # CLV is fixed the moment the match kicks off and does not depend on the
    # result, so it counts every bet that has a closing price — waiting for
    # settlement would throw away the one advantage the metric has over P&L.
    clv = pd.to_numeric(df["clv"], errors="coerce").dropna()
    novig = pd.to_numeric(df["clv_novig"], errors="coerce").dropna()
    sharp = pd.to_numeric(df.loc[df["close_source"] == "pinnacle", "clv"],
                          errors="coerce").dropna()
    return {
        "settled": len(s),
        "open": int((singles["status"] == "open").sum()),
        "systems_settled": sys_settled,
        "systems_open": sys_open,
        "staked": staked,
        "pnl": pnl,
        "roi": pnl / staked if staked else None,
        "hit_rate": float((pd.to_numeric(s["pnl"], errors="coerce") > 0).mean())
                    if not s.empty else None,
        "avg_clv": float(clv.mean()) if not clv.empty else None,
        "clv_novig": float(novig.mean()) if not novig.empty else None,
        "novig_n": int(len(novig)),
        "sharp_clv": float(sharp.mean()) if not sharp.empty else None,
        "sharp_n": int(len(sharp)),
        "no_clv": int(len(df) - len(clv)),
    }


def format_summary(name: str, d: dict) -> str:
    def pct(v):
        return "—" if v is None else f"{v:+.1%}"
    hit = "—" if d["hit_rate"] is None else f"{d['hit_rate']:.0%}"
    extra = ""
    if d["no_clv"]:
        extra += f"，{d['no_clv']} 注还没有收盘赔率"
    # the Pinnacle breakdown only when such bets exist: league bets get that
    # line automatically from football-data.co.uk, but hand-entered ones
    # cannot — oddsportal filters Pinnacle out for German visitors — so the
    # figure would otherwise sit there permanently empty
    sharp = (f"，其中对 Pinnacle 收盘 {pct(d['sharp_clv'])}（{d['sharp_n']} 注）"
             if d["sharp_n"] else "")
    if d.get("systems_settled") or d.get("systems_open"):
        extra = (f"；系统投注已结算 {d['systems_settled']} 组、"
                 f"未结算 {d['systems_open']} 组" + extra)
    return (f"{name}：已结算 {d['settled']} 注，未结算 {d['open']} 注，"
            f"投入 €{d['staked']:.2f}，盈亏 €{d['pnl']:+.2f}，ROI {pct(d['roi'])}，"
            f"命中率 {hit}，去水 CLV {pct(d['clv_novig'])}（{d['novig_n']} 注）"
            f"{sharp}{extra}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Bet ledger")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("pick_id")
    a.add_argument("--odds", type=float, required=True)
    a.add_argument("--stake", type=float, required=True)
    sub.add_parser("settle")
    sub.add_parser("summary")
    y = sub.add_parser("system", help="记录一次系统投注（Systemwette，如 5 选 2）")
    y.add_argument("--k", type=int, required=True, help="每注串几层，5 对 2 就填 2")
    y.add_argument("--stake", type=float, required=True, help="总投入（不是每注）")
    y.add_argument("--leg", action="append", required=True, metavar="ID=赔率",
                   help="一条腿，重复使用。例：--leg 20261009-F2-Nancy-Guingamp-A=3.80")
    y.add_argument("--paper", action="store_true", help="记进模拟账本")
    c = sub.add_parser("close", help="录入收盘赔率（欧战/国家队唯一的 CLV 来源）")
    c.add_argument("pick_id", help="报告里的 ID")
    c.add_argument("--close", type=float, help="这个选项的收盘赔率")
    c.add_argument("--close-h", dest="close_h", type=float, help="收盘 主胜")
    c.add_argument("--close-d", dest="close_d", type=float, help="收盘 平局")
    c.add_argument("--close-a", dest="close_a", type=float, help="收盘 客胜")
    c.add_argument("--close-o25", dest="close_o25", type=float, help="收盘 大 2.5")
    c.add_argument("--close-u25", dest="close_u25", type=float, help="收盘 小 2.5")
    c.add_argument("--source", choices=["pinnacle", "average"], default="pinnacle",
                   help="你记的是哪条线。只有 pinnacle 计入 sharp_clv")
    args = ap.parse_args()
    cfg = load_config()
    if args.cmd == "add":
        add(args.pick_id, args.odds, args.stake, cfg)
    elif args.cmd == "system":
        legs = {}
        for item in args.leg:
            if "=" not in item:
                raise SystemExit(f"--leg 要写成 ID=赔率，收到 {item!r}")
            pid, odds = item.rsplit("=", 1)
            try:
                legs[pid.strip()] = float(odds)
            except ValueError:
                raise SystemExit(f"赔率不是数字：{odds!r}")
        add_system(args.k, args.stake, legs, cfg, paper=args.paper)
    elif args.cmd == "close":
        set_closing(args.pick_id, vars(args), cfg, source=args.source)
    elif args.cmd == "settle":
        settle(cfg)
        print("结算完成。")
    else:
        systems = load_systems(systems_path(cfg, ROOT))
        for paper, name in ((False, "真实投注"), (True, "模拟投注")):
            df = load(ledger_path(cfg, ROOT, paper))
            mine = systems[systems["id"].isin(df["system_id"].dropna().unique())]
            print(format_summary(name, summarize(df, mine)))


if __name__ == "__main__":
    main()
