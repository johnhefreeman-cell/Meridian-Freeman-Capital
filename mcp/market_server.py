"""Market data MCP server — prices, multiples, consensus.

Backed by yfinance. This is a *secondary* source: per CLAUDE.md §7 every
figure that reaches a memo must be tied back to a filing. Use this for
multiples, price context, and consensus (which has no filing equivalent),
then verify the underlying fundamentals against EDGAR.
"""

from __future__ import annotations

from typing import Any

import yfinance as yf
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("market")


def _clean(value: Any) -> Any:
    """Make pandas/NumPy scalars JSON-safe."""
    if value is None:
        return None
    if hasattr(value, "item"):
        try:
            value = value.item()
        except (ValueError, AttributeError):
            return str(value)
    if isinstance(value, float) and value != value:  # NaN
        return None
    return value


def _pick(info: dict, *keys: str) -> Any:
    for k in keys:
        if info.get(k) is not None:
            return _clean(info[k])
    return None


def _snapshot(ticker: str) -> dict:
    t = yf.Ticker(ticker)
    info = t.info or {}
    ev = _pick(info, "enterpriseValue")
    rev = _pick(info, "totalRevenue")
    ebitda = _pick(info, "ebitda")
    gp = _pick(info, "grossProfits")

    return {
        "ticker": ticker.upper(),
        "name": _pick(info, "longName", "shortName"),
        "sector": _pick(info, "sector"),
        "industry": _pick(info, "industry"),
        "price": _pick(info, "currentPrice", "regularMarketPrice"),
        "currency": _pick(info, "currency"),
        "market_cap": _pick(info, "marketCap"),
        "enterprise_value": ev,
        "shares_out": _pick(info, "sharesOutstanding"),
        "total_cash": _pick(info, "totalCash"),
        "total_debt": _pick(info, "totalDebt"),
        "ttm_revenue": rev,
        "revenue_growth_yoy": _pick(info, "revenueGrowth"),
        "gross_margin": (
            _pick(info, "grossMargins")
            or (gp / rev if gp and rev else None)
        ),
        "ebitda_ttm": ebitda,
        "ebitda_margin": _pick(info, "ebitdaMargins"),
        "operating_margin": _pick(info, "operatingMargins"),
        "fcf_ttm": _pick(info, "freeCashflow"),
        "net_debt_to_ebitda": (
            ((_pick(info, "totalDebt") or 0) - (_pick(info, "totalCash") or 0)) / ebitda
            if ebitda else None
        ),
        "ev_to_revenue": (ev / rev if ev and rev else None),
        "ev_to_ebitda": (ev / ebitda if ev and ebitda else None),
        "pe_trailing": _pick(info, "trailingPE"),
        "pe_forward": _pick(info, "forwardPE"),
        "roe": _pick(info, "returnOnEquity"),
        "roa": _pick(info, "returnOnAssets"),
        "insider_pct_held": _pick(info, "heldPercentInsiders"),
        "institution_pct_held": _pick(info, "heldPercentInstitutions"),
        "short_pct_float": _pick(info, "shortPercentOfFloat"),
        "week52_high": _pick(info, "fiftyTwoWeekHigh"),
        "week52_low": _pick(info, "fiftyTwoWeekLow"),
    }


@mcp.tool()
def quote(ticker: str) -> dict:
    """Full snapshot for one ticker: price, multiples, margins, leverage, ownership.

    Args:
        ticker: Exchange ticker, e.g. "MSFT".
    """
    return _snapshot(ticker)


@mcp.tool()
def comps_table(tickers: str) -> dict:
    """Side-by-side comp table for several tickers. Backs the /comps skill.

    Returns the fields CLAUDE.md §5 asks for: EV/Revenue, EV/EBITDA, P/E,
    growth, margins, and Rule of 40 for software names.

    Args:
        tickers: Comma-separated symbols, e.g. "MSFT,ADBE,CRM,NOW".
    """
    symbols = [s.strip().upper() for s in tickers.split(",") if s.strip()]
    if not symbols:
        raise ValueError("Pass at least one ticker.")
    if len(symbols) > 15:
        raise ValueError("Cap of 15 tickers per call; split the request.")

    rows, errors = [], {}
    for sym in symbols:
        try:
            row = _snapshot(sym)
            growth = row.get("revenue_growth_yoy")
            margin = row.get("fcf_ttm")
            rev = row.get("ttm_revenue")
            fcf_margin = (margin / rev) if margin and rev else None
            row["fcf_margin"] = fcf_margin
            row["rule_of_40"] = (
                (growth + fcf_margin) * 100
                if growth is not None and fcf_margin is not None
                else None
            )
            rows.append(row)
        except Exception as exc:  # one bad symbol must not kill the table
            errors[sym] = str(exc)

    def _median(field: str) -> float | None:
        vals = sorted(r[field] for r in rows if r.get(field) is not None)
        if not vals:
            return None
        mid = len(vals) // 2
        return vals[mid] if len(vals) % 2 else (vals[mid - 1] + vals[mid]) / 2

    return {
        "rows": rows,
        "medians": {
            f: _median(f)
            for f in (
                "ev_to_revenue", "ev_to_ebitda", "pe_forward",
                "revenue_growth_yoy", "gross_margin", "ebitda_margin",
                "fcf_margin", "rule_of_40", "net_debt_to_ebitda",
            )
        },
        "errors": errors,
        "source": "yfinance (secondary). Verify fundamentals against EDGAR.",
    }


