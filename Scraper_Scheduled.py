import schedule
import time

from scraper import run_scraper
    

schedule.every(30).minutes.do(run_scraper)

while True:
    schedule.run_pending()
    time.sleep(60)