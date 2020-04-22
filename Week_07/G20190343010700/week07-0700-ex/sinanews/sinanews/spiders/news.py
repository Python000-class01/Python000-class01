# -*- coding: utf-8 -*-
import scrapy
from sinanews.items import SinanewsItem
import json


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://comment.sina.com.cn/page/info?version=1&format=json&channel=kj&newsid=comos-irczymi7245482&group=0&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&']

    def parse(self, response):
        item = SinanewsItem()
        comments =json.loads(response.text)
        news_comments = []
        users = []
        time = []
        for i  in  range(len(comments['result']['cmntlist'])):
            print(comments['result']['cmntlist'][i]['content'])
            news_comments.append(comments['result']['cmntlist'][i]['content'])
            users.append(comments['result']['cmntlist'][i]['uid'])
            time.append(comments['result']['cmntlist'][i]['time'])
        item['news_comments'] = news_comments 
        item['users'] = users
        item['time'] = time
        yield item
        
