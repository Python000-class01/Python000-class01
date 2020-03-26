# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys2019data.items import Rrys2019DataItem
from selenium import webdriver


class Rrys2019Spider(scrapy.Spider):
    name = 'rrys2019'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']


    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]')
        grades = movies.xpath('./ul/li/span/text()').extract()
        names = movies.xpath('./ul/li/a/text()').extract()
        links = movies.xpath('./ul/li/a/@href').extract()
        # items = []
        for grade, name, link in zip(grades, names, links):
            item = Rrys2019DataItem()
            link = 'http://www.rrys2019.com'+link
            item['grade'] = grade
            item['name'] = name
            item['link'] = link
            # items.append(item)
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        driver = webdriver.PhantomJS()
        driver.get(item['link'])

        imginfo = Selector(response=response).xpath('//div[@class="imglink"]/a/img/@src').extract()
        item['imginfo'] = imginfo[0]
        view = driver.find_element_by_xpath('//label[@id="resource_views"]').text
        item['view'] = view
        try:
            levelinfo = Selector(response=response).xpath('//div[@class="level-item"]/img/@src').extract()
            level = levelinfo[0].replace("http://js.jstucdn.com/images/level-icon/", "").replace("-big-1.png", "")
            item['level'] = level
        except:
            item['level'] = 'no'

        yield item