"""Shared test setup.

The suite must behave the same whether or not the developer happens to have
an API key in their shell — otherwise `pytest` quietly starts making real
requests and the results depend on who runs it.
"""
import pytest

from src import oddsapi


@pytest.fixture(autouse=True)
def no_ambient_api_key(monkeypatch):
    """Hide any real ODDS_API_KEY; a test that needs one sets it explicitly."""
    monkeypatch.delenv(oddsapi.KEY_ENV, raising=False)
