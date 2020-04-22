# -*- coding: utf-8 -*-
import scrapy
import json
from sinaComments.items import SinacommentsItem


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn', 'restapi.amap.com', 'www.baidu.com']
    start_urls = ['http://sina.com.cn/']

    def start_requests(self):
        self.headers = {
            "Referer": "http://comment5.news.sina.com.cn/comment/skin/default.html?channel=gj&newsid=comos-ircuyvh7852499&group=0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }
        url = 'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gj&newsid=comos-ircuyvh7852499&group=0&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=1&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp&_=1587113178957'
        yield scrapy.Request(url=url, callback=self.get_comment_list)

    def get_comment_list(self, response):
        text = json.loads(response.text[6:-1])
        count = text['result']['count']['thread_show']
        page = int(count / 10) + 1
        for i in range(1, page+1):
            url = f'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gj&newsid=comos-ircuyvh7852499&group=0&compress=0&ie=utf-8&oe=utf-8&page={i}&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp&_=1587113178957'
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)
    
    def parse(self, response):
        text = json.loads(response.text[6:-1])
        comment_lists = text['result']['cmntlist']
        for comment in comment_lists:
            item = SinacommentsItem()
            item['mid'] = comment['mid']
            item['content'] = comment['content']
            item['nick'] = comment['nick']
            item['area'] = comment['area']
            item['time'] = comment['time']
            yield scrapy.Request(url=f'https://restapi.amap.com/v3/geocode/geo?key=09219797a0e0b0d4948e188497a05c27&address={comment["area"]}', meta={'item': item}, callback=self.getLocation)


    def getLocation(self, response):
        data = json.loads(response.text)
        print(data)
        if data['status'] == "1" and len(data['geocodes']) > 0:
            response.meta['item']['area'] = data['geocodes'][0]['location']
        yield response.meta['item']
