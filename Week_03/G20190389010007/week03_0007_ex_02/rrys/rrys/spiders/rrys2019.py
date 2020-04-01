# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys.items import RrysItem
import re
import json


class Rrys2019Spider(scrapy.Spider):
    name = 'rrys2019'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com']

    def parse(self, response):
        movies_li = Selector(response=response).xpath(
            '//div[@class="box clearfix"]/ul/li')
        for movie_item in movies_li:
            rrys_item = RrysItem()
            movie = movie_item.xpath('./a/@title').extract_first()
            link = movie_item.xpath('./a/@href').extract_first()
            movie_type = movie_item.xpath('./em/text()').extract_first().strip()
            rrys_item['movie'] = movie
            rrys_item['movie_type'] = movie_type
            yield scrapy.Request(url=self.start_urls[0]+link, meta={'rrys_item': rrys_item}, callback=self.parse_moive_detail)

    def parse_moive_detail(self, response):
        rrys_item = response.meta['rrys_item']
        level_url = Selector(response=response).xpath(
            '//div[@class="level-item"]/img/@src').extract_first()
        img_url = Selector(response=response).xpath(
            '//div[@class="imglink"]/a/img/@src').extract_first()
        rank = Selector(response=response).xpath(
            '//p[@class="f4"]/text()').extract_first().strip()
        rrys_item['rank']=re.findall(r"\d+", rank)[0]
        rrys_item['level'] = re.findall(r"icon/(.+?)-big", level_url)[0]
        rrys_item['title_img'] = img_url
        movie_id = re.findall(r"resource/(.+)", response.url)[0]
        # 获得vv数据的url
        index_info_url = f'http://www.rrys2019.com/resource/index_json/rid/{movie_id}/channel/tv'
        yield scrapy.Request(url=index_info_url, meta={'rrys_item': rrys_item}, callback=self.parse_view_data)

    def parse_view_data(self, response):
        rrys_item = response.meta['rrys_item']
        json_data = json.loads(re.findall(
            r"index_info=(.+)", response.text)[0])
        rrys_item['view_volume'] = json_data['views']
        yield rrys_item
