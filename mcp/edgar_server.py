"""SEC EDGAR MCP server.

Exposes EDGAR's public JSON APIs as MCP tools so diligence workflows read
primary sources directly instead of pasted text.

APIs used (all public, no key required):
  - https://www.sec.gov/files/company_tickers.json     ticker -> CIK
  - https://data.sec.gov/submissions/CIK##########.json filing history
  - https://data.sec.gov/api/xbrl/companyconcept/...    single XBRL concept
  - https://data.sec.gov/api/xbrl/companyfacts/...      all XBRL facts
  - https://efts.sec.gov/LATEST/search-index?q=...      full-text search

SEC requires a declared User-Agent with contact info and throttles above
10 requests/second. Set SEC_EDGAR_USER_AGENT="Name email@domain.com".
"""

from __future__ import annotations

import os
import threading
import time
from typing import Any

import httpx
from mcp.server.mcpserver import MCPServer

USER_AGENT = os.environ.get(
    "SEC_EDGAR_USER_AGENT", "Meridian Freeman Capital research@example.com"
)
TIMEOUT = float(os.environ.get("SEC_EDGAR_TIMEOUT", "30"))

mcp = MCPServer("edgar")

_client = httpx.Client(
    headers={
        "User-Agent": USER_AGENT,
        "Accept-Encoding": "gzip, deflate",
    },
    timeout=TIMEOUT,
    follow_redirects=True,
)

# SEC fair-access policy: stay under 10 req/s. Serialize with a min interval.
_MIN_INTERVAL = 0.12
_throttle_lock = threading.Lock()
_last_request = 0.0


def _get(url: str, **params: Any) -> httpx.Response:
    global _last_request
    with _throttle_lock:
        delta = time.monotonic() - _last_request
        if delta < _MIN_INTERVAL:
            time.sleep(_MIN_INTERVAL - delta)
        _last_request = time.monotonic()
    resp = _client.get(url, params=params or None)
    resp.raise_for_status()
    return resp


_ticker_cache: dict[str, str] = {}
_ticker_names: dict[str, str] = {}
_cache_lock = threading.Lock()


def _load_ticker_map() -> None:
    with _cache_lock:
        if _ticker_cache:
            return
        data = _get("https://www.sec.gov/files/company_tickers.json").json()
        for row in data.values():
            sym = str(row["ticker"]).upper()
            _ticker_cache[sym] = f"{int(row['cik_str']):010d}"
            _ticker_names[sym] = row["title"]


def _resolve_cik(ticker_or_cik: str) -> str:
    """Accept a ticker, a bare CIK, or a zero-padded CIK. Return 10-digit CIK."""
    raw = ticker_or_cik.strip().upper().removeprefix("CIK")
    if raw.isdigit():
        return f"{int(raw):010d}"
    _load_ticker_map()
    cik = _ticker_cache.get(raw)
    if cik is None:
        raise ValueError(
            f"No EDGAR CIK found for '{ticker_or_cik}'. "
            "Check the symbol, or pass the CIK directly."
        )
    return cik


@mcp.tool()
def lookup_cik(ticker: str) -> dict:
    """Resolve a ticker symbol to its SEC CIK and registrant name.

    Args:
        ticker: Exchange ticker, e.g. "MSFT".
    """
    cik = _resolve_cik(ticker)
    return {
        "ticker": ticker.upper(),
        "cik": cik,
        "name": _ticker_names.get(ticker.upper().strip()),
        "submissions_url": f"https://data.sec.gov/submissions/CIK{cik}.json",
    }


@mcp.tool()
def company_profile(ticker: str) -> dict:
    """Registrant profile: name, SIC industry, exchange, fiscal year end, address.

    Args:
        ticker: Ticker symbol or CIK.
    """
    cik = _resolve_cik(ticker)
    d = _get(f"https://data.sec.gov/submissions/CIK{cik}.json").json()
    return {
        "cik": cik,
        "name": d.get("name"),
        "tickers": d.get("tickers"),
        "exchanges": d.get("exchanges"),
        "sic": d.get("sic"),
        "sic_description": d.get("sicDescription"),
        "fiscal_year_end": d.get("fiscalYearEnd"),
        "entity_type": d.get("entityType"),
        "state_of_incorporation": d.get("stateOfIncorporation"),
        "business_address": d.get("addresses", {}).get("business"),
        "former_names": d.get("formerNames"),
    }


