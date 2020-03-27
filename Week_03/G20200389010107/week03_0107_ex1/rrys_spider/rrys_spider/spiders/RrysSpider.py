# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from scrapy import Request
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from rrys_spider.items import RrysSpiderItem


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        movies = Selector(response=response).xpath(
            "//div[@class='box clearfix']/ul/li")
        base_url = get_base_url(response)
        for movie in movies:
            item = RrysSpiderItem()
            item["title"] = movie.xpath("a/text()").extract()[0]
            relative_url = movie.xpath("a/@href").extract()[0]
            # str(urljoin_rfc(base_url, relative_url))
            item["id"] = relative_url.split("/")[2]
            item["link"] = base_url + relative_url
            # print(item)
            yield Request(url=item["link"], meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta["item"]
        sel = Selector(response=response)
        rating = sel.xpath(
            "//div[@class='level-item']/img/@src").re('.*\/*([a-e])-big*')[0].upper()
        item["rating"] = rating
        item["cover_image"] = sel.xpath(
            '//div[@class="fl-img"]/div[@class="imglink"]/a/img/@src').extract()[0]

        #print("parse result: ", item)
        view_detail_url = f'http://www.rrys2019.com/resource/index_json/rid/{item["id"]}/channel/tv'
        yield Request(url=view_detail_url, meta={'item': item}, callback=self.parse_view_count)

    def parse_view_count(self, response):
        item = response.meta["item"]
        print("PARSE VIEW COUNT:")
        item["view_count"] = re.search(
            r'"views":"([0-9]+)"', response.text, re.M | re.I).group(1)

        print("item: ", item)
        yield item
