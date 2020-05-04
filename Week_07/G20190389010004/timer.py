import os
import time
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    os.system("scrapy crawl sinacomment")

if __name__ == '__main__':
    # 后台运行（非阻塞）
    # 生成一个名为“default”的MemoryJobStore和名为“default”的ThreadPoolExecutor的BackgroundScheduler，默认最大线程数为10
    scheduler = BackgroundScheduler()
    print("scheduler initialized")
    # 采用固定时间间隔方式，每10分钟执行一次
    scheduler.add_job(job, 'interval', minutes=10)    
    #独立线程
    scheduler.start()
    print("scheduler start in background")

    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()