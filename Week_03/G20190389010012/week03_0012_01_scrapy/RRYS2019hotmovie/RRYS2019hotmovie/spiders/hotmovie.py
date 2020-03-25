# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from RRYS2019hotmovie.items import Rrys2019HotmovieItem


class HotmovieSpider(scrapy.Spider):
    name = 'hotmovie'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        """
        parse start url
        :return:
        """
        movie_list = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movie_list:
            item = Rrys2019HotmovieItem()
            item['title'] = movie.xpath('./a/text()').extract_first().strip()
            link = movie.xpath('./a/@href').extract_first().strip()
            link = self.start_urls[0] + link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse_detail)

    @staticmethod
    def parse_detail(response):
        """
        parse movie detail information
        :param response:
        :return:
        """
        item = response.meta['item']
        selector = Selector(response=response)
        item['rank'] = selector.xpath('//p[@class="f4"]/text()').re('\d+')[0]
        item['count'] = selector.xpath('//*[@id="score_list"]/div[1]').re('\d+')[1]
        item['level'] = selector.xpath('//div[@class="level-item"]/img/@src').re('.*\/*([a-e])-big*')[0].upper()
        item["cover"] = selector.xpath('//div[@class="imglink"]/a/img/@src').extract()[0]
        yield item
