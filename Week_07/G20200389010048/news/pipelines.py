# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from news.dbhelper import DBHelper
from snownlp import SnowNLP
import time

class NewsPipeline(object):

    def __init__(self):
        self.file = open('news_comments.json', 'a+', encoding='utf-8')
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 情感分析
        item['nc_sentiment'] = self.get_sentiment_score(item['nc_content'])
        # 采集时间写入
        item['nc_utime'] = str(time.strftime('%Y-%m-%d %H:%M:%S'))
        # 转为json数据写入到文件
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        self.db.insert(item)
        return item

    def close_spider(self, spider):
        self.file.close()

    def get_sentiment_score(self, text):
        if text != '':
            s = SnowNLP(text)
            return str(s.sentiments)
        else:
            return '0'