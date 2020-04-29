# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from bookcom.items import BookcomItem
import json

class ComcapSpider(scrapy.Spider):
    name = 'comcap'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-irczymi8475793']

    def start_requests(self):
        url = f'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-irczymi8475793'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #print(response.body)
        jsonbody = json.loads(response.body.decode('gbk').encode('utf-8'))
        print(jsonbody)
        articles=jsonbody['result']['cmntlist']
        for art in articles:
            item=BookcomItem()
            item['uid']=art['uid']
            item['cmttime']=art['time']
            item['comment']=art['content']
            item['agree']=art['agree']
            item['usertype']=art['usertype']
            item['area']=art['area']
            item['ipadd']=art['ip']
            yield item

