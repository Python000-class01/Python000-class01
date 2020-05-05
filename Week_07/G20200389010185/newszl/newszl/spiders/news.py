# -*- coding: utf-8 -*-
import scrapy
import time
import random
import json
from newszl.items import NewszlItem
import os


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['comment.api.163.com']
    # start_urls = ['http://comment.api.163.com/']

    def start_requests(self):
        # 浏览器用户代理
        # ua = UserAgent(verify_ssl=False)
        headers = {
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        # 读取上次爬取的位置
        dir = os.path.dirname(os.path.abspath(__file__))
        f = open(f'{dir}\pagenum.txt','r')
        pagenum = f.read()
        f.close()
        # 生成时间戳
        dd = str(time.time()).split(".")[0]
        cc = random.randint(600, 990)
        link = 'http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/FAEE6IMC0529EJ2R/comments/newList?ibc=newspc&limit=30&showLevelThreshold=72&headLimit=1&tailLimit=2&offset='
        # 生成URL
        urls = [
            f'{link}{i + int(pagenum)}&callback=jsonp_{dd}{cc}&_={dd}{cc + 1}'
            for i in range(0,630,30)
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers,callback=self.parse)




    def parse(self, response):
        data = response.text
        jss = json.loads(data.split('(')[1].split(')')[0])
        dir = os.path.dirname(os.path.abspath(__file__))
        if bool(jss['comments']) is False:
            s = open(f'{dir}\pagenum.txt', 'w')
            s.write(str(jss['newListSize']))
            s.close()

        for js in jss['commentIds']:
            item = NewszlItem()
            item['pingjia'] = jss['comments'][js.split(',')[0]]['content']

            yield item




