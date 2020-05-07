# -*- coding: utf-8 -*-
import scrapy
from sinanews.items import SinanewsItem
import json


class SinanewsSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'sinanews'
    allowed_domains = ['comment.news.sina.com.cn']
    # 起始URL列表
    start_urls = ['http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-irczymi9667485&group=0&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user']
    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    
    def start_requests(self):
        urls = tuple(f'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-irczymi9667485&group=0&compress=0&ie=utf-8&oe=utf-8&page={ i + 1 }&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user' for i in range(10))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        res = json.loads(response.text)

        for i in range(len(res['result']['cmntlist'])):
            item = SinanewsItem()
            user = res['result']['cmntlist'][i]['nick']
            short = res['result']['cmntlist'][i]['content']
            timestamp = res['result']['cmntlist'][i]['time']
            item['user'] = user
            item['short'] = short
            item['timestamp'] = timestamp
            yield item
