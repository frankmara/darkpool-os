# app/core/charts/ownership_chart.py
import matplotlib.pyplot as plt
import os
from datetime import datetime

def make_ownership_chart(symbol: str, momentum: dict) -> str:
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.patch.set_facecolor("#0a0a0a")
    ax.set_facecolor("#0a0a0a")

    ax.bar(["Ownership Change"], [momentum.get("change", 0)], color="#00ccff")
    ax.text(0, momentum.get("change", 0), f"{momentum.get('change', 0):+.1f}%", ha="center", va="bottom", color="white")

    ax.set_title(f"{symbol} — 13F Momentum", color="white", fontsize=18, pad=30)
    ax.set_ylabel("% Change", color="#cccccc")

    footer = f"@DarkPoolData • {datetime.now().strftime('%b %d, %Y')}"
    fig.text(0.99, 0.01, footer, ha="right", fontsize=9, color="#666")

    os.makedirs("charts", exist_ok=True)
    path = f"charts/{symbol}_ownership.png"
    plt.savefig(path, dpi=320, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return path