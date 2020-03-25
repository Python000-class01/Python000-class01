# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rryshotmovie.items import RryshotmovieItem
import json


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    # start_urls = ['http://www.rrys2019.com/resource/39526']
    # start_urls = ['http://www.rrys2019.com/resource/index_json/rid/39526/channel/tv']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for mv in movies:
            mvtype = mv.xpath('./em/text()').extract_first().strip()
            if mvtype == '电影':
                seniority = mv.xpath('./span/text()')
                link = mv.xpath('./a/@href')
                title = mv.xpath('./a/@title')
                # 在items.py定义RryshotmovieItem
                item = RryshotmovieItem()
                item['title'] = title.extract_first().strip()
                item['seniority'] = seniority.extract_first().strip()
                item['link'] = response.url + link.extract_first().strip()
                # print(item['title'])
                yield scrapy.Request(url=item['link'], meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        # 电影排名
        seniority = Selector(response=response).xpath('//p[@class="f4"]/text()')
        # 电影分级
        mvrank = Selector(response=response).xpath('//div[@class="level-item"]/img/@src')
        # 封面信息
        cover = Selector(response=response).xpath('//div[@class="imglink"]/a/img/@src')
        item['seniority'] = seniority.extract_first().strip()
        item['rank'] = mvrank.extract_first().strip()
        item['cover'] = cover.extract_first().strip()

        # print(item['seniority'])
        # print(item['rank'])
        # print(item['cover'])
        bt_url = item['link'].replace('/resource', '/resource/index_json/rid') + '/channel/movie'
        yield scrapy.Request(url=bt_url, meta={'item': item}, callback=self.parse_views)

    # 浏览次数
    def parse_views(self, response):
        item = response.meta['item']
        bt_data = response.text.replace('var index_info=', '')
        bt_jsondata = json.loads(bt_data)
        item['views'] = bt_jsondata['views']

        # title = item['title']
        # link = item['link']
        # seniority = item['seniority']
        # views = item['views']
        # rank = item['rank']
        # cover = item['cover']
        # print('id(item):', id(item))
        #
        # print(f'{title}\t{link}\t{seniority}\t{views}\t{rank}\t{cover}\n\n')

        yield item
