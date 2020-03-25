# -*- coding: utf-8 -*-
import scrapy

import os
import io

sys.stdout = io.TestIOWrapper(sys.stdout.buffer, encoding = 'gb18030')

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['http://www.rrys2019.com/']
    start_urls = ['http://http://www.rrys2019.com//']

    def parse(self, response):
        #pass
        print(response.txt)
        print(response.url)
