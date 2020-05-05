# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrysSpider.items import RrysspiderItem


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            title = movie.xpath('./a/text()').extract_first().strip()
            link = self.start_urls[0] + movie.xpath('./a/@href').extract_first().strip()
            item = RrysspiderItem()
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        ranking = Selector(response=response).xpath('//p[@class="f4"]/text()').re('\d+')
        level = Selector(response=response).xpath('//div[@class="level-item"]/img/@src').re('.*\/*([a-z])-big*')
        view_count = Selector(response=response).xpath('//*[@id="score_list"]/div[1]').re('\d+')    
        cover_info = Selector(response=response).xpath('//div[@class="imglink"]/a/img/@src').extract()
        item = response.meta['item']
        item['ranking'] = ranking[0]
        item['level'] = level[0].upper()
        item['view_count'] = view_count[1]
        item['cover_info'] = cover_info[0]
        yield item
