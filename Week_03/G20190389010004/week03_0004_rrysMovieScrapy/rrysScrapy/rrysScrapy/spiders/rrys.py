# -*- coding: utf-8 -*-
import scrapy
# from bs4 import BeautifulSoup
from scrapy.selector import Selector
from rrysScrapy.items import RrysscrapyItem

url = 'http://www.rrys2019.com/'

class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        movie_List = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li') 
        # print(movie_List)
        
        for movie in movie_List:
            title = movie.xpath('./a/text()').extract_first().strip()
            link = movie.xpath('./a/@href').extract_first().strip()
            link  = url + link
            
            item = RrysscrapyItem()            
            item['title'] = title
            # item['link'] = link
            # print(title)
            # print(link)
            yield scrapy.Request(url=link, meta={'item':item}, callback=self.parseDetail)
        
    def parseDetail(self, response):
        rank = Selector(response=response).xpath('//p[@class="f4"]/text()').re('\d+')
        # print(rank[0])
        level = Selector(response=response).xpath('//div[@class="level-item"]/img/@src').re('.*\/*([a-e])-big*')
        # print(level[0].upper())
        views = Selector(response=response).xpath('//*[@id="score_list"]/div[1]').re('\d+')
        # print(views[1])        
        coverInfo = Selector(response=response).xpath('//div[@class="imglink"]/a/img/@src').extract()
        # print(coverInfo[0])
        item = response.meta['item']
        item['rank'] = rank[0]
        item['level'] = level[0].upper()+'级'
        item['views'] = views[1]
        item['coverInfo'] = coverInfo[0]
        # print(item)
        yield item

