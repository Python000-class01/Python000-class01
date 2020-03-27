# -*- coding: utf-8 -*-
import scrapy
import lxml.etree
from movie.items import MovieItem
import re


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['u.geekbang.org'] #允许的域名
    start_urls = ['http://https://u.geekbang.org/lesson/8?article=201448/'] #爬取的第一个页面

    def start_requests(self,response):
        selector1 = lxml.etree.HTML(response.text)
        for i in range(1,15):
            urlpart1 = selector1.xpath('//div[@class="box clearfix"]/ul/li[%s]/a/@href' %i)
            url = 'http://www.rrys2019.com/resource/'+ urlpart1
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): #response是网页的内容
        selector2 = lxml.etree.HTML(response.text)
        item = MovieItem()
        num = selector2.xpath('//p[@class="f4"]/text()')
        level = re.findall("\d+", str(num))
        item['level'] = level
        yield item
