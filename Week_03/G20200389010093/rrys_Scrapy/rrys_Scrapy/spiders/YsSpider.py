# -*- coding: utf-8 -*-
import scrapy
import json
from rrys_Scrapy.items import RrysScrapyItem
from scrapy.http import Request
from scrapy.selector import Selector
from urllib import parse

import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class YsspiderSpider(scrapy.Spider):
    name = 'YsSpider'
    # allowed_domains = ['http://www.rrys2019.com/']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        selector=Selector(response)
        for i in selector.xpath('//div[@class="box clearfix"]//li'):
            item = RrysScrapyItem()
            if i.xpath('./em/text()').extract_first()[-1]=='影':
                item['channel']='movie'
            else:
                item['channel'] = 'tv'
            item['position']=i.xpath('./span/text()').extract_first()
            item['name'] = i.xpath('./a/text()').extract_first()
            item['link'] = i.xpath('./a/@href').extract_first()
            item['id']=item['link'].split('/')[-1]
            url = response.url +'resource/index_json/rid/' + item['id'] + '/channel/'+item['channel']
            yield scrapy.Request(url,meta={'ys':item},callback=self.parse1)

    def parse1(self,response):
        item = response.meta['ys']
        result =response.text[15:]
        res=json.loads(result.replace('\/','/'))
        item['views']=res['views']
        url = parse.urljoin('http://www.rrys2019.com/',item['link'])
        yield  scrapy.Request(url,meta={'ys':item},callback=self.parse2)

    def parse2(self,response):
        item = response.meta['ys']
        selector = Selector(response)
        str1 = selector.xpath('//p[@class="f4"]/text()').extract_first()
        item['rank'] = str1[-3]
        item['cover_link'] = selector.xpath('//div[@class="imglink"]/a/@href').extract_first()
        str2 = selector.xpath('//div[@class="level-item"]/img/@src').extract_first()
        item['level']=str2.split('-')[1][-1]
        yield item



            




