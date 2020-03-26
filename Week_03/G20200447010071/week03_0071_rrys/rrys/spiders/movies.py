# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys.items import RrysItem
import json

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']



    def parse(self, response):
        html = Selector(text=response.text)
        nodes = html.xpath('//div[@class="middle-box"]/div/div[@class="fl box top24"]/div[@class="box clearfix"]/ul/li/em[contains(text(),"电影")]/../a')
        for node in nodes:
            item = RrysItem()
            link, name = self.start_urls[0] + node.xpath('@href').extract()[0][1:], node.xpath('text()').extract()[0]
            item['name'] = name
            item['link'] = link
            rid = link.split('/')[-1]
            url = f'http://www.rrys2019.com/resource/index_json/rid/{rid}/channel/movie'
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.getViews)

    def parseDetail(self, response):
        html = Selector(text=response.text)
        ranking = html.xpath('/html/body/div[2]/div/div[1]/div[2]/div/ul/li[1]/p/text()').extract_first().strip()
        cover = html.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src').extract_first()
        level = html.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src').extract_first()
        if level:
            level = level.split('/')[-1].split('-')[0]
            response.meta['item']['level'] = level
        else:
            response.meta['item']['level'] = None
        response.meta['item']['ranking'] = ranking.split(':')[1]
        response.meta['item']['cover'] = cover
        yield response.meta['item']

    def getViews(self, response):
        datas = json.loads(response.text[15:])
        response.meta['item']['views'] = datas['views']
        yield scrapy.Request(url=response.meta['item']['link'], meta={'item': response.meta['item']}, callback=self.parseDetail)