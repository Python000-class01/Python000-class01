# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from doubanbook.items import DoubanbookItem


class HongloumengSpider(scrapy.Spider):
    name = 'hongloumeng'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/subject/1007305/comments/']

    # star = ci.xpath('./div[@class="comment"]/h3/span[@class="comment-info"]/span[@class="user-stars allstar50 rating"]/@title').extract_first().strip()
    # vote = ci.xpath('./div[@class="comment"]/h3/span[@class="comment-vote"]/span[@class="vote-count"]').extract_first().strip()
    # short = ci.xpath('./div[@class="comment"]/p[@class="comment-content"]/span[@class="short"]').extract_first().strip()

    def parse(self, response):
        print(response.url)
        commonitems = Selector(response=response).xpath('//li[@class="comment-item"]')
        # print(commonitems)
        for ci in commonitems:
            star = ci.xpath(
                './div[@class="comment"]/h3/span[@class="comment-info"]/span[1]/@title').extract_first().strip()
            vote = ci.xpath(
                './div[@class="comment"]/h3/span[@class="comment-vote"]/span[@class="vote-count"]/text()').extract_first().strip()
            short = ci.xpath('./div[@class="comment"]/p[@class="comment-content"]/span[@class="short"]/text()').extract_first().strip()

            # print(star)
            # print(vote)
            # print(short)
            # 在items.py定义DoubanbookItem
            item = DoubanbookItem()
            item['star'] = star
            item['vote'] = vote
            item['short'] = short
            yield item
            # print(item['star'])
            # print(item['vote'])
            # print(item['short'])
            # yield scrapy.Request(url=item['link'], meta={'item': item}, callback=self.parse2)

