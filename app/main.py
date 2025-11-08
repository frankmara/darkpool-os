# app/main.py
import random
from core.signals import darkpool, thirteenf, options, macro
from core.charts import darkpool_chart, ownership_chart, options_chart, macro_chart
from core.thread import generator
from core.poster import post_thread_with_image
from datetime import datetime
from datetime import time

SYMBOLS = ["NVDA", "TSLA", "AAPL", "MSFT"]
SIGNAL_TYPES = ["darkpool", "13f", "options", "macro"]

def run_darkpool_v2():
    print(f"DarkPool OS v2 — Running at {datetime.now().strftime('%H:%M:%S MST')}...")
    for _ in range(3):  # 3 threads/day
        symbol = random.choice(SYMBOLS)
        signal_type = random.choice(SIGNAL_TYPES)

        if signal_type == "darkpool":
            data = darkpool.get_darkpool_block(symbol)
            if not data:
                continue
            chart_path = darkpool_chart.make_darkpool_chart(symbol, data)
            thread = generator.generate_thread(signal_type, data)

        elif signal_type == "13f":
            data = thirteenf.get_13f_momentum(symbol)
            if not data:
                continue
            chart_path = ownership_chart.make_ownership_chart(symbol, data)
            thread = generator.generate_thread(signal_type, data)

        elif signal_type == "options":
            data = options.get_unusual_options(symbol)
            chart_path = options_chart.make_options_chart(symbol, data)
            thread = generator.generate_thread(signal_type, data)

        elif signal_type == "macro":
            data = macro.get_macro_signal()
            chart_path = macro_chart.make_macro_chart(data)
            thread = generator.generate_thread(signal_type, data)

        post_thread_with_image(thread, chart_path)
        time.sleep(60)  # Rate limit buffer

    print("V2 Cycle Complete.")

if __name__ == "__main__":
    run_darkpool_v2()