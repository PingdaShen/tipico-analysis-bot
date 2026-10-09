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
from .value import evaluate_combos, evaluate_fixture


def fit_model(history: pd.DataFrame, cfg: dict, ref_date) -> DixonColes:
    m = cfg["model"]
    return DixonColes(xi=m["xi"], ridge=m["ridge"], max_goals=m["max_goals"],
                      min_team_matches=m["min_team_matches"]).fit(history, ref_date)


def league_history(div: str, cfg: dict, cache: Path, root: Path, today,
                   history_loader) -> tuple[pd.DataFrame, list[str]]:
    """A league's results, with any hand-entered scores merged in.

    football-data publishes a round a day or two after it is played, so
    without this the model would price Saturday's card without having seen
    Friday's. The international and European models already do the same.
    """
    seasons = recent_seasons(cfg["history_seasons"], today.date())
    base = history_loader(div, seasons, cache, today=today.date())
    return manual.apply_results(base, Path(root) / cfg["paths"]["manual_results"],
                                [div], label=f"{cfg['leagues'].get(div, div)}：")


def shift_kickoff(fixtures: pd.DataFrame, hours: int) -> pd.DataFrame:
    """Move feed kick-off times onto the user's clock.

    football-data.co.uk publishes UK times. The UK and Germany change to
    summer time on the same dates, so the gap is a constant hour all year and
    a plain offset is right — no timezone database needed. Only the feed is
    shifted; a hand-entered fixture already carries the time the user typed.
    """
    if not hours or fixtures.empty or "Time" not in fixtures.columns:
        return fixtures

    def shift(value):
        text = str(value).strip()
        if not text or ":" not in text:
            return value
        try:
            h, m = (int(x) for x in text.split(":")[:2])
        except ValueError:
            return value
        total = h + hours
        # a kick-off crossing midnight keeps its date here, so mark it
        return f"{total % 24:02d}:{m:02d}" + ("(+1)" if total >= 24 else "")

    fixtures = fixtures.copy()
    fixtures["Time"] = fixtures["Time"].map(shift)
    return fixtures


def competition_names(cfg: dict) -> dict[str, str]:
    """Code -> display name, across leagues and hand-entered competitions."""
    names = dict(cfg["leagues"])
    for code, spec in (cfg.get("manual_competitions") or {}).items():
        names[code] = (spec or {}).get("name", code)
    return names


def league_rows(cfg: dict, today, cache: Path, root: Path, fixtures_loader,
                history_loader, entered: pd.DataFrame | None = None
                ) -> tuple[list[dict], list[str], pd.DataFrame]:
    """Evaluate league fixtures from the football-data.co.uk feed.

    Hand-entered rows for a match the feed already has are merged in rather
    than evaluated separately, so Tipico's own price replaces the market proxy
    instead of competing with it. Whatever did not match is handed back for
    manual_rows to price on its own.
    """
    try:
        fixtures = fixtures_loader(list(cfg["leagues"]), cache)
    except requests.RequestException as e:
        return [], [f"赛程数据源无法访问：{e}"]
    fixtures_all_divs = sorted(set(fixtures["div"])) if not fixtures.empty else []
    leftover = entered if entered is not None else pd.DataFrame()
    if fixtures.empty:
        return [], ["赛程源 fixtures.csv 是空的，今天没有联赛可以分析。"], leftover
    feed_latest = fixtures["date"].max()
    end = today + pd.Timedelta(days=cfg["value"]["horizon_days"])
    fixtures = fixtures[(fixtures["date"] >= today) & (fixtures["date"] < end)]
    if fixtures.empty:
        lag = (today.normalize() - pd.Timestamp(feed_latest).normalize()).days
        covered = sorted(set(fixtures_all_divs) & set(cfg["leagues"])) if fixtures_all_divs else []
        note = (f"赛程源里没有 {today:%m-%d} 起 {cfg['value']['horizon_days']} 天内的联赛比赛。"
                f"fixtures.csv 最新的一场是 {pd.Timestamp(feed_latest):%Y-%m-%d}")
        note += f"（已经是 {lag} 天前）" if lag > 0 else ""
        note += f"，只覆盖 {len(covered)} 个联赛：{'、'.join(covered)}。" if covered else "。"
        note += ("football-data.co.uk 的赛程是周五下午发布周末场次、周二下午发布周中场次，"
                 "国际比赛周没有联赛可发就不会更新。等不及可以用 manual_fixtures.csv 手填。")
        return [], [note], leftover

    fixtures = shift_kickoff(fixtures,
                             (cfg.get("report") or {}).get("kickoff_offset_hours", 0))
    if entered is not None and not entered.empty:
        fixtures, leftover = manual.overlay(fixtures, entered)

    rows, notes = [], []
    for div, group in fixtures.groupby("div"):
        history, hnotes = league_history(div, cfg, cache, root, today, history_loader)
        notes.extend(hnotes)
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
            if cfg["value"].get("combos"):
                rows.extend(evaluate_combos(fx, model, cfg))
    return rows, notes, leftover


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


