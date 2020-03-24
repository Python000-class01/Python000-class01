# -*- coding: utf-8 -*-
import scrapy
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

from scrapy.selector import Selector
from scrapy_rrys.items import ScrapyRrysItem

class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]')
        for movie in movies:
            video_type = movie.xpath('./ul/li/em/text()').extract()
            if video_type != '电影':
                continue
            link = movie.xpath('./ul/li/a/@href').extract()
            name = movie.xpath('./ul/li/a/@title').extract()
            item = ScrapyRrysItem()
            item['link'] = link
            item['title'] = name

            yield scrapy.Request(url=link, meta={'item': item}, callable=self.movie_parse)

    def movie_parse(self, response):
        item = response.meta['item']
        score_count = response.xpath('//ul[@class="score-con"]')
        score = score_count.xpath('./li/p[@class="f4"]/text()').extract()[0]
        count = score_count.xpath('./li/div[@class="count f4"]/div/label/text()').extract()[0]

