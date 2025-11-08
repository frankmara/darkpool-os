# app/core/charts/macro_chart.py
import matplotlib.pyplot as plt
import os
from datetime import datetime

def make_macro_chart(macro: dict) -> str:
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.patch.set_facecolor("#0a0a0a")
    ax.set_facecolor("#0a0a0a")

    ax.bar(["Fed Cut Odds"], [macro.get("value", 0)], color="#cc00ff")
    ax.text(0, macro.get("value", 0), f"{macro.get('value', 0)}%", ha="center", va="bottom", color="white")

    ax.set_title("Macro — Fed Cut Odds", color="white", fontsize=18, pad=30)
    ax.set_ylabel("% Probability", color="#cccccc")

    footer = f"@DarkPoolData • {datetime.now().strftime('%b %d, %Y')}"
    fig.text(0.99, 0.01, footer, ha="right", fontsize=9, color="#666")

    os.makedirs("charts", exist_ok=True)
    path = f"charts/macro_fed.png"
    plt.savefig(path, dpi=320, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return path