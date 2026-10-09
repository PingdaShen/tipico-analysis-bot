"""The daily run with all three fixture sources, fully offline."""
import copy

import numpy as np
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


# --- data freshness -----------------------------------------------------------

def test_freshness_note_only_fires_when_stale():
    today = pd.Timestamp("2026-10-06")
    assert daily.freshness_note("国家队", pd.Timestamp("2026-10-01"), today) is None
    note = daily.freshness_note("国家队", pd.Timestamp("2026-07-19"), today)
    assert note is not None and "2026-07-19" in note and "79 天" in note
    assert "没有任何赛果数据" in daily.freshness_note("欧战", None, today)


def test_report_warns_that_international_data_is_stale(cfg, tmp_path):
    """The September window missing is invisible in the numbers; say it."""
    df, _ = make_neutral_series(n=900, seed=12)
    df["date"] = pd.Timestamp("2026-07-19") - pd.to_timedelta(np.arange(len(df)) * 3, "D")
    today = pd.Timestamp("2026-10-06")
    _manual_file(tmp_path, f"INT,{today:%Y-%m-%d},20:45,N00,N01,0,"
                           f"2.60,3.30,2.90,2.70,3.40,3.00,,,,")
    _, _, notes = _run(cfg, tmp_path, today, intl_df=df)
    assert any("国家队" in n and "2026-07-19" in n for n in notes)


def test_report_warns_that_uefa_results_lag_a_season(cfg, tmp_path, world):
    domestic, cup, _, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    today = pd.Timestamp(pool["date"].max()) + pd.Timedelta(days=200)
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{truth['teams'][0]},"
                           f"{truth['teams'][-1]},0,3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    _, _, notes = daily.analyze(
        cfg, today, root=tmp_path,
        history_loader=lambda *a, **k: pd.DataFrame(),
        fixtures_loader=lambda *a, **k: pd.DataFrame(),
        pool_loader=lambda c, cache, today=None: (
            pool, {"uefa": len(cup), "uefa_latest": cup["date"].max()}),
        intl_loader=lambda c, cache, today=None, **kw: pd.DataFrame(),
    )
    assert any("欧战" in n and "模型还没看到" in n for n in notes)


# --- the report has to surface the pick IDs ------------------------------------

def _report_for(cfg, tmp_path, world):
    domestic, cup, today, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{truth['teams'][0]},"
                           f"{truth['teams'][-1]},0,3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    all_df, picks, notes = _run(cfg, tmp_path, today, pool=pool)
    assert not picks.empty
    return daily.render_report(today, picks, all_df, notes, cfg), picks


def test_pick_ids_are_findable_outside_a_shell_command(cfg, tmp_path, world):
    """They are needed twice per bet in web forms, not in a terminal."""
    report, picks = _report_for(cfg, tmp_path, world)
    pick_id = picks.iloc[0]["pick_id"]
    assert "## 投注 ID" in report
    # on its own line in a fenced block, so GitHub renders a copy button
    assert f"\n```\n{pick_id}\n```\n" in report
    assert picks.iloc[0]["label"] in report


def test_report_tells_you_to_record_the_closing_odds(cfg, tmp_path, world):
    """For a hand-entered competition it is the only route to a CLV."""
    report, _ = _report_for(cfg, tmp_path, world)
    assert "record-close" in report
    assert "开球前" in report


def test_terminal_commands_are_collapsed_not_removed(cfg, tmp_path, world):
    report, picks = _report_for(cfg, tmp_path, world)
    assert "<details>" in report and "</details>" in report
    assert f"python -m src.ledger add {picks.iloc[0]['pick_id']}" in report
    assert f"python -m src.ledger close {picks.iloc[0]['pick_id']}" in report


def test_league_only_picks_skip_the_closing_step(cfg, tmp_path):
    """Leagues get their closing odds automatically; do not ask for them."""
    league = make_league(div="E0", n_teams=12, seasons=3, seed=1)
    cfg["value"]["min_edge"] = -0.5
    all_df, picks, notes = _run(cfg, tmp_path, league[2], league=league)
    assert not picks.empty and not picks["manual"].any()
    report = daily.render_report(league[2], picks, all_df, notes, cfg)
    assert "## 投注 ID" in report
    assert "record-close" not in report
    assert "ledger close" not in report


# --- hand-entered league fixtures ---------------------------------------------

