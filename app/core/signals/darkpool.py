# app/core/signals/darkpool.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_darkpool_block(symbol: str, min_size: int = 500_000) -> dict:
    """Fetch latest dark pool block via Polygon ATS."""
    url = f"https://api.polygon.io/v3/reference/tickers/{symbol}/ats"
    params = {"apiKey": os.getenv("POLYGON_KEY"), "limit": 10, "sort": "timestamp"}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("results", [])
        blocks = [b for b in data if b.get("size", 0) >= min_size and b.get("price")]
        return blocks[0] if blocks else None
    except Exception as e:
        print(f"Dark pool fetch error: {e}")
        return None