def manual_rows(cfg: dict, today, cache: Path, root: Path, fixtures: pd.DataFrame | None,
                pool_loader=load_pool, intl_loader=intl.load,
                history_loader=load_history) -> tuple[list[dict], list[str]]:
    """Evaluate hand-entered fixtures.

    Covers the European and international competitions, which have no feed at
    all, and also plain league matches: fixtures.csv is unreliable — on
    2026-10-06 it had not been regenerated since 10-02, listed only past dates
    and covered 7 of the 22 configured leagues — so typing a league match in by
    hand has to be possible. A league entered this way is priced by its own
    Dixon-Coles, exactly as a fixture from the feed would be, and settles
    automatically with a real CLV because its results do have a source.
    """
    comps = cfg.get("manual_competitions") or {}
    if fixtures is None or fixtures.empty:
        return [], []

    aliases = load_table(root)
    models: dict[str, DixonColes | None] = {}
    rows, notes = [], []

    def league_model(div: str) -> DixonColes | None:
        """The per-league model, fitted at most once per run."""
        if div in models:
            return models[div]
        models[div] = None
        try:
            history, _ = league_history(div, cfg, cache, root, today, history_loader)
            models[div] = fit_model(history, cfg, today)
        except ValueError as e:
            notes.append(f"{cfg['leagues'][div]}：跳过手填的比赛（{e}）")
        return models[div]

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
        if div in cfg["leagues"]:
            model = league_model(div)
        elif div in comps:
            model = model_for((comps[div] or {}).get("model", "uefa"))
        else:
            known = "、".join([*cfg["leagues"], *comps])
            notes.append(f"手填赛程里的 {div} 不是已知的赛事代码，跳过。可用的有：{known}")
            continue
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
            neutral = bool(fx.get("neutral", False))
            ev = evaluate_fixture(fx, model, cfg, neutral=neutral)
            if not ev:
                notes.append(f"{fx['home']} vs {fx['away']}：球队比赛数不够"
                             f"（门槛 min_team_matches），跳过")
            rows.extend(ev)
            if cfg["value"].get("combos"):
                rows.extend(evaluate_combos(fx, model, cfg, neutral=neutral))
    return rows, notes


