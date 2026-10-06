"""The daily run with all three fixture sources, fully offline."""
import copy

import pandas as pd
import pytest

from src import daily, ledger, manual
from src.config import load_config
from tests.synthetic import loaders, make_league, make_neutral_series, make_world


@pytest.fixture(scope="module")
def world():
    return make_world(seasons=4, cup_rounds=8)


@pytest.fixture()
def cfg(tmp_path):
    c = copy.deepcopy(load_config())
    c["leagues"] = {"E0": "英超"}
    for k in ("cache", "reports"):
        c["paths"][k] = str(tmp_path / k)
    c["paths"]["ledger"] = str(tmp_path / "bets/ledger.csv")
    c["paths"]["paper_ledger"] = str(tmp_path / "bets/paper_ledger.csv")
    c["paths"]["manual_fixtures"] = "manual_fixtures.csv"
    c["uefa"]["min_team_matches"] = 5
    c["international"]["min_team_matches"] = 5
    return c


def _manual_file(tmp_path, *rows):
    p = tmp_path / "manual_fixtures.csv"
    p.write_text(manual.TEMPLATE + "".join(r + "\n" for r in rows), encoding="utf-8")
    return p


def _run(cfg, tmp_path, today, pool=None, intl_df=None, league=None):
    hl, fl = (loaders(*league[:2]) if league else
              (lambda *a, **k: pd.DataFrame(), lambda *a, **k: pd.DataFrame()))
    return daily.analyze(
        cfg, today, root=tmp_path, history_loader=hl, fixtures_loader=fl,
        pool_loader=lambda c, cache, today=None: (pool, {"domestic": 1, "uefa": 1,
                                                         "unresolved": [], "linked_teams": 2}),
        intl_loader=lambda c, cache, today=None, **kw: intl_df,
    )


def test_competition_names_covers_leagues_and_manual():
    cfg = load_config()
    names = daily.competition_names(cfg)
    assert names["E0"] == cfg["leagues"]["E0"]
    assert names["CL"] == "欧冠" and names["INT"] == "国家队"


def test_no_manual_file_is_silent(cfg, tmp_path):
    all_df, picks, notes = _run(cfg, tmp_path, pd.Timestamp("2026-10-06"))
    assert all_df.empty and picks.empty
    assert not any("手填" in n for n in notes)


def test_uefa_fixture_becomes_a_manual_pick(cfg, tmp_path, world):
    domestic, cup, today, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    home, away = truth["teams"][0], truth["teams"][-1]   # strongest league vs weakest
    # reference odds that understate the home side, so the model sees value,
    # and a Tipico price above the minimum
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{home},{away},0,"
                           f"3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    all_df, picks, notes = _run(cfg, tmp_path, today, pool=pool)

    assert not all_df.empty
    row = all_df[all_df["outcome"] == "H"].iloc[0]
    assert row["div"] == "CL" and row["league"] == "欧冠" and row["manual"]
    assert row["price_source"] == "tipico"
    assert not picks.empty and picks["manual"].all()

    report = daily.render_report(today, picks, all_df, notes, cfg)
    assert "欧战 / 国家队（手填赔率）" in report
    assert "无法计算 CLV" in report
    assert "## 联赛" not in report            # nothing from the league feed today


def test_international_fixture_uses_the_neutral_flag(cfg, tmp_path):
    df, _ = make_neutral_series(n=1200, seed=9, home_adv=0.35)
    today = pd.Timestamp("2026-10-06")
    rows = []
    for neutral in (0, 1):
        rows.append(f"INT,{today:%Y-%m-%d},20:45,N00,N01,{neutral},"
                    f"2.60,3.30,2.90,2.70,3.40,3.00,,,,")
    _manual_file(tmp_path, *rows)
    all_df, _, _ = _run(cfg, tmp_path, today, intl_df=df)
    home = all_df[all_df["outcome"] == "H"].sort_values("p_model", ascending=False)
    assert len(home) == 2
    # same teams, same prices: the only difference is the venue
    assert home["p_model"].iloc[0] > home["p_model"].iloc[1]


def test_unknown_team_is_reported_with_a_suggestion(cfg, tmp_path, world):
    domestic, cup, today, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    typo = truth["teams"][0][:-2] + "99"       # close to a real name, but not one
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{typo},{truth['teams'][-1]},0,"
                           f"3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    all_df, picks, notes = _run(cfg, tmp_path, today, pool=pool)
    assert all_df.empty and picks.empty
    assert any(typo in n and "模型不认识" in n for n in notes)


