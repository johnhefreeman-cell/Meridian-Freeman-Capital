"""Offline tests for the EDGAR server's parsing and transform logic.

The sandbox this was authored in cannot reach sec.gov, so these drive the
code with recorded response shapes via httpx.MockTransport. They cover the
logic we own — CIK resolution, filing URL construction, XBRL shaping, HTML
stripping, paging — not SEC's availability.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import httpx
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mcp"))
import edgar_server as E  # noqa: E402


def unwrap(tool):
    """MCPServer wraps decorated functions; reach the callable underneath."""
    return getattr(tool, "fn", tool)


TICKERS = {
    "0": {"cik_str": 789019, "ticker": "MSFT", "title": "MICROSOFT CORP"},
    "1": {"cik_str": 320193, "ticker": "AAPL", "title": "Apple Inc."},
}

SUBMISSIONS = {
    "name": "MICROSOFT CORP",
    "tickers": ["MSFT"],
    "exchanges": ["Nasdaq"],
    "sic": "7372",
    "sicDescription": "Services-Prepackaged Software",
    "fiscalYearEnd": "0630",
    "filings": {
        "recent": {
            "form": ["10-K", "4", "10-Q", "8-K", "4"],
            "filingDate": ["2025-07-30", "2025-07-15", "2025-04-24",
                           "2025-04-24", "2024-11-01"],
            "reportDate": ["2025-06-30", "2025-07-11", "2025-03-31",
                           "2025-04-24", "2024-10-30"],
            "accessionNumber": ["0000950170-25-100000", "0000950170-25-090000",
                                "0000950170-25-050000", "0000950170-25-050001",
                                "0000950170-24-120000"],
            "primaryDocument": ["msft-20250630.htm", "xslF345X05/wk-form4.xml",
                                "msft-20250331.htm", "msft-8k.htm",
                                "xslF345X05/wk-form4b.xml"],
        }
    },
}

CONCEPT = {
    "label": "Revenue from Contract with Customer",
    "description": "Revenue recognized from contracts with customers.",
    "units": {
        "USD": [
            {"start": "2023-07-01", "end": "2024-06-30", "val": 245122000000,
             "fy": 2024, "fp": "FY", "form": "10-K", "filed": "2024-07-30",
             "accn": "0000950170-24-100000"},
            {"start": "2024-07-01", "end": "2025-06-30", "val": 270010000000,
             "fy": 2025, "fp": "FY", "form": "10-K", "filed": "2025-07-30",
             "accn": "0000950170-25-100000"},
        ]
    },
}

FILING_HTML = """<html><head><style>.x{color:red}</style>
<script>var a=1;</script></head><body>
<p>UNITED STATES SECURITIES AND EXCHANGE COMMISSION</p>
<p>Total revenue was &#36;270,010 million, an increase of 10&#37;.</p>
<table><tr><td>Segment</td><td>Revenue</td></tr></table>
</body></html>"""


def handler(request: httpx.Request) -> httpx.Response:
    url = str(request.url)
    assert request.headers["User-Agent"], "SEC requires a declared User-Agent"
    if "company_tickers.json" in url:
        return httpx.Response(200, json=TICKERS)
    if "/submissions/CIK0000789019.json" in url:
        return httpx.Response(200, json=SUBMISSIONS)
    if "/companyconcept/CIK0000789019/us-gaap/Revenues.json" in url:
        return httpx.Response(200, json=CONCEPT)
    if "/companyconcept/" in url and "/NotATag.json" in url:
        return httpx.Response(404, text="not found")
    if url.endswith("msft-20250630.htm"):
        return httpx.Response(
            200, text=FILING_HTML, headers={"content-type": "text/html"}
        )
    return httpx.Response(404, text=f"unmapped: {url}")


@pytest.fixture(autouse=True)
def offline_client(monkeypatch):
    monkeypatch.setattr(
        E, "_client",
        httpx.Client(transport=httpx.MockTransport(handler),
                     headers={"User-Agent": "test suite test@example.com"}),
    )
    monkeypatch.setattr(E, "_MIN_INTERVAL", 0.0)
    E._ticker_cache.clear()
    E._ticker_names.clear()
    yield


def test_resolves_ticker_to_zero_padded_cik():
    out = unwrap(E.lookup_cik)("msft")
    assert out["cik"] == "0000789019"
    assert out["name"] == "MICROSOFT CORP"


def test_accepts_bare_and_prefixed_cik():
    assert E._resolve_cik("789019") == "0000789019"
    assert E._resolve_cik("CIK0000789019") == "0000789019"


def test_unknown_ticker_raises_actionable_error():
    with pytest.raises(ValueError, match="No EDGAR CIK found"):
        unwrap(E.lookup_cik)("NOTATICKER")


def test_company_profile_surfaces_sic_and_fiscal_year_end():
    p = unwrap(E.company_profile)("MSFT")
    assert p["sic_description"] == "Services-Prepackaged Software"
    assert p["fiscal_year_end"] == "0630"


def test_list_filings_filters_by_form_and_builds_archive_url():
    out = unwrap(E.list_filings)("MSFT", form_type="10-K")
    assert out["count"] == 1
    f = out["filings"][0]
    assert f["form"] == "10-K"
    assert f["url"] == (
        "https://www.sec.gov/Archives/edgar/data/789019/"
        "000095017025100000/msft-20250630.htm"
    )
    assert f["filing_index"].endswith("0000950170-25-100000-index.htm")


def test_list_filings_accepts_multiple_forms_and_respects_limit():
    out = unwrap(E.list_filings)("MSFT", form_type="10-K,10-Q", limit=1)
    assert out["count"] == 1


def test_list_filings_since_excludes_older_filings():
    out = unwrap(E.list_filings)("MSFT", form_type="4", since="2025-01-01")
    assert [f["filed"] for f in out["filings"]] == ["2025-07-15"]


def test_insider_transactions_returns_only_ownership_forms():
    out = unwrap(E.insider_transactions)("MSFT")
    assert {f["form"] for f in out["filings"]} == {"4"}
    assert "P=open-market purchase" in out["note"]


def test_xbrl_concept_sorts_ascending_and_keeps_citation_fields():
    out = unwrap(E.xbrl_concept)("MSFT", "Revenues", limit=5)
    obs = out["observations"]
    assert [o["fiscal_year"] for o in obs] == [2024, 2025]
    assert obs[-1]["value"] == 270010000000
    assert obs[-1]["accession"] == "0000950170-25-100000"
    assert obs[-1]["form"] == "10-K"


def test_xbrl_concept_limit_keeps_most_recent():
    out = unwrap(E.xbrl_concept)("MSFT", "Revenues", limit=1)
    assert [o["fiscal_year"] for o in out["observations"]] == [2025]


def test_xbrl_concept_missing_tag_points_at_the_discovery_tool():
    with pytest.raises(ValueError, match="xbrl_available_concepts"):
        unwrap(E.xbrl_concept)("MSFT", "NotATag")


def test_xbrl_concept_wrong_unit_lists_available_units():
    with pytest.raises(ValueError, match="Available: \\['USD'\\]"):
        unwrap(E.xbrl_concept)("MSFT", "Revenues", unit="EUR")


def test_get_filing_text_strips_markup_and_unescapes_entities():
    url = unwrap(E.list_filings)("MSFT", form_type="10-K")["filings"][0]["url"]
    out = unwrap(E.get_filing_text)(url)
    assert "<p>" not in out["text"]
    assert "var a=1" not in out["text"]
    assert "color:red" not in out["text"]
    assert "$270,010 million, an increase of 10%." in out["text"]
    assert out["truncated"] is False


def test_get_filing_text_pages_with_offset():
    url = unwrap(E.list_filings)("MSFT", form_type="10-K")["filings"][0]["url"]
    first = unwrap(E.get_filing_text)(url, max_chars=20)
    assert first["truncated"] is True
    assert first["next_offset"] == 20
    second = unwrap(E.get_filing_text)(url, max_chars=20, offset=first["next_offset"])
    full = unwrap(E.get_filing_text)(url)
    assert full["text"].startswith(first["text"] + second["text"])


def test_get_filing_text_refuses_non_sec_hosts():
    with pytest.raises(ValueError, match="Only sec.gov URLs"):
        unwrap(E.get_filing_text)("https://example.com/10k.htm")


def test_all_tools_are_registered_with_descriptions():
    names = {
        "lookup_cik", "company_profile", "list_filings", "get_filing_text",
        "xbrl_concept", "xbrl_available_concepts", "insider_transactions",
        "full_text_search",
    }
    for n in names:
        tool = getattr(E, n)
        assert unwrap(tool).__doc__, f"{n} has no docstring for the model to read"
