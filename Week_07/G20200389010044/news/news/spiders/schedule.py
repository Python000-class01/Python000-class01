import time 
import os 
while True: 
    print("start to scrawling data:")
    os.system("python -m scrapy crawl sina_news") 
    print("scrawling done.")
    # 24 hours
    # time.sleep(3600*24)
    # test
    time.sleep(4)
