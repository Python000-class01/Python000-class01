# -*- coding: utf-8 -*-
import scrapy
import lxml.etree
from rrys.items import RrysItem
import json
import re

class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com']

    def start_requests(self):
        url = f'http://www.rrys2019.com'
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        selector = lxml.etree.HTML(response.text)
        for i in range(1,13):
            item = RrysItem()
            url = selector.xpath(
                f"/html/body/div[2]/div/div[1]/div/ul/li[{i}]/a/@href")
            link = f'http://www.rrys2019.com{url[0]}'
            print(f"link={link}")
            print(link.split('/')[-1])
            
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
    
    def parse2(self, response):
        link = response.url
        resourceId = link.split('/')[-1]
        item = response.meta['item']
        selector = lxml.etree.HTML(response.text)
        score = selector.xpath(
            "/html/body/div[2]/div/div[1]/div[2]/div/ul/li[1]/p/text()")[0].replace('本站排名:  ', '').replace('本站排名:', '').strip()
        print(f'score={score}')
        item['score'] = score
        imgSrc = selector.xpath(
            "/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src")[0]
        print(f'imgSrc={imgSrc}')
        s = re.search(r'/\w+?-big', imgSrc).group(0)
        print(s[1])
        item['imgSrc'] = s[1]
        # viewCount = selector.xpath("//label[@id='resource_views']")
        # print(f'viewCount={viewCount}')
        # item['viewCount'] = viewCount
        print(resourceId)
        viewLink = f'http://www.rrys2019.com/resource/index_json/rid/{resourceId}/channel/tv'
        yield scrapy.Request(url=viewLink, meta={'item': item}, callback=self.parse3)

    def parse3(self, response):
        item = response.meta['item']
        json_str = response.text[15:]
        data = json.loads(json_str)
        print(data['views'])
        item['viewCount'] = data['views']
        yield item
