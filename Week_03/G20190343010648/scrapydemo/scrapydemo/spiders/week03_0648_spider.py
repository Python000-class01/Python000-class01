# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ExampleSpider(scrapy.Spider):
    name = 'week03_0648_spider'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):

        top24_div = Selector(response=response).xpath('//div[contains(@class,"top24")]')
        #print(top24_div)
        top24_lis = top24_div.xpath('./div/ul/li')
       # print(top24_lis)
        for li in top24_lis:
            title = li.xpath('./a/text()')
            href = li.xpath('./a/@href')
            print(title.extract())
            print(href.extract())

    def parse_details(self, response):
        detail_div = Selector(response=response).xpath('//div[contains(@class,"top24")]')