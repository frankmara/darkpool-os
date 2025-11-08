# app/core/charts/darkpool_chart.py
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

def make_darkpool_chart(symbol: str, block: dict) -> str:
    df = pd.DataFrame([block])
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.patch.set_facecolor("#0a0a0a")
    ax.set_facecolor("#0a0a0a")

    ax.scatter(df["timestamp"], df["price"], s=df["size"]/800, c="#00ff88", alpha=0.8, edgecolors="white", linewidth=1.5)
    ax.text(df["timestamp"].iloc[0], df["price"].iloc[0], f" {block['size']:,.0f} @ ${block['price']}", color="white", fontsize=11, fontweight="bold", bbox=dict(facecolor="#00ff88", alpha=0.3, pad=5))

    ax.set_title(f"{symbol} — Dark Pool Block", color="white", fontsize=18, pad=30)
    ax.set_ylabel("Price ($)", color="#cccccc")
    ax.grid(True, axis="y", linestyle="--", alpha=0.3, color="#333")

    footer = f"@DarkPoolData • {datetime.now().strftime('%b %d, %Y')}"
    fig.text(0.99, 0.01, footer, ha="right", fontsize=9, color="#666")

    os.makedirs("charts", exist_ok=True)
    path = f"charts/{symbol}_darkpool.png"
    plt.savefig(path, dpi=320, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return path