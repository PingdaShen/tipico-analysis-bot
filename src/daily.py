"""Daily run: fit the models, evaluate upcoming fixtures, write the report.

Three sources of fixtures, because the data behind them is different:

* Domestic leagues come from football-data.co.uk with pre-match odds attached,
  and each league gets its own Dixon-Coles. This is the only part that works
  without any manual input.
* European club competitions use the pooled cross-league model (see pool.py).
* National teams use the international model (see intl.py).

The last two have no free fixture-and-odds feed, so their fixtures and prices
are read from manual_fixtures.csv. They also have no closing odds, which
means picks there cannot be scored by CLV — the project's main metric — so
the report keeps them clearly separated from the league picks.

Usage: python -m src.daily [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import pandas as pd
import requests

from . import intl, ledger, manual
from .aliases import load_table
from .config import ROOT, load_config
from .data import load_fixtures, load_history, recent_seasons
from .model import DixonColes
from .pool import fit_pool, load_pool
from .value import evaluate_fixture


def fit_model(history: pd.DataFrame, cfg: dict, ref_date) -> DixonColes:
    m = cfg["model"]
    return DixonColes(xi=m["xi"], ridge=m["ridge"], max_goals=m["max_goals"],
                      min_team_matches=m["min_team_matches"]).fit(history, ref_date)


def competition_names(cfg: dict) -> dict[str, str]:
    """Code -> display name, across leagues and hand-entered competitions."""
    names = dict(cfg["leagues"])
    for code, spec in (cfg.get("manual_competitions") or {}).items():
        names[code] = (spec or {}).get("name", code)
    return names


def league_rows(cfg: dict, today, cache: Path, fixtures_loader, history_loader
                ) -> tuple[list[dict], list[str]]:
    """Evaluate league fixtures from the football-data.co.uk feed."""
    try:
        fixtures = fixtures_loader(list(cfg["leagues"]), cache)
    except requests.RequestException as e:
        return [], [f"赛程数据源无法访问：{e}"]
    stale = ["赛程源里没有未来几天的联赛比赛（fixtures.csv 的更新频率不稳定）。"]
    if fixtures.empty:
        return [], stale
    end = today + pd.Timedelta(days=cfg["value"]["horizon_days"])
    fixtures = fixtures[(fixtures["date"] >= today) & (fixtures["date"] < end)]
    if fixtures.empty:
        return [], stale

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
    return rows, notes


STALE_DAYS = 30


def freshness_note(label: str, latest, today, stale_days: int = STALE_DAYS) -> str | None:
    """Warn when a results source has not caught up yet.

    Both manual competitions depend on feeds that lag: openfootball publishes
    a European season once it is over, and international_results trails the
    most recent international window by weeks. The model is not wrong when it
    has not seen the last window, but the user cannot tell from the numbers,
    so the report says it outright.
    """
    if latest is None or pd.isna(latest):
        return f"{label}：没有任何赛果数据。"
    lag = (pd.Timestamp(today).normalize() - pd.Timestamp(latest).normalize()).days
    if lag < stale_days:
        return None
    return (f"{label}：赛果数据最新到 {pd.Timestamp(latest):%Y-%m-%d}（距今 {lag} 天），"
            f"这之后的比赛模型还没看到。")


def manual_rows(cfg: dict, today, cache: Path, root: Path,
                pool_loader=load_pool, intl_loader=intl.load, manual_loader=manual.load
                ) -> tuple[list[dict], list[str]]:
    """Evaluate the hand-entered European and international fixtures."""
    comps = cfg.get("manual_competitions") or {}
    if not comps:
        return [], []
    path = Path(root) / cfg["paths"]["manual_fixtures"]
    try:
        entered = manual_loader(path)
    except (ValueError, OSError) as e:
        return [], [f"读不了手填赛程 {path.name}：{e}"]
    fixtures = manual.to_fixture_rows(entered)
    if fixtures.empty:
        return [], []
    end = today + pd.Timedelta(days=cfg["value"]["horizon_days"])
    fixtures = fixtures[(fixtures["date"] >= today) & (fixtures["date"] < end)]
    if fixtures.empty:
        return [], []

    aliases = load_table(root)
    models: dict[str, DixonColes | None] = {}
    rows, notes = [], []

    def model_for(kind: str) -> DixonColes | None:
        """Fit a pooled/international model at most once per run."""
        if kind in models:
            return models[kind]
        models[kind] = None
        try:
            if kind == "uefa":
                if not cfg["uefa"].get("enabled", True):
                    notes.append("欧战模型在 config.yaml 里是关闭的。")
                    return None
                pool, info = pool_loader(cfg, cache, today=today)
                pool, pn = manual.apply_results(
                    pool, Path(root) / cfg["paths"]["manual_results"],
                    list(cfg["uefa"]["divs"]) + list(comps), label="欧战：")
                notes.extend(pn)
                models[kind] = fit_pool(pool, cfg, today)
                uefa_latest = info.get("uefa_latest")
                if info.get("uefa", 0) == 0 and not pn:
                    notes.append("没有欧战赛果，跨联赛的实力值无法校准，欧战推荐不可信。")
                else:
                    seen = pool[pool["div"].isin(list(cfg["uefa"]["divs"]) + list(comps))]
                    if not seen.empty:
                        uefa_latest = seen["date"].max()
                    note = freshness_note("欧战", uefa_latest, today)
                    if note:
                        notes.append(note)
            elif kind == "international":
                if not cfg["international"].get("enabled", True):
                    notes.append("国家队模型在 config.yaml 里是关闭的。")
                    return None
                matches = intl_loader(cfg, cache, today=today)
                matches, mn = manual.apply_results(
                    matches, Path(root) / cfg["paths"]["manual_results"], ["INT"],
                    tournaments=cfg["international"].get("tournaments"), label="国家队：")
                notes.extend(mn)
                models[kind] = intl.fit(matches, cfg, today)
                note = freshness_note("国家队",
                                      matches["date"].max() if not matches.empty else None, today)
                if note:
                    notes.append(note)
        except (ValueError, requests.RequestException) as e:
            notes.append(f"{kind} 模型拟合失败：{e}")
        return models[kind]

    for div, group in fixtures.groupby("div"):
        spec = comps.get(div)
        if spec is None:
            notes.append(f"手填赛程里的 {div} 不在 config.yaml 的 manual_competitions 里，跳过。")
            continue
        model = model_for(spec.get("model", "uefa"))
        if model is None:
            continue
        for _, fx in group.iterrows():
            fx = fx.copy()
            bad = False
            for side in ("home", "away"):
                name, hint = manual.resolve_team(fx[side], set(model.teams), aliases)
                if name is None:
                    tip = f"，可能是「{hint}」" if hint else ""
                    notes.append(f"手填赛程里的球队「{fx[side]}」模型不认识{tip}，这场跳过。")
                    bad = True
                else:
                    fx[side] = name
            if bad:
                continue
            ev = evaluate_fixture(fx, model, cfg, neutral=bool(fx.get("neutral", False)))
            if not ev:
                notes.append(f"{fx['home']} vs {fx['away']}：球队比赛数不够"
                             f"（门槛 min_team_matches），跳过")
            rows.extend(ev)
    return rows, notes


def analyze(cfg: dict, today, history_loader=load_history, fixtures_loader=load_fixtures,
            root: Path = ROOT, pool_loader=load_pool, intl_loader=intl.load,
            manual_loader=manual.load) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    today = pd.Timestamp(today).normalize()
    cache = Path(root) / cfg["paths"]["cache"]

    rows, notes = league_rows(cfg, today, cache, fixtures_loader, history_loader)
    mrows, mnotes = manual_rows(cfg, today, cache, root,
                                pool_loader, intl_loader, manual_loader)
    rows += mrows
    notes += mnotes

    all_df = pd.DataFrame(rows)
    if all_df.empty:
        return all_df, all_df, notes
    all_df["league"] = all_df["div"].map(competition_names(cfg)).fillna(all_df["div"])
    all_df["manual"] = all_df["div"].isin(cfg.get("manual_competitions") or {})
    picks = (all_df[all_df["is_candidate"]]
             .sort_values("edge_best", ascending=False)
             .drop_duplicates(subset=["date", "home", "away"])   # 每场比赛最多一注
             .head(cfg["value"]["max_picks"])
             .reset_index(drop=True))
    return all_df, picks, notes


def _pick_table(picks: pd.DataFrame, start: int = 0) -> list[str]:
    lines = [
        "| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for i, (_, p) in enumerate(picks.iterrows(), start=start + 1):
        t = f" {p['time']}" if isinstance(p["time"], str) and p["time"] else ""
        src = "" if p.get("price_source") == "tipico" else "*"
        lines.append(
            f"| {i} | {p['home']} vs {p['away']} | {p['league']} | "
            f"{pd.Timestamp(p['date']):%m-%d}{t} | {p['label']} | {p['fair_odds']:.2f} | "
            f"**{p['min_odds']:.2f}** | {p['best_odds']:.2f}{src} | €{p['stake']:.2f} |"
        )
    return lines


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
        manual_flag = picks["manual"] if "manual" in picks.columns else pd.Series(False, index=picks.index)
        league_picks = picks[~manual_flag]
        other_picks = picks[manual_flag]
        if not league_picks.empty:
            lines += ["## 联赛", ""] + _pick_table(league_picks) + [""]
        if not other_picks.empty:
            lines += [
                "## 欧战 / 国家队（手填赔率）", "",
                "这些赛事没有收盘赔率，**无法计算 CLV**，所以不能用主要指标检验；",
                "欧战的跨联赛实力值本身也比联赛模型不确定得多。请当作次要参考。",
                "",
            ] + _pick_table(other_picks, start=len(league_picks)) + [""]
        lines += [
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
        lines += ["```", "",
                  "「可得赔率」带 * 的是市场最高赔率（只说明这个价格在市场上存在，",
                  "不一定在 Tipico）；不带 * 的是你自己填进来的 Tipico 赔率。", ""]
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
