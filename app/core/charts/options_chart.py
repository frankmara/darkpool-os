# app/core/charts/options_chart.py
import matplotlib.pyplot as plt
import os
from datetime import datetime

def make_options_chart(symbol: str, options: dict) -> str:
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.patch.set_facecolor("#0a0a0a")
    ax.set_facecolor("#0a0a0a")

    ax.bar(["Premium"], [options.get("premium", 0)/1e6], color="#ff6600")
    ax.text(0, options.get("premium", 0)/1e6, f"${options.get('premium', 0)/1e6:.1f}M", ha="center", va="bottom", color="white")

    ax.set_title(f"{symbol} — Options Flow", color="white", fontsize=18, pad=30)
    ax.set_ylabel("Premium ($M)", color="#cccccc")

    footer = f"@DarkPoolData • {datetime.now().strftime('%b %d, %Y')}"
    fig.text(0.99, 0.01, footer, ha="right", fontsize=9, color="#666")

    os.makedirs("charts", exist_ok=True)
    path = f"charts/{symbol}_options.png"
    plt.savefig(path, dpi=320, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return path