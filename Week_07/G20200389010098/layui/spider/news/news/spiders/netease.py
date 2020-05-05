# -*- coding: utf-8 -*-
import scrapy
import json
import lxml.etree
from time import sleep,strptime,mktime
import math
import re
from snownlp import SnowNLP
from news.items import CommentItem
import sqlalchemy as sqlmy
from sqlalchemy.orm import sessionmaker
from news.config import mysql_config as mc
from news.models import HzSpecialUrl as su


class NeteaseSpider(scrapy.Spider):
    offset = 0
    limit=30
    name = 'netease'
    allowed_domains = ['163.com']
    start_urls = ['http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/FA039QJ300019B3E/comments/newList?ibc=newspc&limit=30&showLevelThreshold=72&headLimit=1&tailLimit=2&offset=30&callback=jsonp_1587345047654&_=1587345047655']
    base_url='http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/{sub_id}/comments/newList?ibc=newspc&limit={limit}&showLevelThreshold=72&headLimit=1&tailLimit=2&offset={offset}&callback=jsonp_1587345047654&_=1587345047655'
    def __init__(self,url_id=1, *args, **kwargs):
        super(NeteaseSpider, self).__init__(*args, **kwargs)
        if (url_id is None):
            print("参数缺失")
            return True
        self.engine = sqlmy.create_engine(
                        "mysql+pymysql://"+mc['user']+":"+mc['psw']+"@"+mc['host']+":"+mc['port']+"/"+mc['db_name']+"?charset="+mc['charset'],
                        echo=False)
        self.url_id=int(url_id)
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        get_data = session.query(su).filter(su.id == self.url_id).first()
        if (get_data is None):
            print("抓取地址不存在")
            return True
        self.sub_id = str(get_data.spider_key)
        self.special_id = int(get_data.special_id)
    def start_requests(self):

        yield scrapy.Request(url=self.base_url.format(sub_id=self.sub_id, limit=str(self.limit), offset=str(self.offset)), callback=self.parse_count)

    def jsonp_filter(self, text):
        html=text.strip()
        a=html.split("(")
        json_str=html[len(a[0])+1:-2]
        loaded_json = json.loads(json_str)
        return loaded_json

    def parse_count(self, response):
        json_dict=self.jsonp_filter(response.text)
        sum=json_dict['newListSize']
        for i in range(0, math.ceil((sum/self.limit))):
        #for i in range(0, 1):
            url = self.base_url.format(sub_id=self.sub_id, limit=str(self.limit), offset=str(i*self.limit))
            #print(url)
            yield scrapy.Request(url=url, dont_filter=True , callback=self.parse)


    def toStamp(self, string):
        timeArray = strptime(string, "%Y-%m-%d %H:%M:%S")
        return int(mktime(timeArray))
    def parse(self, response):
        json_dict=self.jsonp_filter(response.text)
        for i in json_dict['comments']:
            item = CommentItem()
            item['cid'] = json_dict['comments'][i]['commentId']
            item['sub_id'] = self.sub_id
            item['url_id'] = self.url_id
            item['special_id'] = self.special_id
            item['comment'] = json_dict['comments'][i]['content']
            s2 = SnowNLP(json_dict['comments'][i]['content'])
            item['score1'] = s2.sentiments
            item['info_time'] = self.toStamp(json_dict['comments'][i]['createTime'])
            #print(item)
            # exit()
            yield item