def analyze(cfg: dict, today, history_loader=load_history, fixtures_loader=load_fixtures,
            root: Path = ROOT, pool_loader=load_pool, intl_loader=intl.load,
            manual_loader=manual.load) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    today = pd.Timestamp(today).normalize()
    cache = Path(root) / cfg["paths"]["cache"]

    notes: list[str] = []
    path = Path(root) / cfg["paths"]["manual_fixtures"]
    try:
        entered = manual.to_fixture_rows(manual_loader(path))
    except (ValueError, OSError) as e:
        entered, _ = pd.DataFrame(), notes.append(f"读不了手填赛程 {path.name}：{e}")
    if not entered.empty:
        end = today + pd.Timedelta(days=cfg["value"]["horizon_days"])
        entered = entered[(entered["date"] >= today) & (entered["date"] < end)]

    rows, lnotes, leftover = league_rows(cfg, today, cache, root, fixtures_loader,
                                         history_loader, entered)
    mrows, mnotes = manual_rows(cfg, today, cache, root, leftover,
                                pool_loader, intl_loader, history_loader)
    rows += mrows
    notes += lnotes + mnotes

    all_df = pd.DataFrame(rows)
    if all_df.empty:
        return all_df, all_df, notes
    all_df["league"] = all_df["div"].map(competition_names(cfg)).fillna(all_df["div"])
    all_df["manual"] = all_df["div"].isin(cfg.get("manual_competitions") or {})
    # max_picks applies per match day. A Friday run covers Saturday too, and
    # Saturday's card is ten times the size, so a global cap let tomorrow take
    # every slot and left tonight's matches unreported.
    picks = (all_df[all_df["is_candidate"]]
             .sort_values("edge_best", ascending=False)
             .drop_duplicates(subset=["date", "home", "away"])   # 每场比赛最多一注
             .groupby("date", group_keys=False, sort=False)
             .head(cfg["value"]["max_picks"])
             .sort_values(["date", "edge_best"], ascending=[True, False])
             .reset_index(drop=True))
    return all_df, picks, notes


