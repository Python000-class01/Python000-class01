'''
    爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

class DouBanSpider():
    def __init__(self):
        '''初始化URL和请求头'''
        self.base_url = "https://movie.douban.com/top250?start={}&filter="
        self.headers = [
            {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
            {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
            {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
            {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
            {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
                       ]
        self.proxies = [
            {'http':'120.83.110.244:9999'},
            {'http':'123.169.102.136:9999'},
            {'http':'163.204.245.133:9999'},
            {'http':'112.246.239.228:8060'},
            {'http':'113.65.249.78:8118'}
        ]
        self.data_list = []

    def get_all_url(self):
        '''获取所有URL'''
        url_list = []
        for i in range(0,250,25):
            url_list.append(self.base_url.format(i))

        return url_list

    def send_request(self, url):
        '''发送请求'''
        response = requests.get(url, headers=random.choice(self.headers), proxies=random.choice(self.proxies))
        data = response.text

        return data

    def parse_data(self, data):
        '''解析数据'''
        soup = BeautifulSoup(data, 'lxml')

        for tag in soup.find_all('div', attrs={'class':"hd"}):
            tag_data = self.send_request(tag.a.get('href'))
            tag_data_soup = BeautifulSoup(tag_data, 'lxml')
            title = tag_data_soup.find('span', attrs={'property':'v:itemreviewed'}).text.split(' ')[0]
            score = tag_data_soup.find('strong', attrs={'property':'v:average'}).text
            comment_nums = tag_data_soup.find('div', attrs={'class':'mod-hd'}).h2.span.a.text[3:-2]
            comment_list = []
            for i in tag_data_soup.find_all('div', attrs={'class':'comment'}):
                comment_list.append(i.p.span.text)
            self.data_list.append([title, score, comment_nums, comment_list])

    def save_data(self):
        '''保存数据'''
        df = pd.DataFrame(data=self.data_list, columns=['电影名称', '评分', '评分人数', '短评'])
        df.to_csv('douban.csv', index=False, encoding='utf-8')

    def start(self):
        '''统筹调用'''
        for url in self.get_all_url():
            data = self.send_request(url)
            self.parse_data(data)
            time.sleep(30)
        self.save_data()


DouBanSpider().start()