"""Neutral-venue support and the analytic gradient it changed."""
import numpy as np
import pandas as pd
import pytest
from scipy.optimize import approx_fprime

import src.model as M
from src.model import DixonColes, _home_vector
from tests.synthetic import make_neutral_series


def test_home_vector():
    assert list(_home_vector(pd.DataFrame({"a": [1, 2]}))) == [1.0, 1.0]
    assert list(_home_vector(pd.DataFrame({"neutral": [True, False, None]}))) == [0.0, 1.0, 1.0]


def _capture_objective(df, ref, **kw):
    """Fit while grabbing the objective closure, so the gradient can be checked."""
    captured = {}
    real = M.minimize

    def spy(fun, p0, **kwargs):
        captured["f"], captured["p0"] = fun, p0
        return real(fun, p0, **kwargs)

    M.minimize = spy
    try:
        model = DixonColes(**kw).fit(df, ref)
    finally:
        M.minimize = real
    return model, captured["f"], captured["p0"]


@pytest.mark.parametrize("with_neutral", [True, False])
def test_analytic_gradient_matches_numeric(with_neutral):
    df, _ = make_neutral_series(n=400, seed=11)
    if not with_neutral:
        df = df.drop(columns=["neutral"])
    ref = pd.Timestamp("2026-01-01")
    _, f, p0 = _capture_objective(df, ref, xi=0.002)
    rng = np.random.default_rng(5)
    for _ in range(3):
        p = p0 + rng.normal(0, 0.25, len(p0))
        p[-1] = np.clip(p[-1], -0.1, 0.1)
        _, grad = f(p)
        num = approx_fprime(p, lambda q: f(q)[0], 1e-7)
        assert np.abs(grad - num).max() / max(1.0, np.abs(num).max()) < 1e-5


def test_recovers_home_advantage_only_from_home_games():
    df, truth = make_neutral_series(n=1600, seed=2, home_adv=0.30)
    m = DixonColes(xi=0.0005, ridge=1e-3).fit(df, pd.Timestamp("2030-01-01"))
    assert m.converged
    assert abs(m.home_adv - truth["home"]) < 0.12

    # a neutral match drops exactly the home term from lambda and leaves mu alone
    lam_h, mu_h = m.rates("N00", "N01", neutral=False)
    lam_n, mu_n = m.rates("N00", "N01", neutral=True)
    assert lam_n == pytest.approx(lam_h / np.exp(m.home_adv))
    assert mu_n == pytest.approx(mu_h)

    p_home = m.predict("N00", "N01", neutral=False)
    p_neutral = m.predict("N00", "N01", neutral=True)
    assert p_home["H"] > p_neutral["H"]
    assert sum(p_neutral[k] for k in "HDA") == pytest.approx(1.0)


def test_ignoring_neutral_flag_biases_home_advantage_down():
    """Why the flag exists: pooling neutral games as home games dilutes it."""
    df, truth = make_neutral_series(n=1600, seed=2, home_adv=0.30, neutral_share=0.6)
    ref = pd.Timestamp("2030-01-01")
    aware = DixonColes(xi=0.0005).fit(df, ref)
    naive = DixonColes(xi=0.0005).fit(df.drop(columns=["neutral"]), ref)
    assert abs(aware.home_adv - truth["home"]) < abs(naive.home_adv - truth["home"])
