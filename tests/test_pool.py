"""The cross-league pooled model.

The point of pooling is identification: per-league fits cannot be compared to
each other, and the cup matches are what fixes that. These tests assert that
property directly rather than just checking the code runs.
"""
import numpy as np
import pandas as pd
import pytest

from src.config import load_config
from src.model import DixonColes
from src.pool import POOL_COLUMNS, fit_pool, load_pool, pool_seasons
from tests.synthetic import make_world


@pytest.fixture(scope="module")
def world():
    return make_world(seasons=4, cup_rounds=8)


def _rating(model, teams):
    return np.array([model.attack[model.teams[t]] - model.defence[model.teams[t]]
                     for t in teams])


def test_per_league_fits_cannot_be_compared_across_leagues(world):
    """Each league fit is centred on itself, so the league gap disappears."""
    domestic, _, today, truth = world
    teams, order = [], []
    for div in truth["divs"]:
        d = domestic[domestic["div"] == div]
        m = DixonColes(xi=0.001, ridge=1e-3).fit(d, today)
        names = sorted(set(d["home"]) | set(d["away"]))
        teams += names
        order.append(_rating(m, names))
    separate = np.concatenate(order)
    true = np.array([truth["att"][truth["teams"].index(t)]
                     - truth["def"][truth["teams"].index(t)] for t in teams])
    # within a league the fit is fine, across leagues the ordering is lost
    within = np.mean([np.corrcoef(order[i], true[i * 10:(i + 1) * 10])[0, 1]
                      for i in range(len(truth["divs"]))])
    assert within > 0.8
    assert np.corrcoef(separate, true)[0, 1] < 0.6


def test_pooled_fit_recovers_one_cross_league_scale(world):
    """With the cup links, every team lands on a single comparable scale."""
    domestic, cup, today, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    m = DixonColes(xi=0.001, ridge=1e-3, min_team_matches=5).fit(pool, today)
    teams = truth["teams"]
    true = np.array([truth["att"][i] - truth["def"][i] for i in range(len(teams))])
    assert np.corrcoef(_rating(m, teams), true)[0, 1] > 0.85

    # and the league averages come out in the right order
    means = {div: _rating(m, [t for t in teams if truth["div"][t] == div]).mean()
             for div in truth["divs"]}
    assert means["L0"] > means["L1"] > means["L2"]


def test_pooling_without_links_does_not_help(world):
    """Sanity check on the claim: drop the cup matches and the scale is gone."""
    domestic, _, today, truth = world
    m = DixonColes(xi=0.001, ridge=1e-3, min_team_matches=5).fit(domestic, today)
    teams = truth["teams"]
    true = np.array([truth["att"][i] - truth["def"][i] for i in range(len(teams))])
    assert np.corrcoef(_rating(m, teams), true)[0, 1] < 0.6


def test_fit_pool_uses_the_uefa_ridge():
    cfg = load_config()
    assert cfg["uefa"]["ridge"] != cfg["model"]["ridge"], "合并模型应当有自己的 ridge"
    domestic, cup, today, _ = make_world(seasons=2, cup_rounds=4)
    m = fit_pool(pd.concat([domestic, cup], ignore_index=True), cfg, today)
    assert m.ridge == cfg["uefa"]["ridge"]
    assert m.xi == cfg["uefa"]["xi"]
    assert m.min_team_matches == cfg["uefa"]["min_team_matches"]


def test_pool_seasons_window():
    cfg = load_config()
    years = pool_seasons(cfg, "2026-10-06")
    assert len(years) == cfg["uefa"]["history_seasons"]
    assert years[-1] == 2026
    assert pool_seasons(cfg, "2026-03-01")[-1] == 2025     # before July = prior season


def test_load_pool_offline_resolves_names_and_reports(tmp_path):
    """Injected loaders only: no network, and the alias report is populated."""
    cfg = load_config()
    # the window has to reach back far enough to cover the synthetic dates:
    # extra countries are trimmed to it, because the real new/ files carry
    # every season back to 2012
    cfg = {**cfg, "leagues": {"E0": "x"}, "extra_countries": {"AUT": "y"},
           "uefa": {**cfg["uefa"], "history_seasons": 2}}
    domestic, cup, today, _ = make_world(league_strength=(0.3, -0.3), n_teams=8,
                                         seasons=1, cup_rounds=3)
    e0 = domestic[domestic["div"] == "L0"].assign(div="E0")
    aut = domestic[domestic["div"] == "L1"].assign(div="AUT")

    def history_loader(div, seasons, cache, today=None, fresh=False):
        return e0 if div == "E0" else e0.iloc[0:0]

    def extra_loader(country, cache, today=None, fresh=False):
        return aut

    # rename one team that actually appears in the cup, the way a real
    # openfootball name differs from the football-data one
    renamed = sorted(set(cup["home"]) | set(cup["away"]))[0]
    cup = cup.assign(home=cup["home"].replace({renamed: "Wien FC"}),
                     away=cup["away"].replace({renamed: "Wien FC"}))

    def uefa_loader(seasons, cache, **kw):
        return cup.assign(div="CL", home_country="ENG", away_country="AUT", stage="League")

    pool, info = load_pool(cfg, tmp_path, today=today, root=tmp_path,
                           history_loader=history_loader, extra_loader=extra_loader,
                           uefa_loader=uefa_loader)
    assert list(pool.columns) == POOL_COLUMNS
    assert info["domestic"] == len(e0) + len(aut)
    assert info["uefa"] == len(cup)
    assert info["linked_teams"] > 0
    # no alias file in tmp_path, so the renamed team stays unresolved and is
    # kept as its own node rather than silently merged into another club
    assert "Wien FC" in info["unresolved"]
    assert "Wien FC" in set(pool["home"]) | set(pool["away"])


def test_load_pool_without_uefa_data_returns_domestic_only(tmp_path):
    cfg = load_config()
    cfg = {**cfg, "leagues": {"E0": "x"}, "extra_countries": {},
           "uefa": {**cfg["uefa"], "history_seasons": 1}}
    domestic, _, today, _ = make_world(league_strength=(0.0,), n_teams=8, seasons=1,
                                       cup_rounds=0)
    e0 = domestic.assign(div="E0")
    pool, info = load_pool(cfg, tmp_path, today=today, root=tmp_path,
                           history_loader=lambda *a, **k: e0,
                           extra_loader=lambda *a, **k: e0.iloc[0:0],
                           uefa_loader=lambda *a, **k: pd.DataFrame())
    assert info["uefa"] == 0
    assert len(pool) == len(e0)
