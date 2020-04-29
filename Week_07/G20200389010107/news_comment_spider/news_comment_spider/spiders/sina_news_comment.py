# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.selector import Selector
from ..items import NewsCommentItem
from pprint import pprint

class SinaNewsCommentSpider(scrapy.Spider):
    name = 'sina_news_comment'
    allowed_domains = ['sina.com']
    
    #sina news url rule example:
    #news: https://tech.sina.com.cn/i/2020-04-28/doc-iircuyvi0248549.shtml
    #comment page: http://comment5.news.sina.com.cn/comment/skin/default.html?channel=kj&newsid=comos-ircuyvi0248549
    #comment json: http://comment5.news.sina.com.cn/page/info?format=json&channel=kj&newsid=comos-ircuyvi0248549
    #key point: doc-xxx -> newsid=comos-xxx & channel=yy

    start_urls = ['http://comment5.news.sina.com.cn/page/info?format=json&channel=kj&newsid=comos-ircuyvi0248549']

    
    
    def parse(self, response):
        print(f"url: {response.url}")
        response_json = json.loads(response.body_as_unicode())
        comments = response_json["result"]["cmntlist"]
        #pprint(comments)
        #print(comments)
        for comment in comments:
            item = NewsCommentItem()
            #pprint(comment)
            item["time_stamp"] = comment["time"]
            item["comment_text"] = comment["content"]
            #pprint(item)
            yield item
            
        

        

