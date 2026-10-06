"""Daily run: fit one model per league, evaluate upcoming fixtures, write the report.

Usage: python -m src.daily [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import pandas as pd
import requests

from . import ledger
from .config import ROOT, load_config
from .data import load_fixtures, load_history, recent_seasons
from .model import DixonColes
from .value import evaluate_fixture


def fit_model(history: pd.DataFrame, cfg: dict, ref_date) -> DixonColes:
    m = cfg["model"]
    return DixonColes(xi=m["xi"], ridge=m["ridge"], max_goals=m["max_goals"],
                      min_team_matches=m["min_team_matches"]).fit(history, ref_date)


def analyze(cfg: dict, today, history_loader=load_history, fixtures_loader=load_fixtures,
            root: Path = ROOT) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    today = pd.Timestamp(today).normalize()
    cache = Path(root) / cfg["paths"]["cache"]
    try:
        fixtures = fixtures_loader(list(cfg["leagues"]), cache)
    except requests.RequestException as e:
        empty = pd.DataFrame()
        return empty, empty, [f"赛程数据源无法访问：{e}"]
    end = today + pd.Timedelta(days=cfg["value"]["horizon_days"])
    fixtures = fixtures[(fixtures["date"] >= today) & (fixtures["date"] < end)]

    rows, notes = [], []
    seasons = recent_seasons(cfg["history_seasons"], today.date())
    for div, group in fixtures.groupby("div"):
        history = history_loader(div, seasons, cache, today=today.date())
        try:
            model = fit_model(history, cfg, today)
        except ValueError as e:
            notes.append(f"{cfg['leagues'][div]}：跳过（{e}）")
            continue
        for _, fx in group.iterrows():
            ev = evaluate_fixture(fx, model, cfg)
            if not ev:
                notes.append(f"{fx['home']} vs {fx['away']}：球队数据不足（可能是升班马），跳过")
            rows.extend(ev)

    all_df = pd.DataFrame(rows)
    if all_df.empty:
        return all_df, all_df, notes
    all_df["league"] = all_df["div"].map(cfg["leagues"])
    picks = (all_df[all_df["is_candidate"]]
             .sort_values("edge_best", ascending=False)
             .drop_duplicates(subset=["date", "home", "away"])   # 每场比赛最多一注
             .head(cfg["value"]["max_picks"])
             .reset_index(drop=True))
    return all_df, picks, notes


def render_report(today, picks: pd.DataFrame, all_df: pd.DataFrame,
                  notes: list[str], cfg: dict) -> str:
    v, s = cfg["value"], cfg["staking"]
    n_matches = 0 if all_df.empty else all_df[["date", "home", "away"]].drop_duplicates().shape[0]
    lines = [
        f"# 今日投注建议 · {pd.Timestamp(today):%Y-%m-%d}",
        "",
        f"本金 €{s['bankroll']:.0f} · 最低赔率 {v['min_odds']:.2f} · 最低优势 {v['min_edge']:.0%} · "
        f"分析了 {n_matches} 场比赛",
        "",
    ]
    if picks.empty:
        lines += ["**今天没有符合条件的投注。** 不下注也是策略的一部分。", ""]
    else:
        lines += [
            "| # | 比赛 | 联赛 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 市场最高 | 注额 |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        for i, p in picks.iterrows():
            t = f" {p['time']}" if isinstance(p["time"], str) and p["time"] else ""
            lines.append(
                f"| {i + 1} | {p['home']} vs {p['away']} | {p['league']} | "
                f"{pd.Timestamp(p['date']):%m-%d}{t} | {p['label']} | {p['fair_odds']:.2f} | "
                f"**{p['min_odds']:.2f}** | {p['best_odds']:.2f} | €{p['stake']:.2f} |"
            )
        lines += [
            "",
            "## 怎么用",
            "1. 在 Tipico App 里找到比赛和对应选项。",
            "2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。",
            "3. 下注后记录（把 ID 和实际赔率填进去）：",
            "",
            "```",
        ]
        for _, p in picks.iterrows():
            lines.append(f"python -m src.ledger add {p['pick_id']} --odds <Tipico赔率> "
                         f"--stake {p['stake']:.2f}")
        lines += ["```", ""]
    if notes:
        lines += ["## 备注", *[f"- {n}" for n in notes], ""]
    lines += [
        "---",
        "开球时间来自数据源，可能是英国时间，请以 Tipico 显示为准。"
        "本报告是模型输出，不保证盈利；只用亏得起的钱。",
    ]
    return "\n".join(lines)


def run(cfg: dict, today=None, root: Path = ROOT, **loaders) -> pd.DataFrame:
    today = pd.Timestamp(today or date.today()).normalize()
    all_df, picks, notes = analyze(cfg, today, root=root, **loaders)
    reports = Path(root) / cfg["paths"]["reports"]
    reports.mkdir(parents=True, exist_ok=True)
    report = render_report(today, picks, all_df, notes, cfg)
    (reports / f"{today:%Y-%m-%d}.md").write_text(report, encoding="utf-8")
    (reports / "latest.md").write_text(report, encoding="utf-8")
    if not all_df.empty:
        all_df.to_csv(reports / f"{today:%Y-%m-%d}_all.csv", index=False)
    if not picks.empty:
        picks.to_csv(reports / f"{today:%Y-%m-%d}_picks.csv", index=False)
        ledger.append_paper(picks, cfg, root, today.date())
    print(report)
    return picks


def main() -> None:
    ap = argparse.ArgumentParser(description="Daily betting report")
    ap.add_argument("--date", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--config", help="path to config.yaml")
    args = ap.parse_args()
    run(load_config(args.config), today=args.date)


if __name__ == "__main__":
    main()
