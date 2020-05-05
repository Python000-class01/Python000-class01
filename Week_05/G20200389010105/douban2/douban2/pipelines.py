# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os
import json
from douban2.dbhelper import DBHelper

class Douban2Pipeline(object):

    def __init__(self):
        self.file = open('movie_reviews.json', 'a+', encoding='utf-8')
        self.db = DBHelper()

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        self.db.insert(item)
        return item

    def close_spider(self, spider):
        self.file.close()

# class Douban2Pipeline(object):
#
#     def __init__(self):
#         self.headers = [
#             '评论分数',
#             '评论内容']
#         self.file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\movie_reviews.csv'
#         with open(self.file_path, 'a+', newline='', encoding='utf-8') as file:
#             csv_file = csv.writer(file)
#             csv_file.writerow(self.headers)
#
#     def process_item(self, item, spider):
#         self.export_csv(item)
#         print('输出完毕！')
#         return item
#
#     def export_csv(self, data):
#         fieldnames = [
#             'm_rating',
#             'm_content']
#         with open(self.file_path, 'a+', newline='', encoding='utf-8') as file:
#             csv_file = csv.DictWriter(file, fieldnames=fieldnames)
#             csv_file.writerow(data)

