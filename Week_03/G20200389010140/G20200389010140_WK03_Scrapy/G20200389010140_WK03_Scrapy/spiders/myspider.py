# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['http://www.rrys2019.com/']
    start_urls = ['http://http://www.rrys2019.com//']

    def parse(self, response):
        pass
