# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from bilibili_news.dbutil import MyDbUtil
class BilibiliNewsPipeline(object):
    dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'db_test_helper',
    'charset':'utf8mb4'
    }   
    def __init__(self):
        self.dbutils = MyDbUtil(self.dbInfo)
    def process_item(self, item, spider):
        self.dbutils.insert("bilibili_comments",[item.__dict__['_values'],])
