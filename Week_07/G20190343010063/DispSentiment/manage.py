
from app import app, db
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from NewsSpider.spiders.HotMovie import HotmovieSpider
from common.NlpProcess import NewsCommentNlpProcess
import time, os
from multiprocessing import Process


# 定时爬虫任务
def spider_task():
    process = CrawlerProcess(get_project_settings())
    process.crawl(HotmovieSpider)
    process.start()


def crawl_in_loop(time_loop_seconds):
    while True:
        print('#' * 50)
        print(f'spider running in loop {time_loop_seconds} seconds， pid is {os.getpid()}, ppid is {os.getppid()}')
        print('#' * 50)
        spider = Process(target=spider_task)
        spider.start()
        spider.join()

        for i in range(max(30, time_loop_seconds)):
            time.sleep(1)
            print('spider sleeping')

# flask web后台任务
def flask_app_task():
    print('#' * 50)
    print(f'flask app running, pid is {os.getpid()}, ppid is {os.getppid()}')
    print('#' * 50)
    app.secret_key = 'key'
    app.run()

    return 0

# 定时nlp分析任务
def nlp_task(time_loop_seconds):
    while True:
        print('#' * 50)
        print(f'nlp running in loop {time_loop_seconds} seconds, pid is {os.getpid()}, ppid is {os.getppid()}')
        print('#' * 50)

        nlp = NewsCommentNlpProcess()
        nlp.nlp_all_db_data()

        time.sleep(max(60, time_loop_seconds))

if __name__ == "__main__":
    # 创建三个服务进程
    spider = Process(target=crawl_in_loop, args=(30,))
    spider.start()
    nlp = Process(target=nlp_task, args=(60,))
    nlp.start()
    flask_app = Process(target=flask_app_task)
    flask_app.start()


    spider.join()
    nlp.join()
    flask_app.join()




