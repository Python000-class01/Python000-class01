# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import json
from homework.items import HomeworkItem

url = 'http://comment5.news.sina.com.cn/page/info?format=json&channel=kj&newsid=comos-ircuyvh8010191'


class SinaCommentSpider(scrapy.Spider):
    name = 'sina_comment'
    allowed_domains = ['www.sina.com.cn']
    start_urls = ['http://www.sina.com.cn/']

    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        comment_list = result['result']['cmntlist']
        for comment in comment_list:
            content = comment['content']
            time = comment['time']
            mid = comment['mid']

            item = HomeworkItem()
            item['mid'] = mid
            item['content'] = content
            item['time'] = time

            yield item
