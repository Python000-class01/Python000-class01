# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from movieinfo.items import MovieinfoItem


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    # def start_requests(self):
    #     movie_list =

    def parse(self, response):
        # /html/body/div[2]/div/div[1]/div/ul/li[10]
        movie_list = Selector(response=response).xpath(
            '/html/body/div[2]/div/div[1]/div/ul/li')
        for movie_info in movie_list:
            movie_rank = movie_info.xpath('./span/text()').extract_first()
            movie_name = movie_info.xpath('./a/@title').extract_first()
            movie_link = movie_info.xpath('./a/@href').extract_first()
            # print(movie_rank)
            # print(movie_name)
            # print(movie_link)
            item = MovieinfoItem()
            item['movie_rank'] = movie_rank
            item['movie_name'] = movie_name
            # url = start_urls + movie_link
            # print (url)
            yield response.follow(movie_link, meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        click_num = response.xpath(
            '//div[@class="count f4"]/div/label/text()').extract_first()
        jacket_addr = response.xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img').extract_first()
        item = response.meta['item']
        item['click_num'] = click_num
        item['jacket_addr'] = jacket_addr

        yield item
