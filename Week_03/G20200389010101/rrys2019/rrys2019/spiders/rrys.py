# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys2019.items import Rrys2019Item


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
        url = 'http://www.rrys2019.com/'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            item = Rrys2019Item()
            rank = movie.xpath('./span/text()').extract_first()
            name = movie.xpath('./a/text()').extract_first()
            link = 'http://www.rrys2019.com' + movie.xpath('./a/@href').extract_first()
            item['rank'] = rank
            item['name'] = name
            yield scrapy.Request(url=link, meta={'item':item}, callback=self.parse2, dont_filter=True)

    def parse2(self, response):
        item = response.meta['item']
        movie_class = Selector(response=response).xpath('//div[@class="level-item"]/img/@src').extract_first()[-11]
        views = Selector(response=response).xpath('//div[@class="count f4"]/div/label/text()').extract_first()
        cover = Selector(response=response).xpath('//div[@class="imglink"]/a/@href').extract_first()
        item['movie_class'] = movie_class
        item['views'] = views
        item['cover'] = cover
        yield item