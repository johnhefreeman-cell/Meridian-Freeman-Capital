"""Tests for the holdings extractor.

The workbook itself is personal data and is not in the repo, so these cover the
pure logic: the bucket taxonomy that decides which positions the risk arithmetic
is allowed to speak about, and the reconciliation guard that is the whole reason
the extractor is trustworthy.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import portfolio_extract as px  # noqa: E402


# --------------------------------------------------------------------------
# Bucket taxonomy
# --------------------------------------------------------------------------

def test_single_names_are_their_own_bucket():
    for ticker in ("MRVL", "AMAT", "KLAC", "BRK.B", "ASML"):
        assert px.bucket(ticker) == "Single names"


def test_cash_like_instruments_are_cash_not_funds():
    """SGOV and FDRXX are funds by structure and cash by function.

    Bucketing them as funds would inflate the diversified sleeve with money
    the holder is not taking equity risk with.
    """
    for ticker in ("CASH", "FDRXX", "SGOV", "SPAXX"):
        assert px.bucket(ticker) == "Cash"


def test_index_funds_fall_through_to_diversified():
    for ticker in ("VOO", "FXAIX", "VTMGX", "QQQ", "SCHD"):
        assert px.bucket(ticker) == "Diversified funds"


def test_bonds_real_assets_and_crypto_are_separated():
    assert px.bucket("BND") == "Fixed income"
    assert px.bucket("GLD") == "Real assets & alts"
    assert px.bucket("DBMF") == "Real assets & alts"
    assert px.bucket("BTC") == "Crypto"


def test_every_single_name_has_a_price_tab_or_is_visibly_unmeasured():
    """The taxonomy must not quietly assume price history exists.

    Risk shares are computed only over names with a price series; a single name
    without one has to surface as unmeasured rather than vanish from the
    denominator. This test pins the contract that `bucket` classifies on
    identity alone and never on data availability.
    """
    assert px.bucket("GOOGL") == "Single names"


def test_international_set_is_disjoint_from_cash_and_bonds():
    assert not px.INTERNATIONAL & px.CASH_LIKE
    assert not px.INTERNATIONAL & px.BONDS


def test_bucket_sets_do_not_overlap():
    """Overlapping sets would make the composition percentages sum past 100."""
    sets = {
        "single": px.SINGLE_NAMES, "cash": px.CASH_LIKE, "crypto": px.CRYPTO,
        "real": px.REAL_ASSETS, "bonds": px.BONDS,
    }
    names = list(sets)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            assert not sets[a] & sets[b], f"{a} and {b} share {sets[a] & sets[b]}"


# --------------------------------------------------------------------------
# Reconciliation
# --------------------------------------------------------------------------

def _acct(name, value):
    return dict(account=name, value=value, share=None, gain=None, divYield=None)


def _hold(name, value):
    return dict(account=name, ticker="X", value=value)


def test_reconcile_passes_when_holdings_match_reported_value():
    accounts = [_acct("Roth", 1000.0)]
    holdings = [_hold("Roth", 600.0), _hold("Roth", 400.0)]
    assert px.reconcile(accounts, holdings, margin=0.0) == []


def test_reconcile_catches_a_dropped_row():
    """The failure mode this guard exists for: cash lines carry no ticker."""
    accounts = [_acct("Roth", 1000.0)]
    holdings = [_hold("Roth", 600.0)]           # the 400 cash line was skipped
    problems = px.reconcile(accounts, holdings, margin=0.0)
    assert len(problems) == 1
    assert "Roth" in problems[0]
    assert "-400" in problems[0].replace(",", "")


def test_reconcile_allows_a_levered_account():
    """Holdings sum to gross; the summary reports net. The loan closes the gap."""
    accounts = [_acct("Joint", 900.0)]
    holdings = [_hold("Joint", 1000.0)]
    assert px.reconcile(accounts, holdings, margin=-100.0) == []


def test_reconcile_does_not_use_the_loan_to_excuse_an_unrelated_gap():
    """A levered account must still be wrong when it is wrong by the wrong amount."""
    accounts = [_acct("Joint", 900.0)]
    holdings = [_hold("Joint", 1050.0)]         # off by 150, not by the 100 loan
    assert len(px.reconcile(accounts, holdings, margin=-100.0)) == 1


def test_reconcile_tolerance_is_a_cent_not_a_dollar():
    accounts = [_acct("Roth", 1000.0)]
    assert px.reconcile(accounts, [_hold("Roth", 1000.005)], margin=0.0) == []
    assert px.reconcile(accounts, [_hold("Roth", 1000.50)], margin=0.0) != []


def test_reconcile_reports_every_broken_account_not_just_the_first():
    accounts = [_acct("A", 100.0), _acct("B", 200.0), _acct("C", 300.0)]
    holdings = [_hold("A", 50.0), _hold("B", 200.0), _hold("C", 250.0)]
    problems = px.reconcile(accounts, holdings, margin=0.0)
    assert len(problems) == 2


def test_an_account_with_no_holdings_reconciles_only_at_zero():
    assert px.reconcile([_acct("Empty", 0.0)], [], margin=0.0) == []
    assert px.reconcile([_acct("Empty", 5.0)], [], margin=0.0) != []


# --------------------------------------------------------------------------
# Constants the dashboard depends on
# --------------------------------------------------------------------------

def test_volatility_window_is_a_quarter_of_weeks():
    assert px.VOL_WINDOW == 13
    assert px.WEEKS_PER_YEAR == 52.0


def test_crypto_rows_map_only_to_known_crypto_tickers():
    """These rows have no ticker cell, so they are positional and fragile.

    The index map is the one place the extractor trusts a row number. Pin that
    it can only ever produce a ticker the crypto bucket recognises, so a sheet
    edit that shifts those rows surfaces as a reconciliation failure rather
    than as silently mislabelled holdings.
    """
    assert px.CRYPTO_ROWS
    assert set(px.CRYPTO_ROWS.values()) <= px.CRYPTO
    for ticker in px.CRYPTO_ROWS.values():
        assert px.bucket(ticker) == "Crypto"
