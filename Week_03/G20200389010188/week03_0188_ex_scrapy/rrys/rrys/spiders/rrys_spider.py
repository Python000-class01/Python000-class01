# -*- coding: utf-8 -*-
import scrapy
import re
import json
from scrapy.selector import Selector
#from fake_useragent import UserAgent
from rrys.items import RrysItem


#import sys
#import io

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030')

class RrysSpiderSpider(scrapy.Spider):
    name = 'rrys_spider'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def start_requests(self):
        start_url = 'http://www.rrys2019.com'
        #ua = UserAgent()
        #header = {}
        #header['user-agent'] = ua.random
        #yield scrapy.Request(start_url, callback = self.parse, headers=header)
        yield scrapy.Request(start_url, callback=self.parse)


    def parse(self, response):
        #print(response.text)
        for i in range(1,14):
            category = Selector(response=response).xpath(f'/html/body/div[2]/div/div[1]/div/ul/li[{i}]/em/text()').extract()
            title = Selector(response=response).xpath(f'/html/body/div[2]/div/div[1]/div/ul/li[{i}]/a/text()').extract()
            url = Selector(response=response).xpath(f'/html/body/div[2]/div/div[1]/div/ul/li[{i}]/a/@href')[0].extract()
            rank = Selector(response=response).xpath(f'/html/body/div[2]/div/div[1]/div/ul/li[{i}]/span/text()').extract()
            item = RrysItem()
            item['title'] = title
            item['rank'] = rank
            item['category'] = category
            item['url'] = f'http://www.rrys2019.com{url}'

            yield scrapy.Request(url=item['url'], meta={'item': item}, callback=self.parse2)

    
    def parse2(self,response):
        item = response.meta['item']
        cover_url = Selector(response=response).xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[1]/a/img/@src')[0].extract()
        classify_raw = Selector(response=response).xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/img/@src')[0].extract()
        classify = re.findall(r'http://js.jstucdn.com/images/level-icon/(.)-big-1.png', classify_raw)
        browse = Selector(response=response).xpath('//*[@id="resource_views"]/text()').extract()

        title = item['title']
        item['image_link'] = f'images/{title}.jpg'
        item['image_urls'] = [cover_url]
        item['classify'] = classify
        item['browse'] = browse

        print(item)

        '''解析出resource id'''
        url = item['url']
        if url is not None:
            resource_id = re.findall(r'http://www.rrys2019.com/resource/(\d+)', url)
            
            if resource_id is not None:
                print(f'resource_id is {resource_id[0]}')
                browse_js = f'http://www.rrys2019.com/resource/index_json/rid/{resource_id[0]}/channel/tv'
                yield scrapy.Request(url=browse_js, meta={'item': item}, callback=self.parse3)
            else:
                yield item
    

    def parse3(self, response):
        item = response.meta['item']

        resjs = re.findall(r'var index_info=([\s\S]+)', response.text)
        if resjs is not None:
            print(f'resjs is {resjs}')
            jsobj = json.loads(resjs[0])
            print(f'jsobj is {jsobj}')
            views = jsobj['views']
            print(f'views is {views}')
            item['browse'] = views

        yield item



            
