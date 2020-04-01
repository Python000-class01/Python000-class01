# -*- coding: utf-8 -*-
import scrapy
import json
from rrys.items import RrysItem


class RrysTop24Spider(scrapy.Spider):
    name = 'rrys_top24'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com']


    # 提取top下载视频url
    def parse(self, response):
        urls_postfix = response.xpath('//div[@class="box clearfix"]//a/@href').extract() 
        
        for u in urls_postfix:
            url = self.start_urls[0] + u
            yield scrapy.Request(url, callback=self.parse_items)


    # 提取每个top下载视频的名称、排行、分级、封面信息等相关信息
    def parse_items(self, response):
        item = RrysItem()

        item['name'] = response.xpath('//div[@class="resource-tit"]//h2/text()[1]').re(r'[《](.*)[》]')[0]
        item['ranking'] = response.xpath('//div[@class="box score-box"]//p[@class]/text()').extract_first().replace(u'\xa0', u'').strip()
        item['level'] = response.xpath('//div[@class="level-item"]//img/@src').re(r'/([a-zA-Z])-big')[0]
        item['cover'] = response.xpath('//div[@class="imglink"]/a/@href').extract_first()
        
        # 
        views_link = response.xpath('//script[contains(@src,"/resource/index_json/rid")]/@src').get()

        yield response.follow(views_link, self.parse_views, meta={'item': item})

    # 提取浏览次数
    def parse_views(self, response):
        item = response.meta['item']
        json_response = json.loads(response.text.replace('var index_info=',''))
        item['views'] = json_response['views']        
        return item