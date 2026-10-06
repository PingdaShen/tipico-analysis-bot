"""Synthetic league in football-data.co.uk CSV format, for offline tests."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import poisson

from src.data import standardize


def _true_probs(lam, mu, max_goals=10):
    g = np.arange(max_goals + 1)
    mat = np.outer(poisson.pmf(g, lam), poisson.pmf(g, mu))
    mat /= mat.sum()
    tot = g[:, None] + g[None, :]
    return (np.tril(mat, -1).sum(), np.trace(mat), np.triu(mat, 1).sum(), mat[tot >= 3].sum())


def _odds(p, margin, rng, noise):
    return round(float(1 / (p * (1 + margin) * np.exp(rng.normal(0, noise)))), 2)


def make_league(div="X1", n_teams=12, seasons=3, start="2023-08-05", seed=0,
                future_days=2, today=None):
    rng = np.random.default_rng(seed)
    teams = [f"Team{i:02d}" for i in range(n_teams)]
    att = rng.normal(0, 0.3, n_teams)
    att -= att.mean()
    dfn = rng.normal(0, 0.2, n_teams)
    home = 0.25
    rows = []
    t0 = pd.Timestamp(start)
    per_round = n_teams // 2

    def row(i, j, date, played):
        lam = np.exp(home + att[i] + dfn[j])
        mu = np.exp(att[j] + dfn[i])
        pH, pD, pA, pO = _true_probs(lam, mu)
        pU = 1 - pO
        r = {"Div": div, "Date": date.strftime("%d/%m/%Y"), "Time": "15:30",
             "HomeTeam": teams[i], "AwayTeam": teams[j]}
        for prefix, margin, noise in (("PS", 0.025, 0.02), ("PSC", 0.02, 0.01),
                                      ("Avg", 0.05, 0.02), ("B365", 0.05, 0.04)):
            for k, p in zip("HDA", (pH, pD, pA)):
                r[f"{prefix}{k}"] = _odds(p, margin, rng, noise)
        for k, p in zip("HDA", (pH, pD, pA)):
            r[f"Max{k}"] = _odds(p, -0.04, rng, 0.02)
        for name, margin, noise in (("P", 0.025, 0.02), ("PC", 0.02, 0.01), ("Avg", 0.05, 0.02),
                                    ("Max", -0.04, 0.02), ("B365", 0.05, 0.04)):
            r[f"{name}>2.5"] = _odds(pO, margin, rng, noise)
            r[f"{name}<2.5"] = _odds(pU, margin, rng, noise)
        if played:
            r["FTHG"], r["FTAG"] = int(rng.poisson(lam)), int(rng.poisson(mu))
        return r

    for s in range(seasons):
        pairs = [(i, j) for i in range(n_teams) for j in range(n_teams) if i != j]
        rng.shuffle(pairs)
        for k, (i, j) in enumerate(pairs):
            date = t0 + pd.Timedelta(days=s * 365 + (k // per_round) * 4)
            rows.append(row(i, j, date, played=True))

    hist = pd.DataFrame(rows)
    today = pd.Timestamp(today) if today is not None else t0 + pd.Timedelta(days=seasons * 365)
    fixtures = pd.DataFrame([row(i, (i + 1) % n_teams, today + pd.Timedelta(days=k % future_days),
                                 played=False) for k, i in enumerate(range(0, n_teams, 2))])
    truth = {"teams": teams, "att": att, "def": dfn, "home": home}
    return hist, fixtures, today, truth


def loaders(hist_raw: pd.DataFrame, fix_raw: pd.DataFrame):
    hist = standardize(hist_raw)
    hist["hg"] = hist["hg"].astype(int)
    hist["ag"] = hist["ag"].astype(int)
    fix = standardize(fix_raw)

    def history_loader(div, seasons, cache_dir, today=None, fresh=False):
        h = hist[hist["div"] == div]
        if today is not None and not fresh:
            h = h[h["date"] < pd.Timestamp(today)]
        return h.sort_values("date").reset_index(drop=True)

    def fixtures_loader(divs, cache_dir):
        return fix[fix["div"].isin(divs)].reset_index(drop=True)

    return history_loader, fixtures_loader


# ---------------------------------------------------------------------------
# A synthetic multi-league world, for the cross-league (pooled) model.
#
# Every team's true strength lives on ONE scale, and the leagues differ in
# average strength. That is what makes the test meaningful: fitting each
# league on its own centres its attack values at zero and throws the league
# difference away, so per-league ratings cannot be compared. Only the cup
# matches between leagues make the single scale recoverable.
# ---------------------------------------------------------------------------

def make_world(league_strength=(0.45, 0.0, -0.45), n_teams=10, seasons=3,
               cup_rounds=6, start="2023-08-05", seed=7, today=None):
    rng = np.random.default_rng(seed)
    divs = [f"L{i}" for i in range(len(league_strength))]
    teams, att, dfn, team_div = [], [], [], {}
    for div, boost in zip(divs, league_strength):
        for k in range(n_teams):
            name = f"{div}T{k:02d}"
            teams.append(name)
            att.append(boost + rng.normal(0, 0.25))
            dfn.append(-boost + rng.normal(0, 0.2))
            team_div[name] = div
    att = np.array(att)
    dfn = np.array(dfn)
    home = 0.26
    idx = {t: i for i, t in enumerate(teams)}
    t0 = pd.Timestamp(start)

    def play(h, a, when, neutral=False):
        lam = np.exp((0.0 if neutral else home) + att[idx[h]] + dfn[idx[a]])
        mu = np.exp(att[idx[a]] + dfn[idx[h]])
        return {"date": pd.Timestamp(when), "home": h, "away": a,
                "hg": int(rng.poisson(lam)), "ag": int(rng.poisson(mu)),
                "neutral": neutral}

    domestic = []
    for div in divs:
        names = [t for t in teams if team_div[t] == div]
        for s in range(seasons):
            pairs = [(i, j) for i in names for j in names if i != j]
            rng.shuffle(pairs)
            for k, (i, j) in enumerate(pairs):
                r = play(i, j, t0 + pd.Timedelta(days=s * 365 + (k // (n_teams // 2)) * 4))
                domestic.append({**r, "div": div, "neutral": False})

    # cup: only matches between different leagues, i.e. the links
    cup = []
    for s in range(seasons):
        for r in range(cup_rounds):
            for di, dj in [(0, 1), (1, 2), (0, 2)]:
                if dj >= len(divs):
                    continue
                h = str(rng.choice([t for t in teams if team_div[t] == divs[di]]))
                a = str(rng.choice([t for t in teams if team_div[t] == divs[dj]]))
                when = t0 + pd.Timedelta(days=s * 365 + 30 + r * 30)
                cup.append({**play(h, a, when), "div": "CUP"})
                cup.append({**play(a, h, when + pd.Timedelta(days=7)), "div": "CUP"})

    today = pd.Timestamp(today) if today is not None else t0 + pd.Timedelta(days=seasons * 365)
    truth = {"teams": teams, "att": att, "def": dfn, "home": home, "div": team_div,
             "divs": divs, "strength": dict(zip(divs, league_strength))}
    cols = ["div", "date", "home", "away", "hg", "ag", "neutral"]
    # columns= keeps the frame usable when a list is empty (one league, or
    # cup_rounds=0), where DataFrame(list) alone would have no columns at all
    return (pd.DataFrame(domestic, columns=cols), pd.DataFrame(cup, columns=cols),
            today, truth)


def make_neutral_series(n=900, seed=3, home_adv=0.3, neutral_share=0.4, n_teams=16):
    """Matches where neutral-venue games genuinely have no home advantage."""
    rng = np.random.default_rng(seed)
    teams = [f"N{i:02d}" for i in range(n_teams)]
    att = rng.normal(0, 0.3, n_teams)
    att -= att.mean()
    dfn = rng.normal(0, 0.2, n_teams)
    rows = []
    for k in range(n):
        i, j = rng.choice(n_teams, 2, replace=False)
        neutral = bool(rng.random() < neutral_share)
        lam = np.exp((0.0 if neutral else home_adv) + att[i] + dfn[j])
        mu = np.exp(att[j] + dfn[i])
        rows.append({"div": "INT", "date": pd.Timestamp("2018-01-01") + pd.Timedelta(days=3 * k),
                     "home": teams[i], "away": teams[j], "hg": int(rng.poisson(lam)),
                     "ag": int(rng.poisson(mu)), "neutral": neutral})
    truth = {"teams": teams, "att": att, "def": dfn, "home": home_adv}
    return pd.DataFrame(rows), truth