def test_unknown_competition_code_is_reported(cfg, tmp_path):
    today = pd.Timestamp("2026-10-06")
    _manual_file(tmp_path, f"ZZZ,{today:%Y-%m-%d},21:00,A,B,0,2.0,3.5,4.0,2.1,3.6,4.1,,,,")
    _, _, notes = _run(cfg, tmp_path, today)
    assert any("ZZZ" in n for n in notes)


def test_disabled_models_are_skipped_with_a_note(cfg, tmp_path):
    cfg["uefa"]["enabled"] = False
    today = pd.Timestamp("2026-10-06")
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,A,B,0,2.0,3.5,4.0,2.1,3.6,4.1,,,,")
    _, picks, notes = _run(cfg, tmp_path, today)
    assert picks.empty
    assert any("关闭" in n for n in notes)


def test_league_and_manual_picks_are_reported_separately(cfg, tmp_path, world):
    league = make_league(div="E0", n_teams=12, seasons=3, seed=1)
    today = league[2]
    domestic, cup, _, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{truth['teams'][0]},"
                           f"{truth['teams'][-1]},0,3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    cfg["value"]["min_edge"] = -0.5             # force league picks too
    cfg["value"]["max_picks"] = 20
    all_df, picks, notes = _run(cfg, tmp_path, today, pool=pool, league=league)
    assert picks["manual"].any() and (~picks["manual"]).any()
    report = daily.render_report(today, picks, all_df, notes, cfg)
    assert "## 联赛" in report and "欧战 / 国家队（手填赔率）" in report
    # numbering runs continuously across the two tables
    assert "| 1 |" in report and f"| {len(picks)} |" in report


def test_manual_picks_are_logged_as_paper_bets(cfg, tmp_path, world):
    domestic, cup, today, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{truth['teams'][0]},"
                           f"{truth['teams'][-1]},0,3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    picks = daily.run(
        cfg, today=today, root=tmp_path,
        history_loader=lambda *a, **k: pd.DataFrame(),
        fixtures_loader=lambda *a, **k: pd.DataFrame(),
        pool_loader=lambda c, cache, today=None: (pool, {"domestic": 1, "uefa": 1}),
        intl_loader=lambda c, cache, today=None, **kw: pd.DataFrame(),
    )
    assert not picks.empty
    paper = ledger.load(tmp_path / cfg["paths"]["paper_ledger"])
    assert len(paper) == len(picks)
    assert set(paper["div"]) == {"CL"}


def test_settle_handles_manual_competitions(cfg, tmp_path, world):
    """A European bet settles for P&L from the results source, with no CLV."""
    domestic, cup, today, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    home, away = truth["teams"][0], truth["teams"][-1]
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{home},{away},0,"
                           f"3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    daily.run(cfg, today=today, root=tmp_path,
              history_loader=lambda *a, **k: pd.DataFrame(),
              fixtures_loader=lambda *a, **k: pd.DataFrame(),
              pool_loader=lambda c, cache, today=None: (pool, {}),
              intl_loader=lambda c, cache, today=None, **kw: pd.DataFrame())

    played = pd.DataFrame([{"div": "CL", "date": today, "home": home, "away": away,
                            "hg": 3, "ag": 0, "neutral": False}])
    ledger.settle(cfg, root=tmp_path, today=today.date(),
                  history_loader=lambda *a, **k: pd.DataFrame(),
                  intl_loader=lambda *a, **k: pd.DataFrame(),
                  uefa_loader=lambda *a, **k: played)
    paper = ledger.load(tmp_path / cfg["paths"]["paper_ledger"])
    assert (paper["status"] == "settled").all()
    assert paper["result"].iloc[0].startswith("3-0")
    assert pd.isna(paper["clv"].iloc[0])      # no closing odds exist for the cup


def test_settle_leaves_unknown_results_open(cfg, tmp_path, world):
    domestic, cup, today, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{truth['teams'][0]},"
                           f"{truth['teams'][-1]},0,3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    daily.run(cfg, today=today, root=tmp_path,
              history_loader=lambda *a, **k: pd.DataFrame(),
              fixtures_loader=lambda *a, **k: pd.DataFrame(),
              pool_loader=lambda c, cache, today=None: (pool, {}),
              intl_loader=lambda c, cache, today=None, **kw: pd.DataFrame())
    ledger.settle(cfg, root=tmp_path, today=today.date(),
                  history_loader=lambda *a, **k: pd.DataFrame(),
                  intl_loader=lambda *a, **k: pd.DataFrame(),
                  uefa_loader=lambda *a, **k: pd.DataFrame())
    paper = ledger.load(tmp_path / cfg["paths"]["paper_ledger"])
    assert (paper["status"] == "open").all()
