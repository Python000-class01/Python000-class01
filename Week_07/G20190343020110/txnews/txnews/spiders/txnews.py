# -*- coding: utf-8 -*-
import scrapy
import lxml.etree
from txnews.items import TxnewsItem
import json
import re
import os
import re
#import jieba.analyse

class TxnewsSpider(scrapy.Spider):
    name = 'txnews'
    cursor = 0
    allowed_domains = ['new.qq.com']
    start_urls = [
        'https://coral.qq.com/article/5158603687/comment/v2?callback=_article5158603687commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6661017195559321119&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=1588120620544']

    def start_requests(self):
        url = f'https://coral.qq.com/article/5158603687/comment/v2?callback=_article5158603687commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=1588123073357'
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        commentnum = json.loads(re.search(
            "_article5158603687commentv2\\((.+)\\)", response.text).group(1))["data"]["targetInfo"]["commentnum"]
        self.last = json.loads(re.search(
            "_article5158603687commentv2\\((.+)\\)", response.text).group(1))["data"]["last"]
        print(self.last)
        #print(round(int(commentnum) / 10))
        num = round(int(commentnum) / 10)
        tmpcursor = self.cursor
        for i in range(0,num):
            try:
                link = f'https://coral.qq.com/article/5158603687/comment/v2?callback=_article5158603687commentv2&orinum=10&oriorder=o&pageflag=1&cursor={tmpcursor}&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=1588123073357'
                yield scrapy.Request(url=link, meta={'last': self.last}, callback=self.parse2)
            except:
                print('error')
            
    
    def parse2(self, response):
        print(response)
       
