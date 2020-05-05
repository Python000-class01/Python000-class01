# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from week03_0147_ex.items import Week030147ExItem
import unicodedata

# 亂碼
# import sysimprot 
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030')

class ExampleSpider(scrapy.Spider):
    name = 'rrys2019'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
        url = 'http://www.rrys2019.com/resource/33701'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Week030147ExItem()
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]')
        for movie in movies:
            item['ranking'] = movie.xpath('.//span/text()').extract()
            item['movie_nm'] = movie.xpath('.//a/text()').extract()
            link = movie.xpath('.//a/@href').extract()
        movie_link = []
        for i in link:
            movie_link.append('http://www.rrys2019.com'+i)
        item['movie_link'] = movie_link
        # 亂碼
        # new_reponse = str(response.body, encoding='utf-8')
        yield scrapy.Request(url=movie_link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        selector = Selector(response=response)

        # sth went wrong
        item['visits'] = selector.xpath('//*[@id="resource_views"]/text()')

        item['rating'] = [selector.xpath('//div[@class="level-item"]/img/@src').extract()[0][40:41]+'-level']
        item['info'] = [unicodedata.normalize('NFKC', \
            ''.join(selector.xpath('//div[@class="con"]/text()[1]').extract()+ \
            selector.xpath('//div[@class="con"]/text()[2]').extract())) \
            .replace('\n', '').replace('\r', '').replace(' ', '')]
        
        yield item