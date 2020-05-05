import re
import csv
import gevent
from gevent.queue import Queue
from lxml import etree
import lxml
from gevent import monkey

monkey.patch_all()
# 让程序变成异步模式

import requests

work = Queue()
# 创建队列对象并赋值给work

url_1 = 'https://book.douban.com/subject/3369600/reviews?start={num}'
# 选取《当我谈跑步时我谈些什么》这本书作为书评爬取对象，一共有99页，先取前50页作为测试

for i in range(50):
    real_url = url_1.format(num=i)
    work.put_nowait(real_url)

def crawler():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    while not work.empty():
        # 当队列非空的时候，就执行下面的程序
        url = work.get_nowait()
        # 从队列里取出url
        text = requests.get(url_1, headers=headers).text

        html = etree.HTML(text)
        comments = html.xpath('//div[@class="short-content"]/text()')
        useless = [')\n                    ', '\n                            ']

        new_comments = [''.join(re.findall(u'([\u4e00-\u9fa5]+)', comment)) \
            for comment in comments if comment not in useless]
        recommends = html.xpath('//header[@class="main-hd"]/span[1]/@title')
        for i in range(len(recommends)):
            writer.writerow([recommends[i], new_comments[i]])


csv_file = open(r'./book.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)

tasks_list = []

for x in range(5):
    task = gevent.spawn(crawler)
    tasks_list.append(task)

gevent.joinall(tasks_list)

csv_file.close() 