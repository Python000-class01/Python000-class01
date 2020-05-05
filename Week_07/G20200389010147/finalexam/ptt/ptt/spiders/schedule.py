from multiprocessing import Process
from scrapy import cmdline
import time
import logging


# 配置參數即可，爬蟲名稱，運行頻率，每天運行一次
confs = [
    {
        "spider_name": "ptt_gossiping",
        "frequency": 86400,
    },
]


def start_spider(spider_name, frequency):
    args = ["scrapy", "crawl", spider_name]
    while True:
        start = time.time()
        p = Process(target=cmdline.execute, args=(args,))
        p.start()
        p.join()
        logging.debug("### use time: %s" % (time.time() - start))
        time.sleep(frequency)


if __name__ == '__main__':
    for conf in confs:
        process = Process(target=start_spider,
                          args=(conf["spider_name"], conf["frequency"]))
        process.start()
        time.sleep(10)