# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapyjop.items import ScrapyjopItem
from selenium import webdriver
import time


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']


    def parse(self, response):
        moves = Selector(response = response).xpath('//div[@class="box clearfix"]//li')
        for move in moves:
            mingci = move.xpath('./span/text()')
            name = move.xpath('./a/@title')
            link = f'http://www.rrys2019.com{move.xpath("./a/@href").extract_first().strip()}'
            item = ScrapyjopItem()
            item['move_name'] = name.extract_first().strip()
            item['move_url'] = link

            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self,response):
        item = response.meta['item']
        fengmian = Selector(response = response).xpath('//div[@class="imglink"]/a/@href').extract_first().strip()
        fenji = Selector(response = response).xpath('//div[@class="fl-info"]//img/@src').extract_first().strip()

        browser = webdriver.Chrome('E:\PycharmProjects\chromedriver_win32\chromedriver.exe')
        browser.get(item['move_url'])
        liulan = browser.find_element_by_xpath('//*[@id="resource_views"]').text
        mingci = browser.find_element_by_xpath('//p[@class="f4"]').text
        browser.close()
        if liulan == "":
            liulan = "无法获取浏览次数"

        item['move_paihang'] = mingci
        item['move_fenji'] = fenji
        item['move_fengmian_url'] = fengmian
        item['move_see_num'] = liulan

        yield item














