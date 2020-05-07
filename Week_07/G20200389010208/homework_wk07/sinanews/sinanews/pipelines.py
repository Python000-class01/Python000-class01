# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# import csv

# class SinanewsPipeline(object):

#     def __init__(self):
#         self.article = open('./sinanews.csv', 'a+', encoding='utf-8')

#     # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
#     def process_item(self, item, spider):
#         user = item['user']
#         comment = item['comment']
#         timestamp = item['timestamp']
#         writer = csv.writer(self.article)
#         writer.writerow([user, comment, timestamp])

#         return item

import json
from logging import Logger
from twisted.enterprise import adbapi
from sinanews.db.dbhelper import DBHelper
import codecs
from logging import log
from scrapy.utils.project import get_project_settings
from snownlp import SnowNLP

class SinanewsPipeline(object):

    def __init__(self):
        self.file = open('sinanews.json', 'a+', encoding='utf-8')
        self.db = DBHelper()

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        s = SnowNLP(item['short']).sentiments
        self.db.insert(item, s)
        return item

    def close_spider(self, spider):
        self.file.close()