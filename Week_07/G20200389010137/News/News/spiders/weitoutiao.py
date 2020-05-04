# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector
from News.items import NewsItem

import json
import datetime


class WeitoutiaoSpider(scrapy.Spider):
    name = 'weitoutiao'
    allowed_domains = ['weitoutiao.zjurl.cn']
    start_urls = ['http://weitoutiao.zjurl.cn/']

    def start_requests(self):
        query_id = 1656810113086509
        tab_id = 1656810113086525
        category = 'forum_flow_subject'
        is_preview = 1
        request_source = 1
        stream_api_version = 82
        aid = 13
        for i in range(0, 5):
            app_extra_params = {"module_id": "1656810113087501","offset": 200+i*20}
            url = f'https://weitoutiao.zjurl.cn/api/feed/forum_flow/v1/?query_id={query_id}&tab_id={tab_id}&category={category}&is_preview={is_preview}&request_source={request_source}&stream_api_version={stream_api_version}&aid={aid}&app_extra_params={app_extra_params}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = NewsItem()
        content = json.loads(response.text)['data'][0]['content']
        subRawDatasList = json.loads(content)["sub_raw_datas"]
        for i in subRawDatasList:
            item['content_id'] = i['raw_data']['content_id']
            item['ndesc'] = i['raw_data']['desc']
            item['event_time'] = i['raw_data']['event_time']
            item['event_date'] = datetime.datetime.fromtimestamp(item['event_time']).strftime('%Y-%m-%d')
            # print(content_id, event_time, desc)
            yield item

