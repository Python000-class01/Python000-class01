import requests
import queue
import threading
import time
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent 

ua = UserAgent()
user_agent = ua.random
header = {}
header['user-agent'] = user_agent

class spider_main_handle(threading.Thread):
    def __init__(self, urlQ, resQ):
        super().__init__()
        self.urlQ = urlQ
        self.resQ = resQ

    def run(self):
        self.spider()

    '''
    抓取URL，response放相应的Queue里
    '''
    def spider(self):
        urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))
        for url in urls:
            response = requests.get(url, headers=header)
            #print("threading spider_main_handle, response=%s",response)
            self.resQ.put(response.text)


class parse_main_handler(threading.Thread):
    def __init__(self, resQ, dataQ, comments_urlQ):
        super().__init__()
        self.resQ = resQ
        self.dataQ = dataQ
        self.comments_urlQ = comments_urlQ

    def run(self):
        self.parse()

    '''
    解析title, rate, count of comments, 以及将评论的url放入队列
    '''
    def parse(self):   
        
        while True:
            time.sleep(1)
            if self.resQ.empty():
                break
            response = self.resQ.get()
            bs_info = bs(response, 'html.parser')

            for item in bs_info.find_all('div',attrs={'class':'info'}):
                eburl = item.find('a').get('href')
                title = item.find('span',attrs={'class':'title'}).text
                rate  = item.find('span',attrs={'class':'rating_num'}).text
                cntComments = item.find('div',attrs={'class':'star'}).contents[7].text
                self.comments_urlQ.put(eburl)
                #print("threading parse_main_handler, eburl=%s",eburl)
                self.dataQ.put(title)
                self.dataQ.put(rate)
                self.dataQ.put(cntComments)

class spider_comments_handle(threading.Thread):
    def __init__(self, comments_urlQ, comments_resQ):
        super().__init__()
        self.comments_urlQ = comments_urlQ
        self.comments_resQ = comments_resQ

    def run(self):
        self.spider()

    '''
    抓取URL，response放相应的Queue里
    '''
    def spider(self):
        #print("spider_comments_handle spider run...")
        time.sleep(3)
        while True:
            time.sleep(1)
            if self.comments_urlQ.empty():
                #print("spider_comments_handle comments_urlQ is empty")
                break
            
            url = self.comments_urlQ.get()
            #print("spider_comments_handle comments_urlQ =", url)
            response = requests.get(url, headers=header)
            #print("threading spider_comments_handle, response=%s",response)
            self.comments_resQ.put(response.text)

class parse_comments_handler(threading.Thread):
    def __init__(self, comments_resQ, comments_dataQ):
        super().__init__()
        self.comments_resQ = comments_resQ
        self.comments_dataQ = comments_dataQ

    def run(self):
        self.parse()

    '''
    解析热评
    '''
    def parse(self):
        time.sleep(10)
        while True:
            time.sleep(3)
            if self.comments_resQ.empty():
                print("parse_comments_handler comments_urlQ is empty")
                break

            response = self.comments_resQ.get()          
            bs_info = bs(response, 'html.parser')

            for i in range(5):
                commentss = bs_info.find('span',attrs={'class':'short'}).text + '\n'
            print("threading parse_comments_handler, comment=%s",commentss)
            self.comments_dataQ.put(commentss)

if __name__ == '__main__':
    urlQ = queue.Queue()
    resQ = queue.Queue()
    dataQ = queue.Queue()
    comments_urlQ = queue.Queue()
    comments_resQ = queue.Queue()
    comments_dataQ = queue.Queue()

    thread_list = []
    t1 = spider_main_handle(urlQ, resQ)
    t1.start()
    thread_list.append(t1)

    t2 = parse_main_handler(resQ, dataQ, comments_urlQ)
    t2.daemon = True
    t2.start()
    thread_list.append(t2)

    t3 = spider_comments_handle(comments_urlQ, comments_resQ)
    t3.daemon = True
    t3.start()
    thread_list.append(t3)

    t4 = parse_comments_handler(comments_resQ, comments_dataQ)
    t4.daemon = True
    t4.start()
    thread_list.append(t4)

    for t in thread_list:
        t.join()

    
    while not dataQ.empty():
        print (dataQ.get())
    
    while not comments_dataQ.empty():
        print (comments_dataQ.get())









    

