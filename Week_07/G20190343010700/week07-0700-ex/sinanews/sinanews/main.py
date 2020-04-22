'''
设置爬虫的自动运行时间间隔为24小时 
'''

import time
import os

while True:
    os.system("scrapy crawl news")
    time.sleep(86400)