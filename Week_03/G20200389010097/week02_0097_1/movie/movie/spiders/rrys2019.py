# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from movie.items import MovieItem


class Rrys2019Spider(scrapy.Spider):
    name = 'rrys2019'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            title = movie.xpath('./a/@title').extract_first().strip()
            link = "http://www.rrys2019.com/" +  movie.xpath('./a/@href').extract_first().strip()
            item = MovieItem()
            item['title'] = title
            item['link'] = link

            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        print(response)
        item = response.meta['item']
        rank_selector = Selector(response=response).xpath('//p[@class="f4"]/text()')
        level_selector = Selector(response=response).xpath('//div[@class="level-item"]')
        cover_selector = Selector(response=response).xpath('//div[@class="level-item"]')
        rank = rank_selector.extract_first().strip()
        item['rank'] = rank
        level = level_selector.xpath('./img/@src').extract_first().strip()
        item['level'] = level
        cover = cover_selector.xpath('./img/@src').extract_first().strip()
        item['cover'] = cover
        yield item
