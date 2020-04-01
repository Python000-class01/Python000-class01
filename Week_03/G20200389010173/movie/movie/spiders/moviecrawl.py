# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from movie.items import MovieItem
import json


class MoviecrawlSpider(scrapy.Spider):
    name = 'moviecrawl'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def start_requests(self):
        url = 'http://rrys2019.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            hot = movie.xpath('span/text()').extract_first().strip()
            link = movie.xpath('a/@href').extract_first().strip()
            name = movie.xpath('a/text()').extract_first().strip()
            # 电影和剧请求的不同接口，需要区别对待
            cate = movie.xpath('em/text()').extract_first().strip()
            cate = 'movie' if cate == '电影' else 'tv'

            movie_item = MovieItem()
            movie_item['hot'] = hot
            movie_item['name'] = name
            movie_item['link'] = link
            movie_item['cate'] = cate

            link = f'http://rrys2019.com{link}'
            yield scrapy.Request(url=link, meta={'item':movie_item}, callback=self.parse_movie)
    
    def parse_movie(self, response):
        movie_item = response.meta['item']
        selector = Selector(response=response)
        level = selector.xpath('//div[@class="fl-info"]/div/img/@src').extract()
        # 资源id，用于请求一些数据
        resourceid = movie_item['link'].split('/')[-1]
        
        cate = movie_item['cate']
        count_url = f'http://www.rrys2019.com/resource/index_json/rid/{resourceid}/channel/{cate} '
        yield scrapy.Request(url=count_url, meta={'item':movie_item}, callback=self.parse_movie_viewcount)
    
    def parse_movie_viewcount(self, response):
        text_dict = json.loads(response.text[15:])
        movie_item = response.meta['item']
        movie_item['viewcount'] = text_dict['views']
        yield movie_item
