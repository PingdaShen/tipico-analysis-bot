"""Dixon-Coles football model with exponential time decay.

log(lambda_home) = home * hv + attack[h] + defence[a]
log(mu_away)     = attack[a] + defence[h]
plus the Dixon-Coles low-score correction tau(x, y; rho).

hv is 1 for a normal home game and 0 when the match is played at a neutral
venue (international tournaments, European finals). Matches carry it in an
optional boolean "neutral" column; without that column everything is a home
game, which is how the domestic league models behave.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import poisson


def _tau_terms(x, y, lam, mu, rho):
    """tau and its derivatives w.r.t. log(lam), log(mu), rho."""
    tau = np.ones_like(lam)
    d_l = np.zeros_like(lam)
    d_m = np.zeros_like(lam)
    d_r = np.zeros_like(lam)

    m = (x == 0) & (y == 0)
    tau[m] = 1 - lam[m] * mu[m] * rho
    d_l[m] = -lam[m] * mu[m] * rho
    d_m[m] = -lam[m] * mu[m] * rho
    d_r[m] = -lam[m] * mu[m]

    m = (x == 0) & (y == 1)
    tau[m] = 1 + lam[m] * rho
    d_l[m] = lam[m] * rho
    d_r[m] = lam[m]

    m = (x == 1) & (y == 0)
    tau[m] = 1 + mu[m] * rho
    d_m[m] = mu[m] * rho
    d_r[m] = mu[m]

    m = (x == 1) & (y == 1)
    tau[m] = 1 - rho
    d_r[m] = -1.0

    return np.maximum(tau, 1e-10), d_l, d_m, d_r


def _home_vector(df: pd.DataFrame) -> np.ndarray:
    """1 for a real home game, 0 at a neutral venue."""
    if "neutral" not in df.columns:
        return np.ones(len(df))
    return 1.0 - df["neutral"].fillna(False).astype(bool).to_numpy(dtype=float)


class DixonColes:
    def __init__(self, xi: float = 0.0019, ridge: float = 1e-3,
                 max_goals: int = 10, min_team_matches: int = 8):
        self.xi = xi
        self.ridge = ridge
        self.max_goals = max_goals
        self.min_team_matches = min_team_matches
        self.teams: dict[str, int] = {}
        self.counts: dict[str, int] = {}

    def fit(self, matches: pd.DataFrame, ref_date) -> "DixonColes":
        """Fit on matches strictly before ref_date (no look-ahead)."""
        ref_date = pd.Timestamp(ref_date)
        df = matches[matches["date"] < ref_date]
        if len(df) < 30:
            raise ValueError(f"not enough matches to fit ({len(df)})")

        names = sorted(set(df["home"]) | set(df["away"]))
        self.teams = {t: i for i, t in enumerate(names)}
        n = len(names)
        h = df["home"].map(self.teams).to_numpy()
        a = df["away"].map(self.teams).to_numpy()
        x = df["hg"].to_numpy(dtype=float)
        y = df["ag"].to_numpy(dtype=float)
        w = np.exp(-self.xi * (ref_date - df["date"]).dt.days.to_numpy(dtype=float))
        hv = _home_vector(df)
        self.counts = pd.concat([df["home"], df["away"]]).value_counts().to_dict()
        ridge = self.ridge

        def objective(p):
            att = p[:n] - p[:n].mean()
            dfn = p[n:2 * n]
            home, rho = p[2 * n], p[2 * n + 1]
            log_l = home * hv + att[h] + dfn[a]
            log_m = att[a] + dfn[h]
            lam, mu = np.exp(log_l), np.exp(log_m)
            tau, d_l, d_m, d_r = _tau_terms(x, y, lam, mu, rho)

            ll = w * (np.log(tau) + x * log_l - lam + y * log_m - mu)
            g_l = w * (x - lam + d_l / tau)
            g_m = w * (y - mu + d_m / tau)

            g_att = np.bincount(h, g_l, n) + np.bincount(a, g_m, n)
            g_att = g_att - g_att.mean()
            g_def = np.bincount(a, g_l, n) + np.bincount(h, g_m, n)

            f = -ll.sum() + ridge * (att @ att + dfn @ dfn)
            grad = -np.concatenate([g_att, g_def,
                                    [float(g_l @ hv), np.sum(w * d_r / tau)]])
            grad[:n] += 2 * ridge * att
            grad[n:2 * n] += 2 * ridge * dfn
            return f, grad

        p0 = np.concatenate([np.zeros(2 * n), [0.25, 0.0]])
        bounds = [(None, None)] * (2 * n + 1) + [(-0.15, 0.15)]
        res = minimize(objective, p0, jac=True, method="L-BFGS-B", bounds=bounds)
        p = res.x
        self.attack = p[:n] - p[:n].mean()
        self.defence = p[n:2 * n]
        self.home_adv = p[2 * n]
        self.rho = p[2 * n + 1]
        self.converged = bool(res.success)
        return self

    def has_team(self, team: str) -> bool:
        return team in self.teams and self.counts.get(team, 0) >= self.min_team_matches

    def rates(self, home: str, away: str, neutral: bool = False) -> tuple[float, float]:
        i, j = self.teams[home], self.teams[away]
        lam = np.exp((0.0 if neutral else self.home_adv) + self.attack[i] + self.defence[j])
        mu = np.exp(self.attack[j] + self.defence[i])
        return float(lam), float(mu)

    def predict(self, home: str, away: str, neutral: bool = False) -> dict | None:
        """Outcome probabilities, or None if either team lacks data."""
        if not (self.has_team(home) and self.has_team(away)):
            return None
        lam, mu = self.rates(home, away, neutral)
        g = np.arange(self.max_goals + 1)
        mat = np.outer(poisson.pmf(g, lam), poisson.pmf(g, mu))
        mat[0, 0] *= 1 - lam * mu * self.rho
        mat[0, 1] *= 1 + lam * self.rho
        mat[1, 0] *= 1 + mu * self.rho
        mat[1, 1] *= 1 - self.rho
        mat = np.clip(mat, 0, None)
        mat /= mat.sum()
        total = g[:, None] + g[None, :]
        over = float(mat[total >= 3].sum())
        return {
            "H": float(np.tril(mat, -1).sum()),
            "D": float(np.trace(mat)),
            "A": float(np.triu(mat, 1).sum()),
            "O25": over,
            "U25": 1.0 - over,
            "lam": lam,
            "mu": mu,
        }
