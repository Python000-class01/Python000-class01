# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from doubanbook.items import DoubanbookItem
import time
from .. import DBAccess as db

class HongloumengSpider(scrapy.Spider):
    name = 'hongloumeng'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/subject/1007305/comments/']

    def parse(self, response):
        # print(response.url)
        # https://book.douban.com/subject/1007305/comments/new?p=2

        url = f'{response.url}new'
        while True:
            yield scrapy.Request(url=url, callback=self.parse2)
            # 每隔12小时扫描一次
            time.sleep(60*60*12)


    def parse2(self, response):
        print('response.url: ', response.url)
        commonitems = Selector(response=response).xpath('//li[@class="comment-item"]')
        for ci in commonitems:
            short = ci.xpath(
                './div[@class="comment"]/p[@class="comment-content"]/span[@class="short"]/text()').extract_first().strip()
            shorttime = ci.xpath(
                './div[@class="comment"]//span[@class="comment-info"]/span[2]/text()').extract_first().strip()
            # 判断数据是否已经读取过,读取过则返回
            sql = 'select count(*) from hlmshorts_new t where t.S_SHORTSTIME = "%s" and t.S_SHORTS = "%s"' % (shorttime, short)
            df = db.readtable(sql)
            cnt = df.iat[0, 0]
            if cnt > 0:
                return

            star = ci.xpath(
                './div[@class="comment"]/h3/span[@class="comment-info"]/span[1]/@title').extract_first().strip()
            vote = ci.xpath(
                './div[@class="comment"]/h3/span[@class="comment-vote"]/span[@class="vote-count"]/text()').extract_first().strip()
            # 在items.py定义DoubanbookItem
            item = DoubanbookItem()
            item['star'] = star
            item['vote'] = vote
            item['short'] = short
            item['shorttime'] = shorttime
            yield item
        # 取下一页数据
        nextpage1 = Selector(response=response).xpath(
            '//div[@class="paginator-wrapper"]/ul[@class="comment-paginator"]/li[last()]/a/@href')
        if nextpage1:
            nextpage = nextpage1.extract_first().strip()
            print('nextpage: ', nextpage)
            url = f'{HongloumengSpider.start_urls[0]}{nextpage}'
            yield scrapy.Request(url=url, callback=self.parse2)
            time.sleep(5)

