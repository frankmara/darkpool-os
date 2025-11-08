# app/core/signals/thirteenf.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_13f_momentum(symbol: str) -> dict:
    """Fetch latest 13F ownership changes via FMP."""
    url = f"https://financialmodelingprep.com/api/v4/institutional-ownership/symbol-ownership-change?symbol={symbol}&apikey={os.getenv('FMP_KEY')}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if not data or not isinstance(data, list):
            return None
        top_change = max(data, key=lambda x: abs(x.get("change", 0)), default=None)
        return {"symbol": symbol, "investor": top_change.get("investor"), "change": top_change.get("change")} if top_change else None
    except Exception as e:
        print(f"13F fetch error: {e}")
        return None