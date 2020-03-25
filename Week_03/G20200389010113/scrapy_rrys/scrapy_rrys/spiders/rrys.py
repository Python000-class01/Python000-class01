# -*- coding: utf-8 -*-
import scrapy
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from scrapy.selector import Selector
from scrapy_rrys.items import ScrapyRrysItem

class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            video_type = movie.xpath('./em/text()').extract_first().strip()
            if video_type != '电影':
                continue
            link = movie.xpath('./a/@href').extract_first().strip()
            name = movie.xpath('./a/@title').extract_first().strip()
            item = ScrapyRrysItem()
            item['link'] = RrysSpider.start_urls[0] + '/' + link
            item['title'] = name
            print(item['link'])
            
            yield scrapy.Request(url=item['link'], meta={'item': item}, callback=self.movie_parse)

    def movie_parse(self, response):
        item = response.meta['item']
        score_count = Selector(response=response).xpath('//ul[@class="score-con"]')
        score = score_count.xpath('./li/p[@class="f4"]/text()').extract_first().strip()
        # count = score_count.xpath('./li/div[@class="count f4"]/div/label/text()').extract_first().strip()
        item['score'] = score
        # item['count'] = count
        # print(item['link'])
        yield item

