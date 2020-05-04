# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import json
from homework.items import HomeworkItem

# url = 'http://comment5.news.sina.com.cn/comment/skin/default.html?channel=kj&newsid=comos-ircuyvh8010191&group=0'
# url = 'https://tech.sina.com.cn/mobile/n/n/2020-04-15/doc-iircuyvh8010191.shtml'

url = 'http://comment5.news.sina.com.cn/page/info?format=json&channel=kj&newsid=comos-ircuyvh8010191'

class SinacommentSpider(scrapy.Spider):
    name = 'sinacomment'
    allowed_domains = ['www.sina.com.cn']
    start_urls = ['http://www.sina.com.cn/']

    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        comment_list = result['result']['cmntlist']
        # print(comment_list)
        for comment in comment_list:
            # print(comment)
            content = comment['content']
            time = comment['time']
            mid = comment['mid']
            # print(content)
            # print(time)

            item = HomeworkItem()
            item['mid'] = mid
            item['content'] = content
            item['time'] = time

            # print(item)

            yield(item)


