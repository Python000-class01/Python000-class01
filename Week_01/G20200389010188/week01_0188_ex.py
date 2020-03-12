import requests
import queue
import threading
import time
#from bs4 import BeautifulSoup as bs
import lxml.etree
from fake_useragent import UserAgent 

ua = UserAgent()
#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

'''
抓取进程，将两个response，传递到resQ中，由解析进程进行解析
'''
class spider_handler(threading.Thread):
    def __init__(self, resQ):
        super().__init__()
        self.resQ = resQ

    def run(self):
        self.spider()

    def spider(self):
        urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))
        for url in urls:
            print(url)
            time.sleep(1)
            header = {}
            header['user-agent'] = ua.random
            res = s.get(url, headers=header)
            print(res)
            selector = lxml.etree.HTML(res.text)

            tags = selector.xpath('//*[@id="content"]/div/div[1]/ol')
            #遍历这个tag, 得到所有25个电影的信息
            tag_tree = lxml.etree.ElementTree(tags[0])

            for tag in tag_tree.iter(tag='li'):
                curl  = tag.xpath('./div/div[2]/div[1]/a/@href')[0] 
                title = tag.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
                rate  = tag.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
                cntComments = tag.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0]
                print(title, rate, cntComments, curl)
                reslist = [title, rate, cntComments, curl]
                self.resQ.put(reslist)
                


class parse_handler(threading.Thread):
    def __init__(self, resQ, movie_list):
        super().__init__()
        self.resQ = resQ
        self.movie_list = movie_list

    def run(self):
        self.parse()

    def parse(self):
        '''
        resQ里的每个元素是一个列表，存放2个元素，前是main的tag，后面是comments的response
        '''
        time.sleep(3)
        while True:
            time.sleep(1)
            if self.resQ.empty():
                print('parse_handler resQ is empty')
                break
            
            res_list = self.resQ.get()
            self.resQ.task_done()
            
            curl = res_list[3]
            cheader = {}
            cheader['user-agent'] = ua.random
            time.sleep(1)
            print(curl)
            cres = s.get(curl, headers=cheader)
            print(cres)
            cselector = lxml.etree.HTML(cres.text)
            comment_list = [cselector.xpath(f'//*[@id="hot-comments"]/div[{i}]/div/p/span/text()') for i in range(1,6,1)]
            
            data_list = [i for i in res_list[:3] ]
            data_list.extend(comment_list)
            print(data_list)
            self.movie_list.append(data_list)


if __name__ == '__main__':
    '''
    登录操作
    '''
    s = requests.Session()
    ## 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 期间使用 urllib3 的 connection pooling 功能。向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    form_data = {
    'ck':'',
    'name':'***', 
    'password':'***',
    'remember':'false',
    'ticket':''
    }
    lheader = {}
    lheader['user-agent'] = ua.random

    response = s.post(login_url, data = form_data, headers = lheader)

    resQ = queue.Queue()
    movie_list = []

    thread_list = []
    t1 = spider_handler(resQ)
    t1.start()
    thread_list.append(t1)

    t2 = parse_handler(resQ, movie_list)
    t2.start()
    thread_list.append(t2)

    for t in thread_list:
        t.join()
    
    '''
    print("main thread is about to end")
    print(movieDict)
    print("main thread ends")
    '''
    print("print movie_list...")
    print(movie_list)
    #保存成csv文件
    column = ['电影名', '评分', '评论数', '热门短评1', '热门短评2', '热门短评3', '热门短评4', '热门短评5']
    import pandas as pd
    book1 = pd.DataFrame(columns=column, data=movie_list)
    book1.to_csv('D:\\Work\\Python\\PythonCampus\\课程\\1st_0209\\douban_movie.csv', encoding='utf-8')
    book1.to_excel('D:\\Work\\Python\\PythonCampus\\课程\\1st_0209\\douban_movie.xlsx', encoding='gbk')