def test_a_league_match_can_be_entered_by_hand(cfg, tmp_path):
    """fixtures.csv is unreliable, so the feed must not be the only way in.

    On 2026-10-06 it had not been regenerated since 10-02, listed only past
    dates and covered 7 of the 22 configured leagues, so a weekend of
    Bundesliga / La Liga / Ligue 1 fixtures produced no report at all.
    """
    league = make_league(div="E0", n_teams=12, seasons=3, seed=1)
    hist_raw, fix_raw, today, _ = league
    hl, _ = loaders(hist_raw, fix_raw)
    _manual_file(tmp_path, f"E0,{today:%Y-%m-%d},15:00,Team00,Team01,0,"
                           f"2.00,3.80,4.60,2.15,3.90,4.80,,,,")

    all_df, picks, notes = daily.analyze(
        cfg, today, root=tmp_path, history_loader=hl,
        fixtures_loader=lambda *a, **k: pd.DataFrame(),       # feed is down
        pool_loader=lambda c, cache, today=None: (pd.DataFrame(), {}),
        intl_loader=lambda c, cache, today=None, **kw: pd.DataFrame(),
    )
    assert not all_df.empty, "手填的联赛比赛应当被评估"
    row = all_df.iloc[0]
    assert row["div"] == "E0"
    assert row["price_source"] == "tipico"
    # a league stays a league: it settles automatically and gets a real CLV,
    # so it must not be filed under the hand-entered section
    assert not all_df["manual"].any()
    assert not any("不是已知的赛事代码" in n for n in notes)


def test_hand_entered_league_uses_its_own_model(cfg, tmp_path):
    league = make_league(div="E0", n_teams=12, seasons=3, seed=1)
    hist_raw, fix_raw, today, _ = league
    hl, _ = loaders(hist_raw, fix_raw)
    _manual_file(tmp_path, f"E0,{today:%Y-%m-%d},15:00,Team00,Team01,0,"
                           f"2.00,3.80,4.60,2.15,3.90,4.80,,,,")
    all_df, _, _ = daily.analyze(
        cfg, today, root=tmp_path, history_loader=hl,
        fixtures_loader=lambda *a, **k: pd.DataFrame(),
        pool_loader=lambda c, cache, today=None: (pd.DataFrame(), {}),
        intl_loader=lambda c, cache, today=None, **kw: pd.DataFrame())
    from src.daily import fit_model
    expected = fit_model(hl("E0", [], None, today=today.date()), cfg, today)
    p = expected.predict("Team00", "Team01")
    assert all_df[all_df["outcome"] == "H"]["p_model"].iloc[0] == pytest.approx(p["H"])


def test_unknown_competition_code_lists_what_is_valid(cfg, tmp_path):
    today = pd.Timestamp("2026-10-06")
    _manual_file(tmp_path, f"ZZZ,{today:%Y-%m-%d},21:00,A,B,0,2.0,3.5,4.0,2.1,3.6,4.1,,,,")
    _, _, notes = _run(cfg, tmp_path, today)
    note = next(n for n in notes if "ZZZ" in n)
    assert "不是已知的赛事代码" in note
    assert "E0" in note and "CL" in note


def test_stale_fixture_feed_says_how_stale(cfg, tmp_path):
    """The old note just called the feed unreliable; say the actual lag."""
    today = pd.Timestamp("2026-10-09")
    feed = pd.DataFrame({"div": ["E2", "SC3"],
                         "date": [pd.Timestamp("2026-10-05")] * 2,
                         "home": ["a", "c"], "away": ["b", "d"]})
    _, _, notes = daily.analyze(
        cfg, today, root=tmp_path, history_loader=lambda *a, **k: pd.DataFrame(),
        fixtures_loader=lambda *a, **k: feed,
        pool_loader=lambda c, cache, today=None: (pd.DataFrame(), {}),
        intl_loader=lambda c, cache, today=None, **kw: pd.DataFrame())
    note = next(n for n in notes if "fixtures.csv" in n)
    assert "2026-10-05" in note and "4 天前" in note
    assert "manual_fixtures.csv" in note
    # the feed is on a published twice-weekly schedule, not broken — say so
    assert "周五下午" in note and "周二下午" in note


def test_header_names_the_window_not_just_today(cfg, tmp_path, world):
    """On a Friday the Saturday card is ten times the size, so the picks are
    usually not today's matches; the old "今日投注建议" header misled."""
    report, _ = _report_for(cfg, tmp_path, world)
    today = pd.Timestamp(world[2])
    last = today + pd.Timedelta(days=cfg["value"]["horizon_days"] - 1)
    assert f"覆盖 {today:%m-%d} 至 {last:%m-%d} 开赛的比赛" in report
    assert "今日投注建议" not in report


def test_single_day_horizon_reads_naturally(cfg, tmp_path, world):
    cfg["value"]["horizon_days"] = 1
    today = pd.Timestamp(world[2])
    report = daily.render_report(today, pd.DataFrame(), pd.DataFrame(), [], cfg)
    assert f"覆盖 {today:%m-%d} 开赛的比赛" in report
    assert "至" not in report.splitlines()[2]


# --- CLI overrides ------------------------------------------------------------

def test_horizon_override_narrows_the_window(cfg, tmp_path, monkeypatch):
    """A Friday run covers Saturday too, and Saturday's card is ten times the
    size, so --horizon 1 is how you see only tonight."""
    import sys
    from src import daily as daily_mod

    seen = {}
    monkeypatch.setattr(daily_mod, "load_config", lambda p=None: cfg)
    monkeypatch.setattr(daily_mod, "run",
                        lambda c, today=None: seen.update(horizon=c["value"]["horizon_days"],
                                                          reports=c["paths"]["reports"]))
    monkeypatch.setattr(sys, "argv", ["daily", "--date", "2026-10-09", "--horizon", "1",
                                      "--out", str(tmp_path / "out")])
    daily_mod.main()
    assert seen["horizon"] == 1
    assert seen["reports"] == str(tmp_path / "out")


