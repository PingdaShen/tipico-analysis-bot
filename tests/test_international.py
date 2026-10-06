"""The national-team model and its data source contract."""
from datetime import date

import pandas as pd
import pytest

from src import intl
from src.config import load_config
from src.data import standardize_international
from tests.synthetic import make_neutral_series

RAW = pd.DataFrame({
    "date": ["2024-09-05", "2024-09-08", "2024-10-10", "bad-date"],
    "home_team": ["Germany", "Spain", "Brazil", "X"],
    "away_team": ["Hungary", "Switzerland", "Peru", "Y"],
    "home_score": [5, 4, 1, 0],
    "away_score": [0, 1, 0, 0],
    "tournament": ["UEFA Nations League", "UEFA Nations League", "Friendly", "Friendly"],
    "city": ["Düsseldorf", "Belgrade", "Brasilia", "?"],
    "country": ["Germany", "Serbia", "Brazil", "?"],
    "neutral": ["FALSE", "TRUE", "FALSE", "FALSE"],
})


def test_standardize_international():
    df = standardize_international(RAW)
    assert len(df) == 3                          # the unparseable date is dropped
    assert list(df.columns[:1]) == ["date"] or "date" in df.columns
    assert set(df["div"]) == {"INT"}
    assert df["neutral"].tolist() == [False, True, False]
    assert df["hg"].dtype.kind == "i" and df["ag"].dtype.kind == "i"
    assert df["date"].is_monotonic_increasing


def test_load_filters_by_window_and_tournament():
    cfg = load_config()
    seen = {}

    def loader(cache, since=None, tournaments=None, fresh=False):
        seen.update(since=since, tournaments=tournaments)
        return standardize_international(RAW)

    intl.load(cfg, "cache", today="2026-10-06", loader=loader)
    assert seen["since"] == intl.window_start(cfg, "2026-10-06")
    assert "UEFA Nations League" in seen["tournaments"]
    # friendlies are deliberately excluded: lineups make them poor evidence
    assert "Friendly" not in seen["tournaments"]


def test_window_start_uses_configured_years():
    cfg = load_config()
    start = intl.window_start(cfg, "2026-10-06")
    years = cfg["international"]["history_years"]
    assert start < date(2026, 10, 6)
    assert abs((date(2026, 10, 6) - start).days - 365 * years) <= 1


def test_fit_uses_international_params_and_neutral_flag():
    cfg = load_config()
    df, truth = make_neutral_series(n=1200, seed=4, home_adv=0.28)
    m = intl.fit(df, cfg, pd.Timestamp("2030-01-01"))
    assert m.xi == cfg["international"]["xi"]
    assert m.ridge == cfg["international"]["ridge"]
    assert m.min_team_matches == cfg["international"]["min_team_matches"]
    assert abs(m.home_adv - truth["home"]) < 0.15
    # the neutral flag reached the fit, so a neutral tie is closer than a home one
    assert m.predict("N00", "N01")["H"] > m.predict("N00", "N01", neutral=True)["H"]


def test_configured_tournament_names_are_non_empty_strings():
    """A misspelt name is silently ignored by the filter, so guard the shape."""
    names = load_config()["international"]["tournaments"]
    assert names and all(isinstance(n, str) and n.strip() for n in names)
    assert len(set(names)) == len(names)
