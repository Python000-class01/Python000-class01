# -*- coding: utf-8 -*-
import scrapy
from rrys2019.items import Rrys2019Item

# scrapy crawl movies --nolog


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }

    def start_requests(self):
        url = f'http://www.rrys2019.com/html/top/month_fav_list.html'
        yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        movies = response.xpath('//html/body/div[2]/div/div/div[2]/ul/li')
        for i in range(len(movies)):
            item = Rrys2019Item()
            # title = movies[i].xpath('.//div[1]/div[2]/a/strong/text()').extract()[0]
            # num = movies[i].xpath('.//div[1]/div[2]/p/span/text()').extract()[0]
            # url = movies[i].xpath('.//div[1]/div[2]/a/@href').extract()[0]
            new_url = self.start_urls[0] + movies[i].xpath('.//div[1]/div[2]/a/@href').extract()[0]
            item['title'] = movies[i].xpath('.//div[1]/div[2]/a/strong/text()').extract()[0]
            item['url'] = movies[i].xpath('.//div[1]/div[2]/a/@href').extract()[0]
            item['people_num'] = movies[i].xpath('.//div[1]/div[2]/p/span/text()').extract()[0]
            yield scrapy.Request(url=new_url, meta={'item': item}, callback=self.detail, headers=self.headers)
            yield item

    def detail(self, response):
        item = response.meta['item']
        content = response.xpath(
            '//html/body/div[2]/div/div[1]/div[1]/div[1]/p/text()').extract()[0]
        item['descr'] = content
        yield item
