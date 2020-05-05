# -*- coding: gbk -*-
import scrapy
from qsbk.items import QsbkItem
import json

class QbSpider(scrapy.Spider):
    name = 'qb'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-ircuyvi0165078&group=0&compress=0&ie=utf-8&oe=utf-8&page=2&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp_1588171987409&_=1588171987409']

    def parse(self, response):
        # comments = response.text
        # print(str(comments,encoding='utf-8',errors='ignore'))
        text = json.loads(response.text[20:-1])
        count = text['result']['count']['thread_show']
        page = int(count/10)+1
        for i in range(1,page+1):
            url = f'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-ircuyvi0165078&group=0&compress=0&ie=utf-8&oe=utf-8&page={i}&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp_1588171987409&_=1588171987409'
            yield scrapy.Request(url=url,callback=self.parse2)

    def parse2(self,response):
        try:
            text = json.loads(response.text[20:-1])
            comment_lists = text['result']['cmntlist']
            # print(comment_lists)
            for comment in comment_lists:
                item = QsbkItem()
                item['mid'] = comment['mid']
                item['content'] = comment['content']
                item['nick'] = comment['nick']
                # print(item)
                yield item
        except:
            pass

