# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys.items import RrysItem

movie_list = []

class Rrys2019Spider(scrapy.Spider):
    name = 'rrys2019'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com']

    def parse(self, response):
        movies =  Selector(response=response).xpath('//div[@class="box clearfix"]//li')

        for movie in movies:   
            title = movie.xpath('./a/text()')
            link = movie.xpath('./a/@href')

            # debug
            # print(self.start_urls[0])
            # print(title)
            # print(link)
            # print('-----------')
            # print(title.extract())
            # print(link.extract())
            # print('-----------')
            # print(title.extract_first().strip())
            # print(self.start_urls[0] + link.extract_first().strip())

            item = RrysItem()
            titles = title.extract_first().strip()
            links = self.start_urls[0] + link.extract_first().strip()
            item['titles'] = titles
            item['links'] = links

            yield scrapy.Request(url=links, meta={'item': item}, callback=self.parse2)


    def parse2(self, response):
        item = response.meta['item']
        count = Selector(response=response).xpath('//*[@id="score_list"]/div[1]/div[2]/text()')
        score = Selector(response=response).xpath('//div[@class="box score-box"]/ul/li[1]/p/text()')

        # debug 
        # print(count.extract_first().strip())
        # print(score.extract_first().strip())
        item['counts'] = count.extract_first().strip()
        item['scores'] = score.extract_first().strip()
        print(item)
        yield item



