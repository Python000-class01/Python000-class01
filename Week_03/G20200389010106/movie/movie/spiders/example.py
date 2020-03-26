# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector
from movie.items import MovieItem
import re
import urllib.parse
import requests
import json

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            item = MovieItem()
            title_selector = movie.xpath('./a/@title')
            url_selectior = movie.xpath('./a/@href')
            title = title_selector.extract_first().strip()
            detail_url = response.url + url_selectior.extract_first().strip()
            item['title'] = title
            yield scrapy.Request(url=detail_url, meta={'item': item}, callback=self.movie_detail_parse)

    def movie_detail_parse(self, response):

        item = response.meta['item']

        rank_elmt = Selector(response=response).xpath('.//div[@class="box score-box"]//p[@class="f4"]/text()')
        rank_p = re.compile("[0-9]+")
        rank = int(rank_p.findall(rank_elmt.extract_first())[0])

        image_elmt = Selector(response=response).xpath('.//div[@class="imglink"]//a/@href')
        image_link = image_elmt.extract_first()

        grade_image_elmt = Selector(response=response).xpath('.//div[@class="level-item"]//img/@src')
        grade_image_link = grade_image_elmt.extract_first()
        grade = grade_image_link.split('/')[-1][0]

        view_selector = Selector(response=response).xpath(
            '//script[@type="text/javascript" and contains(@src,"rid")]/@src')
        view_uri = view_selector.extract_first()
        parsed_uri = urllib.parse.urlsplit(response.url)
        view_link = f'{parsed_uri.scheme}://{parsed_uri.netloc}{view_uri}'
        view_response = requests.get(view_link)
        view = None
        if view_response.status_code == 200:
            view = int(json.loads(view_response.text.split("index_info=")[1])['views'])

        item['rank'] = rank
        item['image'] = image_link
        item['grade'] = grade
        item['view'] = view

        print(item)
        yield item