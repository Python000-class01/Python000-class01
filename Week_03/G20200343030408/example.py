# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapydemo1.items import Scrapydemo1Item

class ExampleSpider(scrapy.Spider):
    name = 'example' # entrance
    allowed_domains = ['rrys2019.com'] #restrict width #depth:top250 #width:wechat/qq login
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        titles = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li/a/text()')
        links = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li/a/@href')
        #print(titles.extract())
        #print(links.extract())
        for i in range(len(titles)):
            title = titles.extract()[i]
            link = 'http://www.rrys2019.com'+links.extract()[i]
            item = Scrapydemo1Item()
            item['title'] = title
            item['link'] = link
            #print(item)
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'level-item'})
        rank = content.find('img').get('src')
        item['rank'] = rank
        views = Selector(response=response).xpath('//label[@id="resource_views"]')
        print(views)
        yield item
