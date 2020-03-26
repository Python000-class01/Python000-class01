# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys.items import RrysItem
import re
import json


class CrawlRrysSpider(scrapy.Spider):
    name = 'crawl-rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def parse(self, response):
        movies = Selector(response=response).xpath(query='//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            title = movie.xpath('./a/@title').get()
            link = movie.xpath('./a/@href').get()

            movie_item = RrysItem()
            movie_item['title'] = title
            movie_item['id'] = link.split("/")[-1]
            yield scrapy.Request(url=f'http://rrys2019.com/{link}', meta={'item': movie_item}, callback=self.parse_detail)


    # 解析详情
    def parse_detail(self, response):
        item = response.meta['item']
        # rank = scrapy.Field()
        # level = scrapy.Field()
        # views = scrapy.Field()
        # cover = scrapy.Field()
        response = Selector(response=response)
        level_link = response.xpath('//div[@class="level-item"]/img/@src').get()
        level = level_link.split('/')[-1].split('-')[0]
        right_ul = response.xpath('//ul[@class="score-con"]')
        rank = right_ul.xpath('./li[1]/p/text()').get()
        cover = response.xpath('//div[@class="imglink"]/a/@href').get()

        item['rank'] = re.sub('\D', '', rank)
        item['level'] = level
        item['cover'] = cover
        movie_id = item['id']
        yield scrapy.Request(
            url=f'http://www.rrys2019.com/resource/index_json/rid/{movie_id}/channel/movie',
            meta={'item': item},
            callback=self.get_views,

        )

    def get_views(self, response):

        item = response.meta['item']
        result = json.loads(response.text[15:])
        views = result['views']
        item['views'] = views
        return item

