# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys2019.items import Rrys2019Item

url = 'http://www.rrys2019.com/'


class RrysspiderSpider(scrapy.Spider):
    name = 'rrysspider'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']


    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        names = movies.xpath('./ul/li/a/text()').extract()
        ranks = movies.xpath('./ul/li/span/text()').extract()
        links = movies.xpath('./ul/li/a/@href').extract()
        for rank, name, link in zip(ranks, names, links):
            item = Rrys2019Item()
            link = 'http://www.rrys2019.com'+link
            item['name'] = name
            item['rank'] = rank
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        driver = webdriver.PhantomJS()
        driver.get(item['link'])

        coverinfo = Selector(response=response).xpath('//div[@class="imglink"]/a/img/@src').extract()
        item['coverinfo'] = imginfo[0]
        view = driver.find_element_by_xpath('//label[@id="resource_views"]').text
        item['view'] = view
        try:
            levelinfo = Selector(response=response).xpath('//div[@class="level-item"]/img/@src').extract()
            level = levelinfo[0].replace("http://js.jstucdn.com/images/level-icon/", "").replace("-big-1.png", "")
            item['level'] = level
        except:
            item['level'] = 'no'

        yield item 
