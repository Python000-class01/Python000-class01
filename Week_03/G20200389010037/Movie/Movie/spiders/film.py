# -*- coding: utf-8 -*-
import scrapy
import sys
import io
import requests
import lxml.etree
from Movie.items import MovieItem
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030')

class FilmSpider(scrapy.Spider):
    name = 'film'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def start_requests(self):
        self.url = 'http://rrys2019.com/'
        yield scrapy.Request(url =self.url ,callback=self.parse)

    def parse(self, response):
        # res = requests.get('http://www.rrys2019.com')
        pl = lxml.etree.HTML(response.text)
        nu = pl.xpath('//div[@class = "box clearfix"]//li/span/text()')
        title = pl.xpath('//div[@class = "box clearfix"]//li/a/text()')
        link = pl.xpath('//div[@class = "box clearfix"]//li/a/@href')
        for x in range(len(title)):
            item =MovieItem()
            num = nu[x]
            Titler = title[x]
            Link = link[x]
            item['num'] = num
            item['title'] = Titler
        # url需要仔细想一下
        yield scrapy.Request(url ='http://www.rrys2019.com'+Link,meta={'item':item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        Pl = lxml.etree.HTML(response.text)
        item =MovieItem()
        level = Pl.xpath('//div[@class="level-item" ]/img/@src')
        views = Pl.xpath('//*[@id="score_list"]/div[1]/div[1]/text()')
        item['level'] = level
        item['resource_views'] = views
        yield item