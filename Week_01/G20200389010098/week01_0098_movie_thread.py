import requests
import lxml.etree
from bs4 import BeautifulSoup as bs
from threading import Thread, current_thread, active_count, enumerate
from queue import Queue
import re
import os
import csv
from time import sleep
from fake_useragent import UserAgent
import time
import hashlib

#python的hash()，不能对字符串，所以用md5加密url作为缓存的key
#由于多并发读取，统一由写入队列消费，不能保证顺序，所以多读一个排名字段，供业务使用


class Douban():
    def __init__(self):
        pass
    #链接转key
    def md5_convert(self, string):
        m = hashlib.md5()
        m.update(string.encode())
        return m.hexdigest()
    #请求链接，若有缓存返回缓存
    def getHttp(self, url):
        # 缓存文件夹，多线程同时访问时可能都判断到不存在，并尝试创建
        dir = "cache"
        global dirExist
        if not dirExist:
            if not os.path.exists(dir):
                os.makedirs(dir)
            dirExist = True

        url_md5 = self.md5_convert(url)
        key = dir + "/" + url_md5

        if not os.path.exists(key):
            sleep(1)
            ua = UserAgent()
            headers = {
                'User-Agent': ua.random
            }
            # print(ua.random)
            res = requests.get(url, headers=headers)
            res.encoding = 'utf-8'
            if (res.status_code == 200):
                with open(key, "w+", newline='', encoding='utf-8-sig') as f:
                    f.write(res.text)
                    print(f"写入缓存{url}")
                    return res.text
                    #return bs(res.text, 'lxml')
            else:
                print("error")
                return False
        else:
            with open(key, encoding='utf-8-sig') as html:
                print(f"读取缓存{url}")
                return html.read()
                #return bs(html.read(), 'lxml')

    # 获取评论页最热5条
    def getComment(self, url):
        restext = self.getHttp(url + 'comments?sort=new_score&status=P')
        #bs_info=bs(restext, 'lxml')
        selector = lxml.etree.HTML(restext)
        #comment = [re.sub(r'\s+', '', x.text) for x in bs_info.find_all('span', {'class': 'short'}, limit=5)]
        comment = selector.xpath('//*[@class="short"]//text()')[0:5]
        return comment
    # 获取列表页数据
    def maker(self, url):
        # global num
        print(url)
        restext = self.getHttp(url)
        #bs_info = bs(restext, 'lxml')
        selector = lxml.etree.HTML(restext)

        #rank = [x.find("em").text for x in bs_info.find_all('div', {'class': 'pic'})]
        rank = selector.xpath('//*[@class="pic"]//em/text()')

        # title = [x.find('span', {'class': 'title'}).text for x in bs_info.find_all('div', {'class': 'hd'})]
        title = selector.xpath('//*[@class="hd"]//span[@class="title"][1]/text()')

        #href = [x.find('a').get('href') for x in bs_info.find_all('div', {'class': 'hd'})]
        href = selector.xpath('//*[@class="hd"]//a/@href')

        #star = [x.text for x in bs_info.find_all('span', {'class': 'rating_num'})]
        star = selector.xpath('//*[@class="rating_num"]/text()')

        # comment_num = [x.text[:-3] for x in bs_info.select("body div.star span:last-child")]
        # comment_num = [x.contents[7].text[:-3] for x in bs_info.find_all('div', {'class': 'star'})]
        comment_num = [x[:-3] for x in selector.xpath('//*[@class="star"]/span[4]/text()')]

        print('列表读取完毕')
        sum = []
        global queue
        for i in range(0, 25):
            comment_top5 = self.getComment(href[i])
            queue.put([title[i], star[i], comment_num[i],
                       comment_top5[0],
                       comment_top5[1],
                       comment_top5[2],
                       comment_top5[3],
                       comment_top5[4]])
            print(f'{title[i]}评论读取完毕')
        return True

# 生产数据，放入队列
class ProducerThread(Thread):
    def run(self):
        global pages
        dob = Douban()
        while True:
            url = pages.get()
            dob.maker(url)
            pages.task_done()
            if (pages.empty()):
                break

# 负责写入
class ConsumerTheard(Thread):
    def run(self):
        global queue
        with open("douban_movie250_t" + ".csv", "w+", newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['电影名', '评分', '短评数量', '评论1',
                             '评论2', '评论3', '评论4', '评论5', '排名'])
            while True:
                print(enumerate())
                if (active_count() < 3 and queue.empty()):
                    print(enumerate())
                    break
                item = queue.get()
                writer.writerow(item)
                queue.task_done()


if __name__ == '__main__':
    # 缓存文件夹不存在时，多个队列同时创建可能会造成冲突，用全局变量加锁
    dirExist = False
    #待采集链接队列
    pages = Queue(11)
    urls = tuple(
        [f'https://movie.douban.com/top250?start={str(x)}' for x in range(0, 226, 25)])
    # https://movie.douban.com/top250?start=
    # http://192.168.17.23/labs/douban/douban_
    # http://192.168.3.23/lab/movie/douban_
    for i in urls:
        pages.put(i)
    #待写入数据队列
    queue = Queue(35)

    p1 = ProducerThread(name='p1')
    p1.start()
    p2 = ProducerThread(name='p2')
    p2.start()
    p3 = ProducerThread(name='p3')
    p3.start()
    p4 = ProducerThread(name='p4')
    p4.start()
    p5 = ProducerThread(name='p5')
    p5.start()
    c1 = ConsumerTheard(name='c1')
    c1.start()