def test_horizon_must_be_at_least_one(cfg, monkeypatch):
    import sys
    from src import daily as daily_mod
    monkeypatch.setattr(daily_mod, "load_config", lambda p=None: cfg)
    monkeypatch.setattr(sys, "argv", ["daily", "--horizon", "0"])
    with pytest.raises(SystemExit):
        daily_mod.main()


def test_without_the_flags_config_is_untouched(cfg, monkeypatch):
    import sys
    from src import daily as daily_mod
    seen = {}
    monkeypatch.setattr(daily_mod, "load_config", lambda p=None: cfg)
    monkeypatch.setattr(daily_mod, "run",
                        lambda c, today=None: seen.update(horizon=c["value"]["horizon_days"]))
    monkeypatch.setattr(sys, "argv", ["daily"])
    daily_mod.main()
    assert seen["horizon"] == cfg["value"]["horizon_days"]


# --- per-day cap and kick-off times -------------------------------------------

def test_max_picks_applies_per_match_day(cfg, tmp_path):
    """A global cap let Saturday's ten-times-bigger card take every slot."""
    league = make_league(div="E0", n_teams=12, seasons=3, seed=1)
    hist_raw, fix_raw, today, _ = league
    # one fixture today, the rest tomorrow
    fix = fix_raw.copy()
    fix["Date"] = [(today if i == 0 else today + pd.Timedelta(days=1)).strftime("%d/%m/%Y")
                   for i in range(len(fix))]
    hl, fl = loaders(hist_raw, fix)
    cfg["value"]["min_edge"] = -0.5          # force plenty of candidates
    cfg["value"]["max_picks"] = 2
    _, picks, _ = daily.analyze(cfg, today, root=tmp_path, history_loader=hl,
                                fixtures_loader=fl)
    per_day = picks.groupby("date").size()
    assert len(per_day) == 2, "两天都应该有推荐"
    assert (per_day <= 2).all()
    assert picks["date"].is_monotonic_increasing, "按比赛日排序，当天在前"


def test_kickoff_times_are_shifted_to_german_time():
    fx = pd.DataFrame({"Time": ["15:00", "19:45", "23:30", "", "tbc"]})
    out = daily.shift_kickoff(fx, 1)["Time"].tolist()
    assert out[:2] == ["16:00", "20:45"]
    assert out[2] == "00:30(+1)", "跨午夜要标出来，日期没有跟着改"
    assert out[3] == "" and out[4] == "tbc"


def test_kickoff_shift_is_a_no_op_at_zero():
    fx = pd.DataFrame({"Time": ["15:00"]})
    assert daily.shift_kickoff(fx, 0)["Time"].iloc[0] == "15:00"
    assert daily.shift_kickoff(pd.DataFrame(), 1).empty


def test_hand_entered_times_are_not_shifted(cfg, tmp_path, world):
    """They are already the user's own local time."""
    domestic, cup, today, truth = world
    pool = pd.concat([domestic, cup], ignore_index=True)
    _manual_file(tmp_path, f"CL,{today:%Y-%m-%d},21:00,{truth['teams'][0]},"
                           f"{truth['teams'][-1]},0,3.00,3.60,2.40,3.20,3.70,2.50,,,,")
    all_df, _, _ = _run(cfg, tmp_path, today, pool=pool)
    assert all_df.iloc[0]["time"] == "21:00"


def test_league_model_sees_hand_entered_results(cfg, tmp_path):
    """football-data publishes a round a day or two late, so without this the
    model would price Saturday's card without having seen Friday's."""
    league = make_league(div="E0", n_teams=12, seasons=3, seed=1)
    hist_raw, fix_raw, today, _ = league
    hl, fl = loaders(hist_raw, fix_raw)

    base, notes = daily.league_history("E0", cfg, tmp_path, tmp_path, today, hl)
    assert not notes

    (tmp_path / "manual_results.csv").write_text(
        "comp,date,home,away,hg,ag,neutral,tournament\n"
        f"E0,{today:%Y-%m-%d},Team00,Team01,5,0,0,\n", encoding="utf-8")
    cfg["paths"]["manual_results"] = "manual_results.csv"
    merged, notes = daily.league_history("E0", cfg, tmp_path, tmp_path, today, hl)

    assert len(merged) == len(base) + 1
    assert any("已合并 1 场手录赛果" in n for n in notes)
    # the model is fitted strictly before ref_date, so the same-day result only
    # counts from the next day on — which is exactly when it should
    later = today + pd.Timedelta(days=1)
    before = daily.fit_model(base, cfg, later)
    after = daily.fit_model(merged, cfg, later)
    assert after.predict("Team00", "Team01")["H"] > before.predict("Team00", "Team01")["H"]
