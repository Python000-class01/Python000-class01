# -*- coding: utf-8 -*-
import scrapy


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030')

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        print(response.url)
        print(response.text) 
        new_response = str(response.body, encoding='utf-8')