# -*- coding: utf-8 -*-
import scrapy
from spider.items import RRysItem
from scrapy.selector import Selector
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030')
import lxml.etree

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
            url = 'http://www.rrys2019.com/'
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # ###debug
        # items = []
        url='http://www.rrys2019.com/'

        books = Selector(response=response).xpath('//*[@class="box clearfix"]/ul/li')
        for book in books:
            title = book.xpath('./a/text()').extract_first().strip()
            link = book.xpath('./a/@href').extract_first().strip()
            link = url + link

            item = RRysItem()
            item['title'] = title
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)


    def parse2(self, response):

        item = response.meta['item']
        # content=Selector(response=response).xpath('//*[@id="score_list"]/div[1]//label/text()').extract()
        # print(//div[@class="fl-info"]/ul/li/strong/text())
        #
        # item['content'] = //*[@class="box score-box"]/ul/li[2]//div[1]/div/label/text()

        # front = response.xpath('//*[@class="imglink"]/a/img/@src').extract()
        order = response.xpath('//div[@class="box score-box"]/ul/li/p/text()').extract()
        view = response.xpath('//*[@class="level-item"]/img/@src').re('.*\/*([a-e])-big*')
        front = response.xpath('//*[@id="score_list"]/div[1]').re('\d+')

        item['front'] = front
        item['order'] = order
        item['view'] = view
        yield item