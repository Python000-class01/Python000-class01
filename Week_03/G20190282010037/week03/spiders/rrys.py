# -*- coding: utf-8 -*-

# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
import scrapy
from scrapy.selector import Selector
from week03.items import Week03Item
# from week03.items

class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com/']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)
        # for i in range(0, 10):
        #     url = f'https://book.douban.com/top250?start={i*25}'
            # yield scrapy.Request(url=url, callback=self.parse)
     

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="fl box top24"]//li')
        for movie in movies:
            item=Week03Item()
            movieName = movie.xpath('./a/text()')
            link = self.start_urls[0]+movie.xpath('./a/@href')
            item['movieName']=movieName
            item['link'] = link

        #     ##debug
        #     items.append(item)
        # return items

            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        # movie = Selector(response=response).xpath('//div[@class="fl box top24"]//li')
        # //div[@class="fl view-left"]//div[@class="level-item"]//img/@src
        # //div[@class="fl view-left"]//div[@class="imglink"]//img/@src
        # content = movie.xpath('./a/@href').get_text().strip()
        # item['content'] = content
        classification=Selector(response=response).xpath('//div[@class="fl view-left"]//div[@class="level-item"]//img/@src')
        coverInfo=Selector(response=response).xpath('//div[@class="fl view-left"]//div[@class="imglink"]//img/@src')
        browse_times = Selector(response=response).xpath('//li[@class="score-star"]//label/text()')
        browseTimes = int(browse_times.extract_first().strip())
        item['classification']=classification
        item['coverInfo']=coverInfo
        item['browseTimes']=browseTimes

        yield item
