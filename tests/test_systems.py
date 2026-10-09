"""System bets (Systemwette): n selections, every k-leg combination.

The money cannot be attributed to individual legs — a double pays only when
both legs win — so recording a 5/2 as five singles would be wrong. Entering
the 2026-10-09 card that way would have reported a €0.95 loss on the 27.7% of
outcomes where exactly one leg wins, when the system actually loses the lot.

CLV is unaffected: it is a per-leg quantity and the legs are still recorded.
"""
import math

import pandas as pd
import pytest

from src import ledger
from src.config import load_config
from src.ledger import (COLUMNS, SYSTEM_LEG, add_system, load_systems, summarize,
                        system_payout, systems_path)

ODDS = [3.80, 2.65, 1.83, 3.20, 3.50]


@pytest.fixture()
def cfg(tmp_path):
    import copy
    c = copy.deepcopy(load_config())
    c["paths"]["ledger"] = str(tmp_path / "bets/ledger.csv")
    c["paths"]["paper_ledger"] = str(tmp_path / "bets/paper_ledger.csv")
    c["paths"]["systems"] = str(tmp_path / "bets/systems.csv")
    c["paths"]["reports"] = str(tmp_path / "reports")
    return c


def _picks(cfg, tmp_path, n=5):
    rows = [{"pick_id": f"P{i}", "date": "2026-10-09", "div": "E0", "home": f"H{i}",
             "away": f"A{i}", "market": "1X2", "outcome": "H", "label": f"主胜 H{i}",
             "p_final": 0.3, "min_odds": 3.0, "stake": 1.0} for i in range(n)]
    d = tmp_path / "reports"
    d.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(d / "2026-10-09_picks.csv", index=False)
    return [r["pick_id"] for r in rows]


# --- the payout arithmetic ----------------------------------------------------

@pytest.mark.parametrize("wins,expected_hits", [
    ([True] * 5, 10), ([True, True, False, False, False], 1),
    ([True, False, False, False, False], 0), ([False] * 5, 0),
])
def test_payout_counts_winning_combinations(wins, expected_hits):
    legs = list(zip(ODDS, wins))
    payout, hit, combos = system_payout(2, 2.0, legs)
    assert combos == math.comb(5, 2) == 10
    assert hit == expected_hits
    manual = sum(0.2 * ODDS[i] * ODDS[j]
                 for i in range(5) for j in range(i + 1, 5) if wins[i] and wins[j])
    assert payout == pytest.approx(manual)


def test_one_winning_leg_loses_everything():
    """The case recording it as singles gets most wrong, and the most common."""
    payout, _, _ = system_payout(2, 2.0, list(zip(ODDS, [True, False, False, False, False])))
    assert payout == 0.0


def test_payout_waits_for_every_leg():
    assert system_payout(2, 2.0, [(2.0, True), (2.0, None)]) == (None, 0, 0)


def test_k_equal_to_n_is_the_full_parlay():
    payout, hit, combos = system_payout(5, 2.0, list(zip(ODDS, [True] * 5)))
    assert combos == 1 and hit == 1
    assert payout == pytest.approx(2.0 * math.prod(ODDS))


# --- recording ----------------------------------------------------------------

def test_legs_carry_no_money_and_the_system_row_does(cfg, tmp_path):
    ids = _picks(cfg, tmp_path)
    sid = add_system(2, 2.0, dict(zip(ids, ODDS)), cfg, tmp_path, today="2026-10-09")

    df = ledger.load(ledger.ledger_path(cfg, tmp_path, False))
    assert len(df) == 5
    assert (df["kind"] == SYSTEM_LEG).all()
    assert (df["stake"] == 0.0).all(), "腿不能带钱，否则会和系统总额重复计算"
    assert (df["system_id"] == sid).all()
    assert df["odds"].tolist() == ODDS

    systems = load_systems(systems_path(cfg, tmp_path))
    assert len(systems) == 1
    row = systems.iloc[0]
    assert row["kind"] == "5/2" and row["k"] == 2 and row["stake"] == 2.0
    assert row["status"] == "open" and str(row["legs"]).split() == ids


@pytest.mark.parametrize("k", [0, 6])
def test_k_must_be_between_one_and_n(cfg, tmp_path, k):
    ids = _picks(cfg, tmp_path)
    with pytest.raises(SystemExit, match="k 必须"):
        add_system(k, 2.0, dict(zip(ids, ODDS)), cfg, tmp_path)


def test_needs_at_least_two_legs(cfg, tmp_path):
    ids = _picks(cfg, tmp_path, n=1)
    with pytest.raises(SystemExit, match="至少要两条腿"):
        add_system(1, 2.0, {ids[0]: 2.0}, cfg, tmp_path)


def test_unknown_pick_is_refused(cfg, tmp_path):
    ids = _picks(cfg, tmp_path, n=2)
    with pytest.raises(SystemExit, match="找不到 ID"):
        add_system(2, 2.0, {ids[0]: 2.0, "NOPE": 3.0}, cfg, tmp_path)


def test_the_same_system_cannot_be_recorded_twice(cfg, tmp_path):
    ids = _picks(cfg, tmp_path)
    legs = dict(zip(ids, ODDS))
    add_system(2, 2.0, legs, cfg, tmp_path, today="2026-10-09")
    with pytest.raises(SystemExit, match="已经记录过"):
        add_system(2, 2.0, legs, cfg, tmp_path, today="2026-10-09")


