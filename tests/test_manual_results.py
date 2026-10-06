"""Hand-entered results, used when a feed has not caught up.

Both results feeds lag, and the effect of a gap is not symmetric: filling in
one team's matches can move a price the opposite way from filling in both.
On 2026-10-06 the September window was missing for every national team, and
Belarus vs Finland went 0.276 -> 0.282 on Belarus's three results alone but
0.276 -> 0.259 once Finland's were added too.
"""
import pandas as pd
import pytest

from src import daily, intl, ledger, manual
from src.config import load_config
from src.manual import (RESULT_COLUMNS, RESULT_TEMPLATE, apply_results, load_results,
                        merge_results, write_result_template)
from tests.synthetic import make_neutral_series

NL = "UEFA Nations League"


def _results_file(tmp_path, *rows):
    p = tmp_path / "manual_results.csv"
    p.write_text(RESULT_TEMPLATE + "".join(r + "\n" for r in rows), encoding="utf-8")
    return p


def test_template_alone_parses_as_zero_rows(tmp_path):
    df = load_results(_results_file(tmp_path))
    assert df.empty and "home" in df.columns


def test_missing_file_is_not_an_error(tmp_path):
    assert load_results(tmp_path / "nope.csv").empty


def test_write_result_template_does_not_clobber(tmp_path):
    p = tmp_path / "sub" / "manual_results.csv"
    write_result_template(p)
    p.write_text(p.read_text(encoding="utf-8") + f"INT,2026-09-29,Finland,Belarus,0,0,0,{NL}\n",
                 encoding="utf-8")
    write_result_template(p)
    assert len(load_results(p)) == 1


def test_load_results_parses_and_filters(tmp_path):
    p = _results_file(
        tmp_path,
        f"INT,2026-09-29,Finland,Belarus,0,0,0,{NL}",
        "CL,2026-09-30,Real Madrid,Juventus,1,0,1,",
        "INT,bad-date,A,B,1,0,0,",          # unparseable date
        "INT,2026-09-30,A,B,,,0,",          # no score yet
        "INT,2026-09-30,,B,1,0,0,",         # no team
    )
    df = load_results(p)
    assert len(df) == 2
    assert df["hg"].dtype.kind == "i"
    cl = df[df["div"] == "CL"].iloc[0]
    assert bool(cl["neutral"]) is True and cl["date"] == pd.Timestamp("2026-09-30")
    assert len(load_results(p, divs=["INT"])) == 1


def test_merge_adds_only_what_the_feed_lacks():
    base = pd.DataFrame([
        {"div": "INT", "date": pd.Timestamp("2026-09-29"), "home": "Finland",
         "away": "Belarus", "hg": 0, "ag": 0, "neutral": False, "tournament": NL},
    ])
    extra = pd.DataFrame([
        # same fixture, a day off: the two sources disagree over time zones
        {"div": "INT", "date": pd.Timestamp("2026-09-30"), "home": "Finland",
         "away": "Belarus", "hg": 0, "ag": 0, "neutral": False, "tournament": NL},
        {"div": "INT", "date": pd.Timestamp("2026-10-03"), "home": "Belarus",
         "away": "San Marino", "hg": 4, "ag": 0, "neutral": False, "tournament": NL},
    ])
    merged, added = merge_results(base, extra)
    assert added == 1
    assert len(merged) == 2
    assert merged["date"].is_monotonic_increasing
    # the reverse fixture is a different match and must not be deduped away
    reverse = extra.assign(home="Belarus", away="Finland")
    assert merge_results(base, reverse.head(1))[1] == 1


def test_merge_into_an_empty_feed():
    extra = pd.DataFrame([{"div": "INT", "date": pd.Timestamp("2026-10-03"), "home": "A",
                           "away": "B", "hg": 1, "ag": 0, "neutral": False, "tournament": NL}])
    merged, added = merge_results(pd.DataFrame(), extra)
    assert added == 1 and len(merged) == 1


def test_apply_results_skips_an_excluded_tournament(tmp_path):
    """A friendly entered by accident must not override the config."""
    p = _results_file(tmp_path,
                      f"INT,2026-09-29,Finland,Belarus,0,0,0,{NL}",
                      "INT,2026-09-30,Belarus,Syria,4,1,0,Friendly")
    merged, notes = apply_results(pd.DataFrame(), p, ["INT"], tournaments=[NL])
    assert len(merged) == 1
    assert any("Friendly" in n and "没有计入" in n for n in notes)
    assert any("已合并 1 场" in n for n in notes)


def test_apply_results_treats_a_blank_tournament_as_deliberate(tmp_path):
    p = _results_file(tmp_path, "INT,2026-09-29,Finland,Belarus,0,0,0,")
    merged, _ = apply_results(pd.DataFrame(), p, ["INT"], tournaments=[NL])
    assert len(merged) == 1


def test_apply_results_is_a_no_op_without_a_file(tmp_path):
    base = pd.DataFrame([{"div": "INT", "date": pd.Timestamp("2026-01-01"), "home": "A",
                          "away": "B", "hg": 1, "ag": 0, "neutral": False, "tournament": NL}])
    merged, notes = apply_results(base, tmp_path / "nope.csv", ["INT"])
    assert merged is base and notes == []


