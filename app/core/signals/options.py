# app/core/signals/options.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_unusual_options(symbol: str) -> dict:
    """Mock options flow (replace with CBOE API later)."""
    # Placeholder — upgrade to Unusual Whales/CBOE
    return {"symbol": symbol, "premium": 2800000, "strike": 140, "expiry": "2026-01-15"}