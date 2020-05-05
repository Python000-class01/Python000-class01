import time
import csv
import requests
from pprint import pprint
from lxml import html
etree = html.etree

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(myurl, headers=header)

class DouBanSpider():
    def __init__(self,max_page=5):
        self.base_url='https://movie.douban.com/top250?start={}&filter='
        self.headers={
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
        self.max_page=max_page
        self.list=[]

    def get_url_list(self):
        url_list=[]
        for page in range(0,self.max_page,25):
            url=self.base_url.format(page)
            url_list.append(url)

        return url_list

    def get_content(self,url):

        response=requests.get(url=url,
                              headers=self.headers)

        return response.content

    def get_items(self,content):
        text=content.decode('utf-8')
        htmlDiv = etree.HTML(text)
        target_list=htmlDiv.xpath('//div[@class="info"]')
        for target in target_list:
            # print(target)
            item={}
            item['titele']=target.xpath('//div[@class="hd"]/a/span[@classs="title"]/text()')
            item['rating_num']=target.xpath('span[@class="rating_num"]/text()')
            self.list.append(item)
        return self.list

    def save_items(self,items):
        with open('./0081.csv','w',encoding='utf-8') as f:
            csv_writer=csv.writer(f)
            for item in items:
                csv_writer.writerow(item.values())

    def main(self):
        # week04_0081_ex. 获取 url 列表
        url_list = self.get_url_list()

        for url in url_list:
            time.sleep(1)
            content = self.get_content(url)
            items=self.get_items(content)
            self.save_items(items)

if __name__ == '__main__':
    spider=DouBanSpider(max_page=1)
    spider.main()