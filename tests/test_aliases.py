"""UEFA team-name resolution."""
import pandas as pd
import pytest
import yaml

from src.aliases import (ALIAS_FILE, build_index, load_table, normalize,
                         resolve_names, suggest, suggest_aliases, uefa_name_countries)
from src.config import ROOT, load_config

UNIVERSE = {
    "E0": ["Arsenal", "Man City", "Tottenham"],
    "SP1": ["Ath Madrid", "Barcelona", "Real Madrid"],
    "D1": ["Bayern Munich", "Dortmund"],
}


@pytest.mark.parametrize("raw,expected", [
    ("Club Atlético de Madrid", "atletico madrid"),
    ("FC Bayern München", "bayern munchen"),
    ("1. FSV Mainz 05", "fsv mainz"),
    ("FK Bodø/Glimt", "bodo glimt"),
    ("Brøndby IF", "brondby"),
])
def test_normalize(raw, expected):
    assert normalize(raw) == expected


def test_normalize_keeps_distinguishing_words():
    """Stripping "sporting" or "real" would merge genuinely different clubs."""
    assert normalize("Sporting CP") != normalize("Sporting Braga")
    assert normalize("Real Madrid") != normalize("Real Betis")


def test_build_index_is_grouped_by_country():
    cfg = load_config()
    index = build_index(UNIVERSE, cfg)
    assert set(index) == {"ENG", "ESP", "GER"}
    assert index["ESP"][normalize("Barcelona")] == "Barcelona"


def test_suggest_stays_inside_the_country():
    cfg = load_config()
    index = build_index(UNIVERSE, cfg)
    assert suggest("FC Barcelona", "ESP", index)[0] == "Barcelona"
    # the same name offered under the wrong country must not match
    assert suggest("FC Barcelona", "GER", index)[0] is None
    assert suggest("Totally Unknown Club", "ENG", index)[0] is None


def test_resolve_names_renames_and_reports():
    df = pd.DataFrame({"home": ["FC Barcelona", "Unknown FC"],
                       "away": ["Real Madrid CF", "FC Barcelona"]})
    table = {"FC Barcelona": "Barcelona", "Real Madrid CF": "Real Madrid"}
    out, unresolved = resolve_names(df, table)
    assert out["home"].tolist() == ["Barcelona", "Unknown FC"]
    assert out["away"].tolist() == ["Real Madrid", "Barcelona"]
    assert unresolved == ["Unknown FC"]


def test_resolve_names_keeps_teams_mapped_to_nothing():
    """An empty value means 'no domestic team'; keep it as its own node."""
    df = pd.DataFrame({"home": ["Shakhtar Donetsk"], "away": ["FC Barcelona"]})
    out, _ = resolve_names(df, {"Shakhtar Donetsk": "", "FC Barcelona": "Barcelona"})
    assert out["home"].tolist() == ["Shakhtar Donetsk"]


def test_suggest_aliases_skips_covered_names():
    cfg = load_config()
    uefa = pd.DataFrame({
        "home": ["FC Barcelona", "FC Bayern München"], "away": ["Arsenal FC", "Arsenal FC"],
        "home_country": ["ESP", "GER"], "away_country": ["ENG", "ENG"],
    })
    out = suggest_aliases(uefa, UNIVERSE, cfg, table={"FC Barcelona": "Barcelona"})
    assert "FC Barcelona" not in set(out["uefa_name"])
    assert set(out["uefa_name"]) == {"FC Bayern München", "Arsenal FC"}
    assert out["has_domestic_data"].all()


def test_uefa_name_countries():
    uefa = pd.DataFrame({"home": ["A"], "away": ["B"],
                         "home_country": ["ENG"], "away_country": ["GER"]})
    assert uefa_name_countries(uefa) == {"A": "ENG", "B": "GER"}


# --- the shipped table itself -------------------------------------------------

def test_shipped_alias_table_parses():
    table = load_table(ROOT)
    assert len(table) > 100, "别名表看起来不完整"
    assert all(isinstance(k, str) and k.strip() for k in table)


def test_shipped_alias_table_has_no_self_referential_chains():
    """A value must not itself be a key, or resolution would depend on order."""
    table = load_table(ROOT)
    targets = {v for v in table.values() if v}
    chained = {t for t in targets if t in table and table[t] != t}
    assert not chained, f"这些目标名又是别名表的键，解析结果会依赖顺序：{sorted(chained)}"


def test_config_div_country_covers_every_division():
    cfg = load_config()
    expected = set(cfg["leagues"]) | set(cfg["extra_countries"])
    assert set(cfg["div_country"]) == expected
