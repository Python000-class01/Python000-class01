# 请在爬虫所在文件路径下执行

import os
import time

if __name__ == '__main__':

    while True:
        os.system("scrapy crawl jdbook")
        os.system("python3 /Users/lulu/Documents/GeekTime_PythonCamp/Homeworks/homework_week_7/JD_book_sentiment_analyais.py")
        # 每２个小时执行一次
        time.sleep(7200)