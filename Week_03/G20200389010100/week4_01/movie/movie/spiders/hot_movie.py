# -*- coding: utf-8 -*-
import re
import json

import scrapy
from scrapy.selector import Selector

from ..items import MovieItem

klass_url_dict = {
    'http://js.jstucdn.com/images/level-icon/a-big-1.png': 'a',
    'http://js.jstucdn.com/images/level-icon/b-big-1.png': 'b',
    'http://js.jstucdn.com/images/level-icon/c-big-1.png': 'c',
    'http://js.jstucdn.com/images/level-icon/d-big-1.png': 'd',
    'http://js.jstucdn.com/images/level-icon/e-big-1.png': 'e',
}


class HotMovieSpider(scrapy.Spider):
    name = 'hot_movie'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com']
    prefix_url = 'http://www.rrys2019.com'

    # def start_requests(self):
    #     yield scrapy.Request(url=self.start_urls[0])

    def parse(self, response):
        # 获得首页
        movies = Selector(response=response).xpath('/html/body/div[2]/div/div[1]/div/ul/li')

        # 循环热门列表
        for movie in movies:
            # 添加电影名称，详情url
            title = movie.xpath('./a/text()').extract_first()
            url = movie.xpath('./a/@href').extract_first()
            full_url = self.prefix_url + url
            item = MovieItem()
            item['title'] = title
            item['link'] = full_url

            rid = url.split('/')[2]
            item['rid'] = rid
            #     ##debug
            #     items.append(item)
            # return items
            yield scrapy.Request(
                url=full_url,
                meta={'item': item},
                callback=self.parse_movie
            )

    def parse_movie(self, response):
        # 分级
        item = response.meta['item']
        klass_url = Selector(response=response).xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src').extract_first()
        klass = self.klass_change(klass_url)
        item['klass'] = klass

        # 排名
        rank_text = Selector(response=response).xpath(
            '/html/body/div[2]/div/div[1]/div[2]/div/ul/li[1]/p/text()').extract_first()
        rank = re.search('\D*(\d*)', rank_text).group(1)
        item['rank'] = rank

        # 浏览数
        # count_text = Selector(response=response).xpath(
        #     '//*[@id="score_list"]/div[1]').extract_first()
        # print(count_text)
        # item['count'] = 0

        image = Selector(response=response).xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src').extract_first()
        item['image'] = image

        # yield item
        yield scrapy.Request(
            url=self.views_url(item['rid']),
            meta={'item': item},
            callback=self.parse3
        )

    def klass_change(self, klass_url):
        return klass_url_dict.get(klass_url)

    def views_url(self, movie_id):
        return f'http://www.rrys2019.com/resource/index_json/rid/{movie_id}/channel/movie'

    def parse3(self, response):
        # 浏览数
        a = response.body[15:].decode()
        item = response.meta['item']

        try:
            d = json.loads(a)
            views = d['views']
            item['count'] = views
        except Exception as err:
            print('err', err)
        yield item
