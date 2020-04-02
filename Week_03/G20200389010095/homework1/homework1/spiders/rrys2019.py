# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sys
sys.path.append('/Users/leith14/Python/Python000-class01')

from Week_03.G20200389010095.homework1.homework1.items import Homework1Item


class Rrys2019Spider(scrapy.Spider):
    name = 'rrys2019'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)
        # for i in range(0, 10):
        #     url = f'https://book.douban.com/top250?start={i*25}'
        # yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="fl box top24"]//li')
        for movie in movies:
            item = Homework1Item()
            movieName = movie.xpath('./a/text()')
            link = self.start_urls[0]+movie.xpath('./a/@href').extract_first().strip()
            item['movieName'] = movieName
            item['link'] = link
            # output = f'{movieName}\t{link}\n\n'
            # print(output)
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    # 图片的url转换成等级
    def levelImgUrl2levelNum(self, url: str) -> str:
        idx = url.rfind('/')
        if idx != -1 and idx != len(url) - 1:
            return url[idx + 1]

        return 'unknown'

    def parse2(self, response):
        item = response.meta['item']
        # movie = Selector(response=response).xpath('//div[@class="fl box top24"]//li')
        # //div[@class="fl view-left"]//div[@class="level-item"]//img/@src
        # //div[@class="fl view-left"]//div[@class="imglink"]//img/@src
        # content = movie.xpath('./a/@href').get_text().strip()
        # item['content'] = content


        classification = Selector(response=response).xpath('//div[@class="fl view-left"]//div[@class="level-item"]//img/@src')
        # classification= Selector(response=response).xpath('//div[@class="level-item"]//img/@src')
        # classification = self.levelImgUrl2levelNum(classification_sel.extract_first().strip())
        coverInfo = Selector(response=response).xpath('//div[@class="fl view-left"]//div[@class="imglink"]//img/@src')
        # coverInfo = self.levelImgUrl2levelNum(classification_sel.extract_first().strip())
        # browse_times_sel = Selector(response=response).xpath('//li[@class="score-star"]//label/text()')
        # browse_times = Selector(response=response).xpath('//li[@class="score-star"]//label/text()')

        # output = f'{coverInfo}\t{browse_times_sel}\n\n'
        # print(output)
        # browseTimes = int(browse_times_sel.extract_first().strip())
        item['classification'] = classification
        item['coverInfo'] = coverInfo
        # item['browseTimes'] = browseTimes

        yield item