# -*- coding: utf-8 -*-
import scrapy

import sys
import io
import codecs
from mySpilder.items import Top24HoursItem
import re

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030')

class RsjSpider(scrapy.Spider):
    name = 'rsj'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
            yield scrapy.Request(url = 'http://www.rrys2019.com/', callback=self.parse)

    def parse(self, response):

        selectorList = scrapy.Selector(text=response.text).xpath('//div[contains(@class, "top24")]/div[contains(@class,"box")]/ul/li/a')
        idx = 1
        for s in selectorList:
            href = s.xpath('./@href').extract()[0]
            url =  f'http://www.rrys2019.com{href}'
            title = s.xpath('./@title').extract()[0]
            item = Top24HoursItem()
            item['url'] = url
            item['title'] = title
            item['topIndex'] = idx
            item['id'] = item['url'].replace('http://www.rrys2019.com/resource/','')
            idx = idx + 1
            yield scrapy.Request(url=item["url"], meta={'item': item}, callback=self.parseInfo)
    
    def parseInfo(self, response):
        item = response.meta['item']
        shtml = scrapy.Selector(text=response.text)
        item['score'] = shtml.xpath('//ul[@class="score-con"]//p[contains(text(), "本站排名")]/text()').extract()[0].replace('本站排名:','')
        item['level'] = shtml.xpath('//div[@class="level-item"]/img/@src').extract()[0].replace('http://js.jstucdn.com/images/level-icon/','').replace('-big-1.png','')
        viewUrl = f'http://www.rrys2019.com/resource/index_json/rid/{item["id"]}/channel/tv'
        item['faceImageUrl'] = shtml.xpath('//div[contains(@class, "resource-con")]/div[@class="fl-img"]/div[@class="imglink"]/a/@href').extract()[0]
        yield scrapy.Request(url=viewUrl, meta={'item': item}, callback=self.parseViews)
    
    # 获取浏览数量
    def parseViews(self, response):
        item = response.meta['item']
        item['views'] = re.search(r'"views":"([0-9]+)"', response.text, re.M|re.I).group(1)
        item['file_urls'] = []
        item['file_urls'].append(item['faceImageUrl'])
        yield item


