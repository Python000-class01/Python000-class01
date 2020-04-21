# -*- coding: utf-8 -*-
import scrapy
from ..items import PttItem
import time
import lxml.etree


class PttGossipingSpider(scrapy.Spider):

    name = 'ptt_gossiping'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html']

    def start_requests(self):
        url = "https://www.ptt.cc/bbs/Gossiping/M.1587447015.A.4FC.html"
        yield scrapy.Request(url, cookies={'over18': '1'}, callback=self.parse)

    def parse(self, response):
        item = PttItem()
        cmts = []
        selector = lxml.etree.HTML(response.text)
        title = selector.xpath('//*[@id="main-content"]/div[3]/span[2]/text()')
        for i in range(11,12):
            cmt = selector.xpath('//*[@id="main-content"]/div['+str(i)+']/span[3]/text()')[0][2:]
            cmts.append(cmt)
        item['title'] = str(title)
        item['cmt'] = str(cmts)
        yield item