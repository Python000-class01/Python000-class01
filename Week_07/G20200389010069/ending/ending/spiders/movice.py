# -*- coding: utf-8 -*-
import scrapy
from ..items import EndingItem

class MoviceSpider(scrapy.Spider):
    name = 'movice'
    allowed_domains = ['http://www.rrys2019.com/']
    start_urls = ['http://www.rrys2019.com//']

    def parse(self, response):
        urls = response.xpath('//ul[@id="commentList"]/li/div/p')
        for i  in urls:
            moives = i.xpath('./text()').getall()
            item = EndingItem(movie=moives)
            print(item)
            yield item


