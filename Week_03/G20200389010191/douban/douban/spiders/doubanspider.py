# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanspider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath('//ol[@class="grid_view"]//li')
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = i_item.xpath('.//em/text()').extract()
            douban_item['movie_name'] = i_item.xpath('.//a//span[1]/text()').extract()
            content = i_item.xpath(".//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = ''.join(i_content.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = i_item.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            yield douban_item
            
        next_link = response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('https://movie.douban.com/top250'+str(next_link),callback=self.parse)
