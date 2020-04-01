# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys.items import RrysItem

class Hot24hMovieSpider(scrapy.Spider):
    name = 'hot_24h_movie'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
        yield scrapy.Request(url='http://www.rrys2019.com/', callback=self.parse)

    def parse(self, response):
        top_24 = Selector(response=response).xpath('/html/body/div[2]/div/div[1]')
        movies = top_24.xpath('./li')
        print(movies)
        for movie in movies:
            item = RrysItem()

            rank = movie.xpath('./em/text()')
            title = movie.xpath('./a/text()')
            link = movie.xpath('./a/@href')
            print('hohohohoho')
            print(link)
            item['title'] = titile
            item['rank'] = rank
            item['link'] = link
            
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        print(response.text)
        category = Selector(response=response).xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src')
        item['category'] = category
        return item