def test_append_result_requires_the_score(tmp_path):
    p = tmp_path / "manual_results.csv"
    with pytest.raises(SystemExit):
        manual.append_result(p, {"comp": "INT", "date": "2026-09-29", "home": "A",
                                 "away": "B", "hg": "", "ag": "1"})
    manual.append_result(p, {"comp": "INT", "date": "2026-09-29", "home": "A",
                             "away": "B", "hg": "0", "ag": "1", "tournament": NL})
    assert len(load_results(p)) == 1


# --- reaching the models ------------------------------------------------------

@pytest.fixture()
def cfg(tmp_path):
    import copy
    c = copy.deepcopy(load_config())
    c["leagues"] = {"E0": "英超"}
    for k in ("cache", "reports"):
        c["paths"][k] = str(tmp_path / k)
    c["paths"]["ledger"] = str(tmp_path / "bets/ledger.csv")
    c["paths"]["paper_ledger"] = str(tmp_path / "bets/paper_ledger.csv")
    c["paths"]["manual_fixtures"] = "manual_fixtures.csv"
    c["paths"]["manual_results"] = "manual_results.csv"
    c["international"]["min_team_matches"] = 5
    return c


def test_manual_results_change_the_international_prediction(cfg, tmp_path):
    base, _ = make_neutral_series(n=900, seed=21)
    base["tournament"] = NL
    base["date"] = pd.Timestamp("2026-07-19") - pd.to_timedelta(range(len(base)), unit="D")
    today = pd.Timestamp("2026-10-06")

    (tmp_path / "manual_fixtures.csv").write_text(
        manual.TEMPLATE + f"INT,{today:%Y-%m-%d},20:45,N00,N01,0,"
                          f"2.60,3.30,2.90,2.70,3.40,3.00,,,,\n", encoding="utf-8")

    def run():
        return daily.analyze(
            cfg, today, root=tmp_path,
            history_loader=lambda *a, **k: pd.DataFrame(),
            fixtures_loader=lambda *a, **k: pd.DataFrame(),
            pool_loader=lambda c, cache, today=None: (pd.DataFrame(), {}),
            intl_loader=lambda c, cache, today=None, **kw: base,
        )

    before, _, notes_before = run()
    assert not any("已合并" in n for n in notes_before)

    # N01 thrashes everyone in the window the feed has not published yet
    _results_file(tmp_path, *[
        f"INT,2026-09-2{d},N01,N{t:02d},5,0,0,{NL}" for d, t in enumerate([2, 3, 4, 5, 6])
    ])
    after, _, notes_after = run()

    assert any("已合并 5 场手录赛果" in n for n in notes_after)
    h_before = before[before["outcome"] == "H"]["p_model"].iloc[0]
    h_after = after[after["outcome"] == "H"]["p_model"].iloc[0]
    assert h_after < h_before, "对手变强了，主胜概率应当下降"


def test_manual_results_refresh_the_staleness_warning(cfg, tmp_path):
    base, _ = make_neutral_series(n=600, seed=22)
    base["tournament"] = NL
    base["date"] = pd.Timestamp("2026-07-19") - pd.to_timedelta(range(len(base)), unit="D")
    today = pd.Timestamp("2026-10-06")
    (tmp_path / "manual_fixtures.csv").write_text(
        manual.TEMPLATE + f"INT,{today:%Y-%m-%d},20:45,N00,N01,0,"
                          f"2.60,3.30,2.90,2.70,3.40,3.00,,,,\n", encoding="utf-8")
    _results_file(tmp_path, f"INT,2026-10-03,N00,N02,1,0,0,{NL}")
    _, _, notes = daily.analyze(
        cfg, today, root=tmp_path,
        history_loader=lambda *a, **k: pd.DataFrame(),
        fixtures_loader=lambda *a, **k: pd.DataFrame(),
        pool_loader=lambda c, cache, today=None: (pd.DataFrame(), {}),
        intl_loader=lambda c, cache, today=None, **kw: base,
    )
    assert not any("赛果数据最新到" in n for n in notes), "合并之后数据不再算过期"


def test_settle_uses_a_hand_entered_result(cfg, tmp_path):
    """A bet on a match the feed has not published can still be settled."""
    path = tmp_path / cfg["paths"]["paper_ledger"]
    path.parent.mkdir(parents=True, exist_ok=True)
    row = ledger._row_from_pick(
        {"pick_id": "x", "date": pd.Timestamp("2026-09-29"), "div": "INT", "home": "Finland",
         "away": "Belarus", "market": "1X2", "outcome": "D", "label": "平局",
         "p_final": 0.3}, odds=4.06, stake=1.0, today="2026-09-29")
    ledger.save(ledger._append(ledger.load(path), [row]), path)

    _results_file(tmp_path, f"INT,2026-09-29,Finland,Belarus,0,0,0,{NL}")
    ledger.settle(cfg, root=tmp_path, today=pd.Timestamp("2026-10-06").date(),
                  history_loader=lambda *a, **k: pd.DataFrame(),
                  intl_loader=lambda *a, **k: pd.DataFrame(),
                  uefa_loader=lambda *a, **k: pd.DataFrame())
    df = ledger.load(path)
    assert df["status"].iloc[0] == "settled"
    assert df["result"].iloc[0].startswith("0-0") and "赢" in df["result"].iloc[0]
    assert pd.isna(df["clv"].iloc[0])        # still no closing odds for internationals