def test_a_pick_can_be_both_a_single_and_a_system_leg(cfg, tmp_path):
    ids = _picks(cfg, tmp_path)
    ledger.add(ids[0], odds=3.80, stake=1.0, cfg=cfg, root=tmp_path)
    add_system(2, 2.0, dict(zip(ids, ODDS)), cfg, tmp_path, today="2026-10-09")
    df = ledger.load(ledger.ledger_path(cfg, tmp_path, False))
    assert (df["id"] == ids[0]).sum() == 2
    assert set(df[df["id"] == ids[0]]["kind"]) == {"single", SYSTEM_LEG}


# --- settlement ---------------------------------------------------------------

def _settle_with(cfg, tmp_path, wins):
    played = pd.DataFrame([
        {"div": "E0", "date": pd.Timestamp("2026-10-09"), "home": f"H{i}", "away": f"A{i}",
         "hg": 2 if w else 0, "ag": 1}
        for i, w in enumerate(wins)])
    ledger.settle(cfg, root=tmp_path, today=pd.Timestamp("2026-10-10").date(),
                  history_loader=lambda *a, **k: played,
                  intl_loader=lambda *a, **k: pd.DataFrame(),
                  uefa_loader=lambda *a, **k: pd.DataFrame())
    return (ledger.load(ledger.ledger_path(cfg, tmp_path, False)),
            load_systems(systems_path(cfg, tmp_path)))


def test_settlement_pays_the_combinations_not_the_legs(cfg, tmp_path):
    ids = _picks(cfg, tmp_path)
    add_system(2, 2.0, dict(zip(ids, ODDS)), cfg, tmp_path, today="2026-10-09")
    wins = [True, True, False, False, False]
    df, systems = _settle_with(cfg, tmp_path, wins)

    assert (df["status"] == "settled").all()
    assert df["pnl"].isna().all(), "系统腿不能有自己的盈亏"
    row = systems.iloc[0]
    assert row["status"] == "settled"
    expected, _, _ = system_payout(2, 2.0, list(zip(ODDS, wins)))
    assert row["pnl"] == pytest.approx(round(expected - 2.0, 2))
    assert "5 中 2" in row["result"] and "10 注中 1 注" in row["result"]


def test_one_winner_settles_as_a_total_loss(cfg, tmp_path):
    ids = _picks(cfg, tmp_path)
    add_system(2, 2.0, dict(zip(ids, ODDS)), cfg, tmp_path, today="2026-10-09")
    _, systems = _settle_with(cfg, tmp_path, [True, False, False, False, False])
    assert systems.iloc[0]["pnl"] == pytest.approx(-2.0)


def test_system_stays_open_until_every_leg_is_decided(cfg, tmp_path):
    ids = _picks(cfg, tmp_path)
    add_system(2, 2.0, dict(zip(ids, ODDS)), cfg, tmp_path, today="2026-10-09")
    played = pd.DataFrame([{"div": "E0", "date": pd.Timestamp("2026-10-09"),
                            "home": "H0", "away": "A0", "hg": 2, "ag": 1}])
    ledger.settle(cfg, root=tmp_path, today=pd.Timestamp("2026-10-10").date(),
                  history_loader=lambda *a, **k: played,
                  intl_loader=lambda *a, **k: pd.DataFrame(),
                  uefa_loader=lambda *a, **k: pd.DataFrame())
    assert load_systems(systems_path(cfg, tmp_path)).iloc[0]["status"] == "open"


# --- the summary --------------------------------------------------------------

def test_clv_is_untouched_by_the_system_structure(cfg, tmp_path):
    """The whole point: legs keep their own closing price and CLV."""
    ids = _picks(cfg, tmp_path)
    add_system(2, 2.0, dict(zip(ids, ODDS)), cfg, tmp_path, today="2026-10-09")
    played = pd.DataFrame([
        {"div": "E0", "date": pd.Timestamp("2026-10-09"), "home": f"H{i}", "away": f"A{i}",
         "hg": 2, "ag": 1, "PSCH": o * 0.95, "PSCD": 3.5, "PSCA": 4.0}
        for i, o in enumerate(ODDS)])
    ledger.settle(cfg, root=tmp_path, today=pd.Timestamp("2026-10-10").date(),
                  history_loader=lambda *a, **k: played,
                  intl_loader=lambda *a, **k: pd.DataFrame(),
                  uefa_loader=lambda *a, **k: pd.DataFrame())
    df = ledger.load(ledger.ledger_path(cfg, tmp_path, False))
    assert df["clv"].notna().all()
    assert df["clv_novig"].notna().all()
    d = summarize(df, load_systems(systems_path(cfg, tmp_path)))
    assert d["sharp_n"] == 5 and d["clv_novig"] is not None


def test_summary_counts_the_system_money_once(cfg, tmp_path):
    ids = _picks(cfg, tmp_path)
    add_system(2, 2.0, dict(zip(ids, ODDS)), cfg, tmp_path, today="2026-10-09")
    wins = [True, True, False, False, False]
    df, systems = _settle_with(cfg, tmp_path, wins)
    d = summarize(df, systems)
    assert d["settled"] == 0, "系统腿不算作已结算的单注"
    assert d["systems_settled"] == 1
    assert d["staked"] == pytest.approx(2.0), "总投入只能算一次"
    assert d["pnl"] == pytest.approx(systems.iloc[0]["pnl"])
    text = ledger.format_summary("真实投注", d)
    assert "系统投注已结算 1 组" in text


def test_summary_without_any_system(cfg, tmp_path):
    ids = _picks(cfg, tmp_path, n=2)
    ledger.add(ids[0], odds=3.80, stake=1.0, cfg=cfg, root=tmp_path)
    d = summarize(ledger.load(ledger.ledger_path(cfg, tmp_path, False)), pd.DataFrame())
    assert d["systems_settled"] == 0 and d["systems_open"] == 0
    assert "系统投注" not in ledger.format_summary("真实投注", d)
