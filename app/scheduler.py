# app/scheduler.py
import schedule
import time
from main import run_darkpool_v2

def job():
    run_darkpool_v2()

schedule.every(4).hours.do(job)  # Local test; Render handles cron

while True:
    schedule.run_pending()
    time.sleep(60)