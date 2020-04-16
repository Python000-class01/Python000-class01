# -*- coding: utf-8 -*-
import scrapy
from rensheng.items import RenshengItem


class HaihaiSpider(scrapy.Spider):
    name = 'haihai'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/subject/30475767/comments/']


####  first-step get the url for short-comment 
    def parse(self, response): 
        item = RenshengItem() 
        stars = response.xpath('//*[@id="comments"]//span[@class="comment-info"]/span[1]/@title').extract()
        short = response.xpath('//*[@id="comments"]//span[@class= "short"]/text()').extract()
        next_url = response.xpath('//*[@id="content"]//li[3]/a[@class="page-btn"]/@href').extract()
        item['star'] = stars
        item['short'] = short
        yield item
        if next_url:
            next_page_url = 'https://book.douban.com/subject/30475767/comments/'+ str(next_url[0])
            yield  scrapy.Request(url = next_page_url,meta={'item':item},callback = self.parse)
