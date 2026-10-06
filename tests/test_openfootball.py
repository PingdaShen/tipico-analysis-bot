"""Parsing the openfootball UEFA text files."""
import pandas as pd
import pytest

from src.openfootball import (load_uefa_history, ninety_minute_score, parse,
                              season_dir, split_team)

SAMPLE = """= UEFA Champions League 2025/26

# Date       Tue Sep 16 2025 - Sat May 30 2026 (256d)
# Teams      36
# Matches    189


▪ League, Matchday 1
  Tue Sep 16 2025
    18:45  BSC Young Boys (SUI)    v Aston Villa FC (ENG)     0-3 (0-2)
           Juventus FC (ITA)       v PSV (NED)                3-1 (2-0)
  Wed Sep 17
    21:00  Real Madrid CF (ESP)    v VfB Stuttgart (GER)      3-1 (0-0)


▪ Playoffs, Matchday 2
  Thu Jul 17 2026
    19:00  NK Celje (SVN)          v Sabah FK (AZE)           3-3 a.e.t. (2-3, 1-1)
    20:00  Partizan (SRB)          v AEK Larnaca (CYP)        5-6 pen. 2-1 a.e.t. (1-0, 0-0)


▪ Finals, Final
  Sat May 30 2026
    18:00  Paris Saint-Germain FC (FRA) v Arsenal FC (ENG)    4-3 pen. 1-1 a.e.t. (1-1, 0-1)
"""


def test_season_dir():
    assert season_dir(2025) == "2025-26"
    assert season_dir(2099) == "2099-00"


def test_split_team():
    assert split_team("FC Bayern München (GER)") == ("FC Bayern München", "GER")
    assert split_team("Some Club") == ("Some Club", "")


@pytest.mark.parametrize("raw,expected", [
    ("2-3 (2-1)", (2, 3)),            # plain result, bracket is half time
    ("0-0", (0, 0)),
    ("9-2 (3-0)", (9, 2)),
    ("3-3 a.e.t. (2-3, 1-1)", (2, 3)),      # bracket is (90 minutes, half time)
    ("5-6 pen. 2-1 a.e.t. (1-0, 0-0)", (1, 0)),
    ("4-2 pen. 1-1", (1, 1)),               # shootout first, 90' result after
    ("v", None),
])
def test_ninety_minute_score(raw, expected):
    assert ninety_minute_score(raw) == expected


def test_parse_sample():
    df = parse(SAMPLE, "CL")
    assert len(df) == 6
    assert list(df.columns[:7]) == ["div", "date", "home", "away", "hg", "ag", "neutral"]

    first = df.iloc[0]
    assert (first["home"], first["away"]) == ("BSC Young Boys", "Aston Villa FC")
    assert (first["hg"], first["ag"]) == (0, 3)
    assert first["date"] == pd.Timestamp("2025-09-16")
    assert first["home_country"] == "SUI" and first["away_country"] == "ENG"

    # the year carries over to a date line that omits it
    assert df.iloc[2]["date"] == pd.Timestamp("2025-09-17")

    # extra time and penalties are stripped back to the 90-minute score
    celje = df[df["home"] == "NK Celje"].iloc[0]
    assert (celje["hg"], celje["ag"]) == (2, 3)
    partizan = df[df["home"] == "Partizan"].iloc[0]
    assert (partizan["hg"], partizan["ag"]) == (1, 0)

    # only the one-off final counts as a neutral venue
    assert df["neutral"].sum() == 1
    final = df[df["neutral"]].iloc[0]
    assert final["stage"] == "Finals, Final" and (final["hg"], final["ag"]) == (1, 1)


def test_parse_skips_headers_and_unplayed():
    df = parse("= Title\n# Date  Tue Sep 16 2025 - x\n▪ League\n  Tue Sep 16 2025\n"
               "    18:45  A FC (ENG)              v B FC (GER)\n", "CL")
    assert df.empty                       # no score reported yet


def test_parse_ignores_matches_before_any_date_line():
    df = parse("▪ League\n    18:45  A FC (ENG)   v B FC (GER)   1-0\n", "CL")
    assert df.empty


def test_load_uefa_history_offline(tmp_path):
    """The loader concatenates files and tolerates missing ones."""
    def fetcher(url, cache_file, max_age):
        if "/2025-26/cl.txt" in url:
            return SAMPLE.encode("utf-8")
        raise __import__("requests").RequestException("not published")

    df = load_uefa_history([2025], tmp_path, fetcher=fetcher)
    assert len(df) == 6
    assert set(df["div"]) == {"CL"}
    assert df["date"].is_monotonic_increasing

    empty = load_uefa_history([2030], tmp_path,
                              fetcher=lambda *a: (_ for _ in ()).throw(
                                  __import__("requests").RequestException("x")))
    assert empty.empty
