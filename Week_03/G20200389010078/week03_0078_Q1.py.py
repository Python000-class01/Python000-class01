# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import sys
import io
from lxml import etree
from bs4 import BeautifulSoup as bs
import requests

class MovieSpider(scrapy.Spider):
    #定义爬虫名称
    name = 'Movies'
    allowed_domains = ['www.rrys2019.com']
    #起始url列表
    start_urls = ['http://www.rrys2019.com/ ']

    def start_requests(self):
        link = selector.xpath('/html/body/div[2]/div/div[1]/div/ul/li/a/@href')
        for i in range(0, 13):
            url = 'http://www.rrys2019.com/'+link[i]
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]')
        for movie in movies:
            ranking = movie.xpath('./span/text()')
            # classification =
            # movie.xpath('./span/text()')
        print(ranking)
        # new_response = str(response.body, encoding='utf-8')

