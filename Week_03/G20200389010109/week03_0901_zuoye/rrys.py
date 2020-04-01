# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ceshi.items import CeshiItem
import re
import json

class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        # print(response.url)
        ys = Selector(response=response).xpath('/html/body/div[2]/div/div[1]/div/ul/li')
        for y in ys:
            #/html/body/div[2]/div/div[1]/div/ul/li[1]/em
            lx = y.xpath('./em/text()')[0]
            if lx == '电影':
                #/html/body/div[2]/div/div[1]/div/ul/li[2]/span
                rank = y.xpath('./span/text()')
                #/html/body/div[2]/div/div[1]/div/ul/li[2]/a
                title = y.xpath('./a/text()')
                url = y.xpath('./a/@href')
                url1 = url.extract_first().strip()
                item = CeshiItem()
                item['rank'] = rank
                item['title'] = title
                rid = re.findall(r'\d+',url1)
                item['rid'] = rid
                url2 = 'http://www.rrys2019.com' + url1
                yield scrapy.Request(url=url2, meta={'item': item}, callback=self.parse2)
        
    def parse2(self, response):
        item = response.meta['item']
        #/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img
        img = Selector(response=response).xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src')
        # //*[@id="resource_views"]
        # views = Selector(response=response).xpath('')
        #/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img
        level = Selector(response=response).xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src')
        url3 = 'http://www.rrys2019.com/'+ 'resource/index_json/rid/' + item['rid'] + 'channel/movie'
        item['img'] = img
        item['level'] = level
        yield scrapy.Request(url=url3, meta={'item': item}, callback=self.parse3)

    def parse3(self, response):
        item = response.meta['item']
        views = json.loads(response.text[15:])['views']
        item['views'] = views
        yield item