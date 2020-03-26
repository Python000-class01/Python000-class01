# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from Hour24HotMovieRRYS.items import Hour24HotmovierrysItem
import re

class HotmovieSpider(scrapy.Spider):
    name = 'HotMovie'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        hot_movies = Selector(response=response).xpath('//div[@class="fl box top24"]//li')
        for movie in hot_movies:
            rank = movie.xpath('./span/text()').extract_first().strip()
            name = movie.xpath('./a/@title').extract_first().strip()
            link_url = movie.xpath('./a/@href').extract_first().strip()
            if link_url.find('http') == -1:
                link_url = self.start_urls[0] + link_url

            movie_info = Hour24HotmovierrysItem()
            movie_info['movie_name'] = name
            movie_info['movie_rank'] = rank

            yield scrapy.Request(url=link_url, meta={'movie_info': movie_info}, callback=self.parseMovieDetail)

    # 图片的url转换成等级
    def levelImgUrl2levelNum(self, url: str) -> str:
        idx = url.rfind('/')
        if idx != -1 and idx != len(url) - 1:
            return url[idx+1]

        return 'unknown'

    def parseMovieDetail(self, response):
        movie_info = response.meta['movie_info']

        level_sel = Selector(response=response).xpath('//div[@class="level-item"]//img/@src')
        level = self.levelImgUrl2levelNum(level_sel.extract_first().strip())
        movie_info['movie_level'] = level

        brief_sel = Selector(response=response).xpath('//div[@class="resource-desc"]/div[@class="con"]/span[1]//text()')
        brief = brief_sel.extract_first().strip()
        movie_info['brief_desc'] = brief

        browse_times_sel = Selector(response=response).xpath('//li[@class="score-star"]//label/text()')
        browse_times = int(browse_times_sel.extract_first().strip())
        movie_info['browse_times'] = browse_times

        yield movie_info





