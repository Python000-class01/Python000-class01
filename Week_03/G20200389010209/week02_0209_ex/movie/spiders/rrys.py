# -*- coding: utf-8 -*-
import scrapy


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['u.geekbang.org'] #允许的域名
    start_urls = ['http://https://u.geekbang.org/lesson/8?article=201448/'] #爬取的第一个页面

    def parse(self, response): #response是网页的内容
        pass
