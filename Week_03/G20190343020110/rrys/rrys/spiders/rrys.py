# -*- coding: utf-8 -*-
import scrapy
import lxml.etree
from rrys.items import RrysItem

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
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
    
    def parse2(self, response):
        item = response.meta['item']
        selector = lxml.etree.HTML(response.text)
        score = selector.xpath(
            "/html/body/div[2]/div/div[1]/div[2]/div/ul/li[1]/p/text()")[0].replace('本站排名:  ', '').replace('本站排名:', '').strip()
        print(f'score={score}')
        item['score'] = score
        imgSrc = selector.xpath(
            "/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src")[0]
        print(f'imgSrc={imgSrc}')
        item['imgSrc'] = imgSrc
        viewCount = selector.xpath('//*[@id="resource_views"]/text()')
        print(f'viewCount={viewCount}')
        item['viewCount'] = viewCount
        yield item
