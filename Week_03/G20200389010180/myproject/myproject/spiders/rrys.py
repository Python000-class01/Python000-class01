# -*- coding: utf-8 -*-
import scrapy
import json
from myproject.items import HotMovies

class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']


    def parse(self, response):
        for mv in response.xpath('//div[@class="box clearfix"]//li'):  
            item = HotMovies()
            if mv.xpath('./em[contains(text(), "电影")]'):
                item['rank_24h'] = mv.xpath('.//span/text()').get()
                item['cname'] = mv.xpath('.//a/text()').get()
                yield response.follow(mv.xpath('.//a/@href').get(), self.detail_parse, meta={'item': item})


    def detail_parse(self, response):
        item = response.meta['item']

        cover = response.xpath('//div[@class="box clearfix res-view-top"]//div[@class="fl-info"]')      
        item['ename'] = cover.xpath('.//span[contains(text(), "原名")]/../strong/text()').get()
        item['area'] = cover.xpath('.//span[contains(text(), "地区")]/../strong/text()').get()
        item['language'] = cover.xpath('.//span[contains(text(), "语")]/../strong/text()').get()
        item['premiere'] = cover.xpath('.//span[contains(text(), "首播")]/../strong/text()').get()
        item['tv_station'] = cover.xpath('.//span[contains(text(), "制作公司")]/../strong/text()').get()
        item['category'] = cover.xpath('.//span[contains(text(), "类型")]/../strong/text()').get()
        item['rank'] = response.xpath('//p[@class="f4"]/text()').re(r'\d+')
        item['grade'] = response.xpath('//div[@class="level-item"]/img/@src').re(r'/([a-zA-Z])-big')[0]
        views_link = response.xpath('//script[contains(@src,"/resource/index_json/rid")]/@src').get()

        yield response.follow(views_link, self.parse_views, meta={'item': item})


    def parse_views(self, response):
        item = response.meta['item']
        body_text = response.text.replace('var index_info=','')
        jsonresponse = json.loads(body_text)
        item['views'] = jsonresponse['views']        
        return item

