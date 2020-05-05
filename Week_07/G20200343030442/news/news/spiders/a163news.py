# -*- coding: utf-8 -*-
import scrapy
import sys 
import io
from news.items import NewsItem
from scrapy.selector import Selector
import json
import scrapy.http
import codecs
import jsonpath
import os

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer ,encoding = 'utf-8')

class A163newsSpider(scrapy.Spider):
    name = '163news'
    allowed_domains = ['news.163.com','comment.tie.163.com', 'dy.163.com', 'comment.api.163.com']
    start_urls = ['http://news.163.com/']

    def start_requests(self):
        url = 'https://news.163.com/20/0421/20/FAP08DF60001899O.html'   # url 要带:http://
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        item = NewsItem()
        new_id = response.url.split('/')[-1].split('.')[0]
        print(new_id)
        print(type(new_id))

        news_infoes = Selector(response=response).xpath("//div[@class='post_content_main']")
        
        for info in news_infoes:            
            newname = info.xpath('./h1/text()')
            new_name = newname.extract_first()
            print(new_name)
            item['new_title'] = new_name
            print(item['new_title'])
        
            url = f'https://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/{new_id}/comments/newList?ibc=newspc&limit=35&showLevelThreshold=72&headLimit=1&tailLimit=2&offset=0&callback=jsonp_1587525647702&_=1587525647703'
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        # print(response.text[20:-3]) #改造json串
        # result = json.loads(response.text[20:-3])
        res = json.loads(response.text.strip('\n').strip('jsonp_1587525647702(').strip(');'))
        custcomment = jsonpath.jsonpath(res,"$..content")
        for comment in custcomment:
            print(comment)
            item['new_custcomment'] = comment
            print(item['new_custcomment'])
            yield item




    


 
        

