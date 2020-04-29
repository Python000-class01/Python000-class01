import os
import time
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    os.system("scrapy crawl sina_comment")


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', minutes=10)
    scheduler.start()

    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
