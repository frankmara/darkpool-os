# app/core/signals/macro.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_macro_signal() -> dict:
    """Fetch macro indicator (mock Fed cut odds)."""
    # Placeholder — use FRED/NewsAPI later
    return {"indicator": "Fed Cut Odds", "value": 92, "change": "+14%"}