@mcp.tool()
def list_filings(
    ticker: str,
    form_type: str = "",
    limit: int = 20,
    since: str = "",
) -> dict:
    """List a registrant's filings, newest first, with direct document URLs.

    Args:
        ticker: Ticker symbol or CIK.
        form_type: Filter by form, e.g. "10-K", "10-Q", "8-K", "4", "DEF 14A".
            Comma-separate for several. Empty means all forms.
        limit: Maximum filings to return (default 20).
        since: Only filings on/after this ISO date, e.g. "2024-01-01".
    """
    cik = _resolve_cik(ticker)
    d = _get(f"https://data.sec.gov/submissions/CIK{cik}.json").json()
    recent = d.get("filings", {}).get("recent", {})

    wanted = {f.strip().upper() for f in form_type.split(",") if f.strip()}
    out = []
    for i, form in enumerate(recent.get("form", [])):
        if wanted and form.upper() not in wanted:
            continue
        filed = recent["filingDate"][i]
        if since and filed < since:
            continue
        accession = recent["accessionNumber"][i]
        acc_nodash = accession.replace("-", "")
        primary = recent["primaryDocument"][i]
        out.append(
            {
                "form": form,
                "filed": filed,
                "report_period": recent.get("reportDate", [""] * (i + 1))[i],
                "accession": accession,
                "primary_document": primary,
                "url": (
                    f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                    f"{acc_nodash}/{primary}"
                ),
                "filing_index": (
                    f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                    f"{acc_nodash}/{accession}-index.htm"
                ),
            }
        )
        if len(out) >= limit:
            break

    return {"cik": cik, "name": d.get("name"), "count": len(out), "filings": out}


@mcp.tool()
def get_filing_text(url: str, max_chars: int = 120_000, offset: int = 0) -> dict:
    """Fetch a filing document and return it as plain text.

    Use the `url` from list_filings. HTML is stripped to text. Long documents
    are paged — check `truncated` and call again with a higher `offset`.

    Args:
        url: Absolute sec.gov document URL.
        max_chars: Characters to return in this call.
        offset: Character offset to start from, for paging.
    """
    if "sec.gov" not in httpx.URL(url).host:
        raise ValueError("Only sec.gov URLs are allowed by this tool.")
    resp = _get(url)
    body = resp.text

    if "html" in resp.headers.get("content-type", "") or body.lstrip()[:1] == "<":
        import re
        body = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", body)
        body = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", body)
        body = re.sub(r"(?i)</t[dh]>", "\t", body)
        body = re.sub(r"(?s)<[^>]+>", " ", body)
        import html as _html
        body = _html.unescape(body)
        body = re.sub(r"[ \t]+", " ", body)
        body = re.sub(r"\n\s*\n\s*\n+", "\n\n", body).strip()

    chunk = body[offset : offset + max_chars]
    return {
        "url": url,
        "total_chars": len(body),
        "offset": offset,
        "returned_chars": len(chunk),
        "truncated": offset + len(chunk) < len(body),
        "next_offset": offset + len(chunk),
        "text": chunk,
    }


@mcp.tool()
def xbrl_concept(
    ticker: str,
    concept: str,
    taxonomy: str = "us-gaap",
    unit: str = "USD",
    limit: int = 24,
) -> dict:
    """Time series for one XBRL concept, as reported, with the source filing.

    Every point carries its accession number and fiscal period, so figures can
    be cited directly.

    Args:
        ticker: Ticker symbol or CIK.
        concept: XBRL tag, e.g. "Revenues", "NetIncomeLoss",
            "NetCashProvidedByUsedInOperatingActivities", "Assets".
        taxonomy: "us-gaap" (default), "ifrs-full", or "dei".
        unit: Unit key, e.g. "USD", "USD/shares", "shares".
        limit: Most recent N observations (default 24).
    """
    cik = _resolve_cik(ticker)
    url = (
        f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/"
        f"{taxonomy}/{concept}.json"
    )
    try:
        d = _get(url).json()
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 404:
            raise ValueError(
                f"Concept '{concept}' not reported by this filer under "
                f"'{taxonomy}'. Use xbrl_available_concepts to list valid tags."
            ) from exc
        raise

    points = d.get("units", {}).get(unit, [])
    if not points:
        raise ValueError(
            f"No data in unit '{unit}'. Available: {list(d.get('units', {}))}"
        )
    points = sorted(points, key=lambda p: (p.get("end", ""), p.get("filed", "")))
    tail = points[-limit:]
    return {
        "cik": cik,
        "concept": concept,
        "taxonomy": taxonomy,
        "label": d.get("label"),
        "description": d.get("description"),
        "unit": unit,
        "observations": [
            {
                "start": p.get("start"),
                "end": p.get("end"),
                "value": p.get("val"),
                "fiscal_year": p.get("fy"),
                "fiscal_period": p.get("fp"),
                "form": p.get("form"),
                "filed": p.get("filed"),
                "accession": p.get("accn"),
                "frame": p.get("frame"),
            }
            for p in tail
        ],
    }


