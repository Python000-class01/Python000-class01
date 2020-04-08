# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from doubanbook.items import DoubanbookItem
from lxml import etree

class DoubanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'douban'
    allowed_domains = ['book.douban.com']
    # 起始URL列表
    start_urls = ['http://book.douban.com/top250']


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 1):
            url = f'https://book.douban.com/subject/1084336/reviews?start={i*20}'
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        # ###debug
        # items = []
        selector = etree.HTML(response.text)
        IDs = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/div/@data-cid')
        for id in IDs:
            # 在items.py定义
            item = DoubanbookItem()
            full_review_url = 'https://book.douban.com/j/review/' + id + '/full'
            item['url'] = full_review_url
        #     ##debug
        #     items.append(item)
        # return items

            yield scrapy.Request(url=full_review_url, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        content = response.body.decode('utf-8')
        # soup = BeautifulSoup(response.text, 'html.parser')
        # content = soup.find('div', attrs={'class': 'intro'}).get_text().strip()
        item['content'] = content
        yield item
