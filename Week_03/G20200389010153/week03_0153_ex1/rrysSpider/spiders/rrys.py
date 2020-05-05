# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from items import RrysspiderItem

url = 'http://www.rrys2019.com/'


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       movie_list = Selector(response=response).xpath(
           '//div[@class="box clearfix"]/ul/li')
       for movie in movie_list:
           title = movie.xpath('./a/text()').extract_first().strip()
           href = movie.xpath('./a/@href').extract_first().strip()
           href_url = url + href

           item = RrysspiderItem()
           item['title'] = title
           item['href_url'] = href_url
           print(href_url)
           yield scrapy.Request(url=href_url, meta={'item': item}, callback=self.parse_deep)

    def parse_deep(self, response):
        rank = Selector(response=response).xpath('//p[@class="f4"]/text()').re('\d+')
        print(rank)
        level = Selector(response=response).xpath('//div[@class="level-item"]/img/@src').re('.*\/*([a-e])-big*')
        print(level[0].upper())
        viewcount = Selector(response=response).xpath('//*[@id="score_list"]/div[1]').re('\d+')
        print(viewcount[1])
        coverinfo = Selector(response=response).xpath(
            '//div[@class="imglink"]/a/img/@src').extract()
        print(coverinfo[0])
        item = response.meta['item']
        item['rank'] = rank[0]
        item['level'] = level[0].upper() + '级'
        item['viewcount'] = viewcount[1]
        item['coverinfo'] = coverinfo[0]
        yield item
