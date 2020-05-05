# -*- coding: utf-8 -*-
import scrapy
from ..items import *


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        movie_24 = response.selector.xpath('/html/body/div[2]/div/div[1]/div/ul/li')
        for movie in movie_24:
            item = MyspiderItem()
            item['name'] = movie.xpath('a/text()').get()
            url = movie.xpath('a/@href').get()
            yield scrapy.Request(ExampleSpider.start_urls[0] + url, callback=self.parse_movie, meta={"item": item})
        pass

    def parse_movie(self, response):
        item = response.meta['item']
        url = item['url']
        item['pm'] = response.selector.xpath('/html/body/div[2]/div/div[1]/div[2]/div/ul/li[1]/p/text()').get()
        item['views'] = response.selector.xpath('//*[@id="resource_views"]/text()').get()
        item['infor'] = response.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src').extract()
        movie_id = url.split('\\')[1]
        views_url = f'http://www.rrys2019.com/resource/index_json/rid/{movie_id}/channel/tv'
        scrapy.Request(views_url,callback=self.parse3, meta={"item": item})
        yield item

    def parse3(self, response):
        
