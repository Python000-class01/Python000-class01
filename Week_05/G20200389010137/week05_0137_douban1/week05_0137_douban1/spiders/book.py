# -*- coding: utf-8 -*-
import scrapy
# from scrapy.selector import Selector
from week05_0137_douban1.items import Week050137Douban1Item
import re

character_map = {
    ord('\n') : ' ',
    ord('\t') : ' ',
    ord('\r'): None,
    ord('\''): None,
    ord(','): "，",
    }

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']

    def start_requests(self):
        for i in range(1, 6):
            url = f'https://book.douban.com/subject/1007305/comments/hot?p={i}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        comments = response.selector.xpath('//div[@class="comment"]')
        for comment in comments:
            shortContent = comment.xpath('./p/span[@class="short"]/text()').extract_first().strip().translate(character_map)
            star = comment.xpath('.//span[contains(@class,"user-stars")]/@title').extract_first()
            # print(f'shortContent={shortContent}')
            # print(f'star={star}')

            item = Week050137Douban1Item()
            item['shortContent'] = shortContent
            item['star'] = star
            yield item