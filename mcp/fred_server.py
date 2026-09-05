"""FRED (St. Louis Fed) MCP server — macro series for cycle context.

Requires a free API key: https://fredaccount.stlouisfed.org/apikeys
Set FRED_API_KEY in the environment before use.

Per CLAUDE.md this fund does not underwrite macro theses. These series are
context for cyclicals and discount-rate sanity checks, not a thesis driver.
"""

from __future__ import annotations

import os
from typing import Any

import httpx
from mcp.server.mcpserver import MCPServer

BASE = "https://api.stlouisfed.org/fred"
mcp = MCPServer("fred")

COMMON_SERIES = {
    "DGS10": "10-Year Treasury constant maturity yield",
    "DGS2": "2-Year Treasury constant maturity yield",
    "FEDFUNDS": "Effective federal funds rate",
    "CPIAUCSL": "CPI, all urban consumers, SA",
    "CORESTICKM159SFRBATL": "Sticky-price core CPI, YoY",
    "UNRATE": "Unemployment rate",
    "PAYEMS": "Total nonfarm payrolls",
    "GDPC1": "Real GDP, chained 2017 dollars",
    "INDPRO": "Industrial production index",
    "UMCSENT": "University of Michigan consumer sentiment",
    "BAMLH0A0HYM2": "ICE BofA US high-yield option-adjusted spread",
    "T10Y2Y": "10Y minus 2Y Treasury spread",
    "HOUST": "Housing starts",
    "RSAFS": "Advance retail sales, total",
}


def _key() -> str:
    key = os.environ.get("FRED_API_KEY", "").strip()
    if not key:
        raise ValueError(
            "FRED_API_KEY is not set. Get a free key at "
            "https://fredaccount.stlouisfed.org/apikeys and export it."
        )
    return key


def _get(path: str, **params: Any) -> dict:
    params.update(api_key=_key(), file_type="json")
    resp = httpx.get(f"{BASE}/{path}", params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
def list_common_series() -> dict:
    """Curated FRED series IDs used in this fund's cycle work."""
    return {"series": COMMON_SERIES}


@mcp.tool()
def fred_search(query: str, limit: int = 15) -> dict:
    """Search FRED for a series ID by description.

    Args:
        query: Free-text search, e.g. "semiconductor shipments".
        limit: Maximum results (default 15).
    """
    d = _get("series/search", search_text=query, limit=limit)
    return {
        "query": query,
        "results": [
            {
                "id": s["id"],
                "title": s["title"],
                "frequency": s.get("frequency_short"),
                "units": s.get("units_short"),
                "seasonal_adjustment": s.get("seasonal_adjustment_short"),
                "last_updated": s.get("last_updated"),
                "observation_start": s.get("observation_start"),
                "observation_end": s.get("observation_end"),
            }
            for s in d.get("seriess", [])
        ],
    }


@mcp.tool()
def fred_series(
    series_id: str,
    start: str = "",
    end: str = "",
    units: str = "lin",
    frequency: str = "",
    limit: int = 120,
) -> dict:
    """Observations for a FRED series, oldest to newest.

    Args:
        series_id: FRED ID, e.g. "DGS10". See list_common_series.
        start: ISO start date.
        end: ISO end date.
        units: Transformation — "lin" (level), "chg", "pch" (% change),
            "pc1" (% change from a year ago).
        frequency: Optional resample, e.g. "m", "q", "a".
        limit: Most recent N observations (default 120).
    """
    params: dict[str, Any] = {"series_id": series_id, "units": units,
                              "sort_order": "desc", "limit": limit}
    if start:
        params["observation_start"] = start
    if end:
        params["observation_end"] = end
    if frequency:
        params["frequency"] = frequency

    meta = _get("series", series_id=series_id).get("seriess", [{}])[0]
    d = _get("series/observations", **params)
    obs = [
        {"date": o["date"], "value": None if o["value"] == "." else float(o["value"])}
        for o in d.get("observations", [])
    ]
    obs.reverse()
    return {
        "series_id": series_id,
        "title": meta.get("title"),
        "units": meta.get("units"),
        "frequency": meta.get("frequency"),
        "seasonal_adjustment": meta.get("seasonal_adjustment"),
        "last_updated": meta.get("last_updated"),
        "transformation": units,
        "observations": obs,
    }


if __name__ == "__main__":
    mcp.run()
