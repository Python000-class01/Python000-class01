# -*- coding: utf-8 -*-
import scrapy
import json
from news.items import NewsItem
import time
import random
from news.dbhelper import Sync_MySql

class HotnewsSpider(scrapy.Spider):
    name = 'hotnews'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-ircuyvh9815599&group=0&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user']

    def __init__(self):
        max_tr = Sync_MySql().query_max_time_and_rows()
        self.max_rows = max_tr['max_rows']
        self.max_time = max_tr['max_time']

    def parse(self, response):
        data = self.jsonp(response.text)
        tc_num = data['result']['count']['show'] # 评论总数
        print(f'网页最新评论总数：{tc_num}')
        print(f'数据库中的评论数：{self.max_rows}')
        if tc_num > self.max_rows:
            # 根据评论总数生成page数，并生成所有url
            count = tc_num - self.max_rows
            page = count // 10
            page_m = count % 10
            # 若评论不能整除10，则页数+1
            if page_m != 0:
                page += 1
            # 若评论小于10，则页数为1
            if page == 0:
                page = 1

            # 获取评论
            other_urls = [
                f'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-ircuyvh9815599&group=0&compress=0&ie=utf-8&oe=utf-8&page={i}&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user'
                for i in range(1, page + 1)]
            for url in other_urls:
                yield scrapy.Request(url=url, callback=self.get_comment_data)

    def get_comment_data(self, response):
        data = self.jsonp(response.text)
        # 判断请求结果是否正确，再输出结果
        if data['result']['status']['code'] == 0 and data['result']['status']['msg'] == "":
            # 获得数据
            item = NewsItem()
            for i in range(0, len(data['result']['cmntlist'])):
                if int(data['result']['cmntlist'][i]['against']) > self.max_time:
                    item['nc_mid'] = data['result']['cmntlist'][i]['mid']
                    item['nc_uid'] = data['result']['cmntlist'][i]['uid']
                    item['nc_nickname'] = data['result']['cmntlist'][i]['nick']
                    item['nc_content'] = data['result']['cmntlist'][i]['content']
                    item['nc_time'] = data['result']['cmntlist'][i]['time']
                    item['nc_time2'] = data['result']['cmntlist'][i]['against']
                    yield item


    # 解析jsonp数据，返回json格式数据
    def jsonp(self, text):
        text_rpre = text[text.find('(') + 1:]
        text_rsuffix = text_rpre[:-1]
        js = json.loads(text_rsuffix)
        # print(js)
        return js

