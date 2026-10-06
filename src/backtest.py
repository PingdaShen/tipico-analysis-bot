"""Walk-forward backtest on completed seasons.

Tipico odds are not in the data, so Bet365 pre-match odds act as a soft-book proxy.
Each week the model is refit on data strictly before that week (no look-ahead).

Usage: python -m src.backtest [--seasons 2] [--leagues E0 D1] [--model-weight 0.3]
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import pandas as pd

from .config import ROOT, load_config
from .daily import fit_model
from .data import current_season_start, load_history, season_code
from .market import OUTCOMES, SOFT_PRE, closing_odds, market_probs, odds_dict, outcome_won
from .value import blend


def backtest_league(history: pd.DataFrame, cfg: dict, test_start: pd.Timestamp,
                    refit_days: int = 7) -> list[dict]:
    v, w = cfg["value"], cfg["blend"]["model_weight"]
    window = pd.Timedelta(days=365 * cfg["history_seasons"])
    test = history[history["date"] >= test_start]
    bets = []
    ref = test_start
    while ref <= test["date"].max():
        week = test[(test["date"] >= ref) & (test["date"] < ref + pd.Timedelta(days=refit_days))]
        if not week.empty:
            train = history[(history["date"] < ref) & (history["date"] >= ref - window)]
            try:
                model = fit_model(train, cfg, ref)
            except ValueError:
                ref += pd.Timedelta(days=refit_days)
                continue
            for _, g in week.iterrows():
                p_model = model.predict(g["home"], g["away"])
                if p_model is None:
                    continue
                for market in v["markets"]:
                    p_mkt, _ = market_probs(g, market)
                    soft = odds_dict(g, SOFT_PRE, market)
                    if p_mkt is None or soft is None:
                        continue
                    p_final = blend(p_model, p_mkt, w)
                    for o in OUTCOMES[market]:
                        odds = soft[o]
                        if not (v["min_odds"] <= odds <= v["max_odds"]):
                            continue
                        if p_model[o] <= p_mkt[o] or p_final[o] * odds < 1 + v["min_edge"]:
                            continue
                        won = outcome_won(o, int(g["hg"]), int(g["ag"]))
                        close, close_source = closing_odds(g, market, o)
                        bets.append({
                            "date": g["date"], "div": g["div"], "home": g["home"],
                            "away": g["away"], "market": market, "outcome": o,
                            "odds": odds, "p_final": p_final[o], "won": won,
                            "pnl": odds - 1 if won else -1.0,
                            "clv": odds / close - 1 if close else None,
                            "close_source": close_source,
                        })
        ref += pd.Timedelta(days=refit_days)
    return bets


def _sharp_clv(s: pd.DataFrame) -> float:
    """Average CLV counting only bets priced against Pinnacle's closing line."""
    sharp = s.loc[s["close_source"] == "pinnacle", "clv"].dropna()
    return float(sharp.mean()) if not sharp.empty else float("nan")


def _sharp_n(s: pd.DataFrame) -> int:
    return int((s["close_source"] == "pinnacle").sum())


def summarize(bets: pd.DataFrame) -> pd.DataFrame:
    """Per-league and overall summary.

    sharp_clv is the number to look at: avg_clv mixes Pinnacle's closing line
    with the much softer market average, which flatters it badly. See
    market.closing_odds.
    """
    if bets.empty:
        return pd.DataFrame()
    if "close_source" not in bets.columns:
        bets = bets.assign(close_source=None)
    rows = {}
    for div, s in bets.groupby("div"):
        rows[div] = {"bets": len(s), "pnl": s["pnl"].sum(), "hit_rate": s["won"].mean(),
                     "avg_clv": s["clv"].mean(), "sharp_n": _sharp_n(s),
                     "sharp_clv": _sharp_clv(s)}
    rows["ALL"] = {"bets": len(bets), "pnl": bets["pnl"].sum(),
                   "hit_rate": bets["won"].mean(), "avg_clv": bets["clv"].mean(),
                   "sharp_n": _sharp_n(bets), "sharp_clv": _sharp_clv(bets)}
    out = pd.DataFrame.from_dict(rows, orient="index")
    out["roi"] = out["pnl"] / out["bets"]
    return out


def run(cfg: dict, n_test_seasons: int = 2, leagues: list[str] | None = None,
        history_loader=load_history, root: Path = ROOT, today=None) -> pd.DataFrame:
    today = today or date.today()
    last_complete = current_season_start(today) - 1
    first_test = last_complete - n_test_seasons + 1
    seasons = [season_code(y) for y in range(first_test - cfg["history_seasons"], last_complete + 1)]
    test_start = pd.Timestamp(f"{first_test}-07-01")
    cache = Path(root) / cfg["paths"]["cache"]

    all_bets = []
    for div in leagues or list(cfg["leagues"]):
        hist = history_loader(div, seasons, cache, today=today)
        if hist.empty:
            print(f"[warn] {div}: no data")
            continue
        all_bets += backtest_league(hist, cfg, test_start)
        print(f"{div}: done")
    bets = pd.DataFrame(all_bets)
    out_dir = Path(root) / cfg["paths"]["reports"]
    out_dir.mkdir(parents=True, exist_ok=True)
    if not bets.empty:
        bets.to_csv(out_dir / "backtest_bets.csv", index=False)
    summary = summarize(bets)
    print(summary.to_string(float_format=lambda x: f"{x:.3f}") if not summary.empty else "没有产生任何投注")
    return summary


def main() -> None:
    ap = argparse.ArgumentParser(description="Walk-forward backtest")
    ap.add_argument("--seasons", type=int, default=2, help="number of completed seasons to test")
    ap.add_argument("--leagues", nargs="*", help="league codes, e.g. E0 D1")
    ap.add_argument("--model-weight", type=float, help="override blend.model_weight")
    args = ap.parse_args()
    cfg = load_config()
    if args.model_weight is not None:
        cfg["blend"]["model_weight"] = args.model_weight
    run(cfg, args.seasons, args.leagues)


if __name__ == "__main__":
    main()