@mcp.tool()
def price_history(ticker: str, period: str = "2y", interval: str = "1wk") -> dict:
    """OHLCV history, for drawdown and entry-point context.

    Args:
        ticker: Ticker symbol.
        period: "1mo","3mo","6mo","1y","2y","5y","10y","max".
        interval: "1d","1wk","1mo".
    """
    hist = yf.Ticker(ticker).history(period=period, interval=interval)
    if hist.empty:
        raise ValueError(f"No price history returned for '{ticker}'.")
    bars = [
        {
            "date": idx.strftime("%Y-%m-%d"),
            "open": _clean(row.Open),
            "high": _clean(row.High),
            "low": _clean(row.Low),
            "close": _clean(row.Close),
            "volume": _clean(row.Volume),
        }
        for idx, row in hist.iterrows()
    ]
    closes = [b["close"] for b in bars if b["close"] is not None]
    peak = max(closes) if closes else None
    return {
        "ticker": ticker.upper(),
        "period": period,
        "interval": interval,
        "bars": bars,
        "last_close": closes[-1] if closes else None,
        "period_high": peak,
        "drawdown_from_period_high": (
            closes[-1] / peak - 1 if closes and peak else None
        ),
    }


@mcp.tool()
def consensus(ticker: str) -> dict:
    """Sell-side consensus: price targets, revenue and EPS estimates.

    This is the input to the variant-perception section (CLAUDE.md §6.5) —
    what we must disagree with to have a thesis.

    Args:
        ticker: Ticker symbol.
    """
    t = yf.Ticker(ticker)
    out: dict[str, Any] = {"ticker": ticker.upper()}

    info = t.info or {}
    out["targets"] = {
        "mean": _pick(info, "targetMeanPrice"),
        "high": _pick(info, "targetHighPrice"),
        "low": _pick(info, "targetLowPrice"),
        "analyst_count": _pick(info, "numberOfAnalystOpinions"),
        "recommendation": _pick(info, "recommendationKey"),
    }

    for label, attr in (
        ("revenue_estimate", "revenue_estimate"),
        ("earnings_estimate", "earnings_estimate"),
        ("eps_revisions", "eps_revisions"),
        ("growth_estimates", "growth_estimates"),
    ):
        try:
            frame = getattr(t, attr, None)
            if frame is not None and not frame.empty:
                out[label] = {
                    str(idx): {str(c): _clean(frame.loc[idx, c]) for c in frame.columns}
                    for idx in frame.index
                }
        except Exception as exc:
            out[label] = f"unavailable: {exc}"

    out["source"] = "yfinance (secondary). Consensus has no filing equivalent."
    return out


@mcp.tool()
def financial_statements(ticker: str, statement: str = "income", quarterly: bool = False) -> dict:
    """Standardized financial statements, for a fast read before EDGAR.

    Args:
        ticker: Ticker symbol.
        statement: "income", "balance", or "cashflow".
        quarterly: True for quarterly periods, False for annual.
    """
    t = yf.Ticker(ticker)
    attr = {
        ("income", False): "income_stmt",
        ("income", True): "quarterly_income_stmt",
        ("balance", False): "balance_sheet",
        ("balance", True): "quarterly_balance_sheet",
        ("cashflow", False): "cashflow",
        ("cashflow", True): "quarterly_cashflow",
    }.get((statement, quarterly))
    if attr is None:
        raise ValueError('statement must be "income", "balance", or "cashflow".')

    frame = getattr(t, attr)
    if frame is None or frame.empty:
        raise ValueError(f"No {statement} statement available for '{ticker}'.")

    return {
        "ticker": ticker.upper(),
        "statement": statement,
        "periodicity": "quarterly" if quarterly else "annual",
        "periods": [str(c.date()) if hasattr(c, "date") else str(c) for c in frame.columns],
        "line_items": {
            str(idx): [_clean(frame.loc[idx, c]) for c in frame.columns]
            for idx in frame.index
        },
        "source": "yfinance (secondary). Tie every memo figure back to EDGAR.",
    }


if __name__ == "__main__":
    mcp.run()
