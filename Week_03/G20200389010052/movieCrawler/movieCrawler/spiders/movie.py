# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from movieCrawler.items import MoviecrawlerItem
import re


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    # def start_requests(self):
    #     url = 'http://www.rrys2019.com/'
    #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 通过首页获取24小时下载热门电影列表
        links = Selector(response=response).xpath('//*[@class="box clearfix"]//a')
        for link in links:
            # 通过列表中的链接进入电影详情页面
            yield response.follow(link, callback=self.parse2)

    # 详情解析
    def parse2(self, response):
        item = MoviecrawlerItem()
        selector = Selector(response=response)
        item['name'] = selector.xpath('//*[@class="fl-info"]//li[1]/strong/text()').extract_first()
        item['area'] = selector.xpath('//*[@class="fl-info"]//li[2]/strong/text()').extract_first()
        item['language'] = selector.xpath('//*[@class="fl-info"]//li[3]/strong/text()').extract_first()
        item['movie_type'] = selector.xpath('//*[@class="fl-info"]//li[6]/strong/text()').extract_first()
        item['ranking'] = re.findall(r'\d+', selector.xpath('//*[@class="score-con"]/li[1]/p/text()').extract_first())[0]
        item['level'] = selector.xpath('//*[@class="level-item"]/img/@src').extract_first()[40:41]
        item['images_urls'] = selector.xpath('//*[@class="clearfix resource-con"]//a/img/@src').extract()
        yield item