def _pick_table(picks: pd.DataFrame, start: int = 0) -> list[str]:
    lines = [
        "| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for i, (_, p) in enumerate(picks.iterrows(), start=start + 1):
        t = f" {p['time']}" if isinstance(p["time"], str) and p["time"] else ""
        src = "" if str(p.get("price_source", "")).startswith("tipico") else "*"
        lines.append(
            f"| {i} | {p['home']} vs {p['away']} | {p['league']} | "
            f"{pd.Timestamp(p['date']):%m-%d}{t} | {p['label']} | {p['fair_odds']:.2f} | "
            f"**{p['min_odds']:.2f}** | {p['best_odds']:.2f}{src} | €{p['stake']:.2f} |"
        )
    return lines


def _manual_picks(picks: pd.DataFrame) -> pd.Series:
    if "manual" in picks.columns:
        return picks["manual"].astype(bool)
    return pd.Series(False, index=picks.index)


def _id_section(picks: pd.DataFrame) -> list[str]:
    """The pick IDs, on their own and easy to copy.

    They used to appear only inside a shell command, which is the one way the
    user does not record bets: record-bet and record-close are web forms, so
    the ID is needed on a phone — twice per bet when the closing odds have to
    be entered too. Each ID gets its own fenced block, which GitHub renders
    with a copy button.
    """
    if picks.empty:
        return []
    forms = "record-bet 和 record-close" if _manual_picks(picks).any() else "record-bet"
    lines = ["## 投注 ID", "",
             f"{forms} 表单要填这个（点代码块右上角可直接复制）：", ""]
    for i, (_, p) in enumerate(picks.iterrows(), start=1):
        lines += [f"**{i}. {p['home']} vs {p['away']} — {p['label']}**",
                  "", "```", str(p["pick_id"]), "```", ""]
    return lines


def _how_to_section(picks: pd.DataFrame) -> list[str]:
    manual_flag = _manual_picks(picks)
    lines = [
        "## 怎么用",
        "",
        "1. 在 Tipico App 里找到比赛和对应选项。",
        "2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。",
        "3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。",
    ]
    if bool(manual_flag.any()):
        lines += [
            "4. **开球前几分钟**在 Actions 页面跑 **record-close**，填那一刻的市场赔率"
            "（有 Pinnacle 用 Pinnacle）。",
            "   欧战和国家队没有收盘赔率源，不记就永远算不出 CLV，这些推荐也就无从检验。"
            "联赛不用管，收盘价会自动取。",
        ]
    lines += [
        "",
        "<details><summary>用终端的话</summary>",
        "",
        "```bash",
    ]
    for _, p in picks.iterrows():
        lines.append(f"python -m src.ledger add {p['pick_id']} --odds <Tipico赔率> "
                     f"--stake {p['stake']:.2f}")
    if bool(manual_flag.any()):
        lines.append("# 开球前：")
        for _, p in picks[manual_flag].iterrows():
            lines.append(f"python -m src.ledger close {p['pick_id']} "
                         f"--close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>")
    lines += ["```", "", "</details>", "",
              "「可得赔率」带 * 的是市场最高赔率（只说明这个价格在市场上存在，",
              "不一定在 Tipico）；不带 * 的是你自己填进来的 Tipico 赔率。", ""]
    return lines


def _combo_section(picks: pd.DataFrame, all_df: pd.DataFrame, cfg: dict) -> list[str]:
    """Minimum odds for same-match combinations on the matches already picked.

    No feed quotes combination odds, so these can never be checked against a
    real price here — the report gives the threshold and the user compares it
    in the app. They are listed only where the model sits above the market, and
    only for matches that already produced a pick, to keep the report short.
    """
    if not cfg["value"].get("combos") or all_df.empty or picks.empty:
        return []
    combos = all_df[all_df["market"] == "1X2+OU25"]
    if combos.empty:
        return []
    key = ["date", "home", "away"]
    combos = combos.merge(picks[key].drop_duplicates(), on=key, how="inner")
    combos = combos[combos["p_model"] > combos["p_market"]]
    if combos.empty:
        return []
    lines = [
        "## 同场组合参考（胜负 + 大小球）",
        "",
        "没有数据源报组合赔率，所以这些**不是推荐**，只是阈值：",
        "在 Tipico 的组合投注里找到对应选项，**赔率 ≥ 最低赔率才值得下**。",
        "注意组合的公平赔率不等于两个盘口相乘——平局和大球强烈负相关。",
        "",
        "| 比赛 | 组合 | 公平赔率 | **最低赔率** | 相乘会误算成 |",
        "|---|---|---|---|---|",
    ]
    for (_, _, _), g in combos.groupby(key, sort=False):
        g = g.sort_values("min_odds").head(cfg["value"].get("max_combo_rows", 4))
        for _, c in g.iterrows():
            naive = f"{c['naive_odds']:.2f}" if pd.notna(c.get("naive_odds")) else "—"
            lines.append(f"| {c['home']} vs {c['away']} | {c['label']} | "
                         f"{c['fair_odds']:.2f} | **{c['min_odds']:.2f}** | {naive} |")
    return lines + [""]


def render_report(today, picks: pd.DataFrame, all_df: pd.DataFrame,
                  notes: list[str], cfg: dict) -> str:
    v, s = cfg["value"], cfg["staking"]
    n_matches = 0 if all_df.empty else all_df[["date", "home", "away"]].drop_duplicates().shape[0]
    today = pd.Timestamp(today)
    # the horizon is more than one day, and on a Friday the Saturday card is
    # ten times the size — so the picks are usually not today's matches. Say
    # which days are covered instead of calling it "today's".
    last = today + pd.Timedelta(days=v["horizon_days"] - 1)
    window = f"{today:%m-%d}" if last == today else f"{today:%m-%d} 至 {last:%m-%d}"
    lines = [
        f"# 投注建议 · {today:%Y-%m-%d}",
        "",
        f"覆盖 {window} 开赛的比赛 · 本金 €{s['bankroll']:.0f} · "
        f"最低赔率 {v['min_odds']:.2f} · 最低优势 {v['min_edge']:.0%} · "
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
        lines += _id_section(picks)
        lines += _how_to_section(picks)
        lines += _combo_section(picks, all_df, cfg)
    if notes:
        lines += ["## 备注", *[f"- {n}" for n in notes], ""]
    lines += [
        "---",
        "开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。"
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
    ap.add_argument("--horizon", type=int,
                    help="只看未来几天开赛的比赛，覆盖 value.horizon_days。"
                         "填 1 就是只看当天——周五跑默认的 2 天时，周六的比赛量是"
                         "周五的十倍，会把当天的挤出推荐。")
    ap.add_argument("--out", help="报告写到这个目录，默认是 paths.reports")
    args = ap.parse_args()
    cfg = load_config(args.config)
    if args.horizon is not None:
        if args.horizon < 1:
            raise SystemExit("--horizon 至少是 1。")
        cfg["value"]["horizon_days"] = args.horizon
    if args.out:
        cfg["paths"]["reports"] = args.out
    run(cfg, today=args.date)


if __name__ == "__main__":
    main()
