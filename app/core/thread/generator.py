# app/core/thread/generator.py
def generate_thread(signal_type: str, data: dict) -> list:
    """Generate 5-tweet thread based on signal type."""
    symbol = data.get("symbol", "MACRO")
    if signal_type == "darkpool":
        size, price = data.get("size", 0), data.get("price", 0)
        vwap_diff = 12.0  # Mock for now
        return [
            f"1/5 ${symbol} — Dark Pool Block Alert\n• {size:,} shares @ ${price}\n• {vwap_diff:.1f}% below VWAP\n• Pre-market",
            f"2/5 Context\n• AI backlog: $30B+\n• Next catalyst: GTC 2026",
            f"3/5 Edge\n• Block = {size/1_500_000:.1f}x 10-min volume\n• Price +2.1% since",
            f"4/5 Risk\n• China export ban\n• RSI 78",
            f"5/5 Action\n• Long above ${price + 0.5}\n• Target: ${price + 15}\n• Stop: ${price - 5}\n@DarkPoolData"
        ]
    elif signal_type == "13f":
        change = data.get("change", 0)
        return [
            f"1/5 ${symbol} — 13F Momentum Alert\n• {data['investor']}: {change:+.1f}% change",
            f"2/5 Context\n• Ownership: {abs(change):.1f}% of float\n• Q3 earnings beat",
            f"3/5 Edge\n• Trend: {change:+.1f}% QoQ\n• Volume spike",
            f"4/5 Risk\n• Sector rotation\n• Overbought",
            f"5/5 Action\n• Watch for breakout\n• Target: +10%\n• Stop: -5%\n@DarkPoolData"
        ]
    elif signal_type == "options":
        premium = data.get("premium", 0) / 1e6
        return [
            f"1/5 ${symbol} — Options Flow Alert\n• ${premium:.1f}M premium\n• Strike: ${data['strike']}",
            f"2/5 Context\n• Implied volatility: 45%\n• Earnings next week",
            f"3/5 Edge\n• Paid 110% ask\n• High conviction",
            f"4/5 Risk\n• Gamma squeeze risk\n• Expiration",
            f"5/5 Action\n• Long calls\n• Target: +8%\n• Stop: -4%\n@DarkPoolData"
        ]
    elif signal_type == "macro":
        value = data.get("value", 0)
        return [
            f"1/5 Macro — {data['indicator']} Alert\n• {value}% probability",
            f"2/5 Context\n• Yield curve: Inverted\n• CPI: +0.1%",
            f"3/5 Edge\n• Trend: {data['change']}\n• Sector impact",
            f"4/5 Risk\n• Fed hawkishness\n• Recession odds",
            f"5/5 Action\n• Overweight tech\n• Hedge with bonds\n@DarkPoolData"
        ]
    return []