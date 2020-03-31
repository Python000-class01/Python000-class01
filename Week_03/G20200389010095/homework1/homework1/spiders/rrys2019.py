# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

class Rrys2019Spider(scrapy.Spider):
    name = 'rrys2019'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="fl box top24"]//li')
        for movie in movies:
            from Week_03.G20200389010095.homework1.homework1.items import Homework1Item
            item = Homework1Item()
            movieName = movie.xpath('./a/text()')
            link = self.start_urls[0]+movie.xpath('./a/@href')
            item['movieName'] = movieName
            item['link'] = link
            # print([movieName,link])

            yield scrapy.Request(url=link,meta={'item':item}, callback=self.parse2)

    def parse2(self,response):
        item = response.meta['item']
        classification = Selector(response=response).xpath(
            '//div[@class="fl view-left"]//div[@class="level-item"]//img/@src')
        coverInfo = Selector(response=response).xpath('//div[@class="fl view-left"]//div[@class="imglink"]//img/@src')
        browse_times = Selector(response=response).xpath('//li[@class="score-star"]//label/text()')
        browseTimes = int(browse_times.extract_first().strip())

        item['classification'] = classification
        item['coverInfo'] = coverInfo
        item['browseTimes'] = browseTimes

        yield item