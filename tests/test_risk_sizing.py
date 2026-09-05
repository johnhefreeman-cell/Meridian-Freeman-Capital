"""Tests for the risk-contribution sizing tool.

The failure that matters here is silent and directional: a weighting bug that
sizes *up* into volatility rather than down would look like a plausible table
and quietly concentrate risk. So the sign of the relationship is asserted
explicitly, not just the arithmetic.
"""

from __future__ import annotations

import datetime as dt
import math
import sys
from pathlib import Path

import openpyxl
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import risk_sizing as rs  # noqa: E402


def price_series(start: float, weekly: list[float]) -> dict:
    """{date: price} walking `start` forward by the given weekly returns."""
    d, p, out = dt.datetime(2025, 1, 6), start, {}
    out[d] = p
    for r in weekly:
        d += dt.timedelta(days=7)
        p *= (1 + r)
        out[d] = p
    return out


def alternating(magnitude: float, n: int = 40) -> list[float]:
    """Zero-drift saw-tooth: realized vol scales with `magnitude`."""
    return [magnitude if i % 2 == 0 else -magnitude for i in range(n)]


def build_workbook(path: Path, holdings: dict[str, float],
                   vols: dict[str, float]) -> Path:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Asset PM"
    ws.append([None] * 12)
    for ticker, value in holdings.items():
        row = [None] * 12
        row[rs.HOLD_TICKER_COL] = ticker
        row[rs.HOLD_VALUE_COL] = value
        ws.append(row)
    for ticker, mag in vols.items():
        sh = wb.create_sheet(f"HMM {ticker}")
        sh.append([None] * 10)
        for d, p in price_series(100.0, alternating(mag)).items():
            row = [None] * 10
            row[rs.DATE_COL] = d
            row[rs.PRICE_COL] = p
            sh.append(row)
    wb.save(path)
    return path


@pytest.fixture
def book(tmp_path):
    return build_workbook(
        tmp_path / "p.xlsx",
        holdings={"CALM": 50_000, "WILD": 50_000, "CASHX": 10_000},
        vols={"CALM": 0.01, "WILD": 0.04},
    )


def load(book):
    wb = openpyxl.load_workbook(book, data_only=True, read_only=True)
    return rs.build_report(rs.load_holdings(wb), rs.load_price_history(wb, min_weeks=20))


# ------------------------------------------------------------ parsing

def test_holdings_sum_across_accounts(tmp_path):
    p = build_workbook(tmp_path / "d.xlsx", {}, {"AAA": 0.02})
    wb = openpyxl.load_workbook(p)
    ws = wb["Asset PM"]
    for value in (1_000, 2_500):
        row = [None] * 12
        row[rs.HOLD_TICKER_COL] = "AAA"
        row[rs.HOLD_VALUE_COL] = value
        ws.append(row)
    wb.save(p)
    assert rs.load_holdings(openpyxl.load_workbook(p, data_only=True))["AAA"] == 3_500


def test_holdings_without_price_history_are_reported_not_sized(book):
    rep = load(book)
    assert "CASHX" in rep["no_history"]
    assert all(r["ticker"] != "CASHX" for r in rep["rows"])


def test_summary_sheets_are_not_mistaken_for_price_sheets(tmp_path):
    p = build_workbook(tmp_path / "s.xlsx", {"AAA": 1}, {"AAA": 0.02})
    wb = openpyxl.load_workbook(p)
    wb.create_sheet("HMM Data")
    wb.create_sheet("HMM Backtest")
    wb.save(p)
    assert set(rs.load_price_history(openpyxl.load_workbook(p, data_only=True),
                                     min_weeks=20)) == {"AAA"}


# ------------------------------------------------------------ the math

def test_volatility_is_annualized(tmp_path):
    p = build_workbook(tmp_path / "v.xlsx", {"AAA": 1}, {"AAA": 0.02})
    hist = rs.load_price_history(openpyxl.load_workbook(p, data_only=True), min_weeks=20)
    vol = rs.annualized_vol(hist["AAA"], window=13)
    assert vol == pytest.approx(0.02 * math.sqrt(52), rel=0.10)


def test_higher_volatility_gets_a_smaller_target_weight(book):
    rep = load(book)
    by = {r["ticker"]: r for r in rep["rows"]}
    assert by["WILD"]["vol"] > by["CALM"]["vol"]
    assert by["WILD"]["target_weight"] < by["CALM"]["target_weight"], (
        "sizing up into volatility — the sign is inverted"
    )


def test_target_weights_are_inverse_proportional_to_volatility(book):
    rep = load(book)
    by = {r["ticker"]: r for r in rep["rows"]}
    ratio = by["CALM"]["target_weight"] / by["WILD"]["target_weight"]
    assert ratio == pytest.approx(by["WILD"]["vol"] / by["CALM"]["vol"], rel=0.05)


def test_weights_and_risk_shares_each_sum_to_one(book):
    rep = load(book)
    assert sum(r["target_weight"] for r in rep["rows"]) == pytest.approx(1.0)
    assert sum(r["weight"] for r in rep["rows"]) == pytest.approx(1.0)
    assert sum(r["risk_share"] for r in rep["rows"]) == pytest.approx(1.0)


def test_equal_capital_in_unequal_vol_gives_unequal_risk(book):
    """The mismatch the tool exists to expose."""
    rep = load(book)
    by = {r["ticker"]: r for r in rep["rows"]}
    assert by["CALM"]["weight"] == pytest.approx(by["WILD"]["weight"])
    assert by["WILD"]["risk_share"] > 3 * by["CALM"]["risk_share"]


def test_trades_net_to_zero_and_move_toward_target(book):
    rep = load(book)
    assert sum(r["trade"] for r in rep["rows"]) == pytest.approx(0.0, abs=1e-6)
    for r in rep["rows"]:
        if abs(r["target_weight"] - r["weight"]) > 1e-9:
            assert (r["trade"] > 0) == (r["target_weight"] > r["weight"])


def test_rows_are_ordered_by_risk_share(book):
    shares = [r["risk_share"] for r in load(book)["rows"]]
    assert shares == sorted(shares, reverse=True)


def test_already_risk_balanced_book_needs_no_trades(tmp_path):
    """Capital already inverse to vol -> trades vanish."""
    p = build_workbook(tmp_path / "b.xlsx",
                       holdings={"CALM": 80_000, "WILD": 20_000},
                       vols={"CALM": 0.01, "WILD": 0.04})
    rep = load(p)
    for r in rep["rows"]:
        assert abs(r["trade"]) < 0.02 * rep["total"]


# ------------------------------------------------------------ output

def test_render_reports_the_top_concentration(book):
    text = rs.render(load(book))
    assert "WILD" in text
    assert "Largest risk concentration" in text
    assert "Sizing only" in text, "the no-forecast caveat must survive rendering"


def test_report_is_json_serializable(book):
    import json
    json.loads(json.dumps(load(book), default=str))
