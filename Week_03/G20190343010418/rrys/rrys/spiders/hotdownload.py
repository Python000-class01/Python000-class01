# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from rrys.items import RrysItem


class HotdownloadSpider(scrapy.Spider):
    name = 'hotdownload'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        print(f'in parse of hotdownload_spider, url:{response.url}')
        # print(response.text)
        films = Selector(response=response).xpath('/html/body/div[2]/div/div[1]/div/ul/li')

        # print(films)
        for li in films:
            # print(li)
            film_name = li.xpath('./a/@title').extract()[0]
            film_url = response.url + li.xpath('./a/@href').extract()[0]
            print(f'{film_name} \t {film_url}')
            # from src.homework.week03.rrys.rrys.items import RrysItem
            item = RrysItem()
            item['film_name'] = film_name
            item['film_rank'] = ''
            item['film_class'] = ''
            item['film_viewcount'] = ''
            item['film_cover'] = ''

            print(item)

            yield scrapy.Request(url=film_url, meta={'item': item}, callback=self.parse_film)

    def parse_film(self, response):
        item = response.meta['item']
        film_rank = Selector(response=response).xpath(
            '/html/body/div[2]/div/div[1]/div[2]/div/ul/li[1]/p/text()').extract_first()
        # film_viewcount = Selector(response=response).xpath('//*[@id="resource_views"]/../..')
        # film_viewcount = Selector(response=response).xpath('//*[@id="resource_views"]//text()').extract()[0]
        film_viewcount = '0'
        film_class = Selector(response=response).xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src').extract_first()
        film_cover = Selector(response=response).xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src').extract_first()

        index = film_rank.index(':')
        film_rank = film_rank[index + 1:].lstrip().rstrip()
        print(f'film_rank: {film_rank}')
        print(f'film_class: {film_class}')
        print(f'film_cover: {film_cover}')
        print(f'film_viewcount: {film_viewcount}')
        # print(f'film_viewcount: {film_viewcount.xpath("./div/label/text()").extract()[0]}')
        item['film_class'] = 'a'
        item['film_rank'] = film_rank
        item['film_class'] = film_class
        item['film_cover'] = film_cover
        item['film_viewcount'] = film_viewcount

        # item['film_viewcount'] = film_viewcount
        # print(item)
        print(f"in parse_film , item: {item}")
        return item