@mcp.tool()
def xbrl_available_concepts(ticker: str, contains: str = "") -> dict:
    """List the XBRL tags a filer actually reports. Use before xbrl_concept.

    Args:
        ticker: Ticker symbol or CIK.
        contains: Case-insensitive substring filter, e.g. "revenue".
    """
    cik = _resolve_cik(ticker)
    d = _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json").json()
    needle = contains.lower()
    found = []
    for taxonomy, concepts in d.get("facts", {}).items():
        for tag, meta in concepts.items():
            if needle and needle not in tag.lower() and needle not in (
                meta.get("label") or ""
            ).lower():
                continue
            found.append(
                {
                    "taxonomy": taxonomy,
                    "concept": tag,
                    "label": meta.get("label"),
                    "units": list(meta.get("units", {})),
                }
            )
    found.sort(key=lambda r: (r["taxonomy"], r["concept"]))
    return {"cik": cik, "name": d.get("entityName"), "count": len(found),
            "concepts": found[:400]}


@mcp.tool()
def insider_transactions(ticker: str, since: str = "", limit: int = 40) -> dict:
    """Recent Form 3/4/5 insider filings with links to each document.

    Form 4 is the buy/sell signal referenced in the kill criteria. This returns
    the filing index; read individual documents with get_filing_text.

    Args:
        ticker: Ticker symbol or CIK.
        since: ISO date lower bound, e.g. "2025-03-01".
        limit: Maximum filings (default 40).
    """
    result = list_filings(ticker, form_type="3,4,5", limit=limit, since=since)
    result["note"] = (
        "Form 4 shows transaction code, share count and price inside the "
        "document. Codes: P=open-market purchase, S=open-market sale, "
        "A=grant/award, M=option exercise, F=shares withheld for tax, "
        "G=gift. Only P and S are discretionary market decisions."
    )
    return result


@mcp.tool()
def full_text_search(
    query: str, forms: str = "", date_from: str = "", date_to: str = "", limit: int = 20
) -> dict:
    """Search the full text of EDGAR filings (2001-present).

    Use for language diligence: find every filing containing a phrase such as
    "material weakness" or a named customer.

    Args:
        query: Search phrase. Wrap in double quotes for an exact phrase.
        forms: Comma-separated form filter, e.g. "10-K,10-Q".
        date_from: ISO start date.
        date_to: ISO end date.
        limit: Maximum hits (default 20).
    """
    params: dict[str, Any] = {"q": query}
    if forms:
        params["forms"] = forms
    if date_from:
        params["dateRange"] = "custom"
        params["startdt"] = date_from
    if date_to:
        params["dateRange"] = "custom"
        params["enddt"] = date_to

    d = _get("https://efts.sec.gov/LATEST/search-index", **params).json()
    hits = d.get("hits", {}).get("hits", [])[:limit]
    out = []
    for h in hits:
        src = h.get("_source", {})
        doc_id = h.get("_id", "")
        acc, _, doc = doc_id.partition(":")
        acc_nodash = acc.replace("-", "")
        ciks = src.get("ciks") or [""]
        out.append(
            {
                "company": (src.get("display_names") or [None])[0],
                "form": src.get("root_form") or src.get("file_type"),
                "filed": src.get("file_date"),
                "accession": acc,
                "url": (
                    f"https://www.sec.gov/Archives/edgar/data/"
                    f"{int(ciks[0]) if ciks[0] else ''}/{acc_nodash}/{doc}"
                ),
            }
        )
    return {
        "query": query,
        "total_hits": d.get("hits", {}).get("total", {}).get("value"),
        "returned": len(out),
        "results": out,
    }


if __name__ == "__main__":
    mcp.run()
