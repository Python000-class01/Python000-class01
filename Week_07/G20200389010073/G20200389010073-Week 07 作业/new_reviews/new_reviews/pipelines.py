# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
from new_reviews.db.dbhelper_sql import DBHelper


class NewReviewsPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    # 注册到settings.py文件的ITEM_PIPELINES中，激活组件
    def process_item(self, item, spider):
        # 1.写入mysql
        self.db.insert(item)
        # 2.保存csv文件
        self.save_csvfile(item)
        return item

    def save_csvfile(self, item):
        """ 保存csv文件 """
        c_name = item['c_Name']
        c_time = item['c_Time']
        c_mark = item['c_Mark']
        c_sln_comment = item['c_Sln_comment']
        c_comment = item['c_Comment']
        self.article = open('./控方证人 短评.txt', 'a+', encoding='utf-8')
        self.article.write(f'评论人：{c_name}\n'
                           f'评分：{c_mark}\n'
                           f'评论时间：{c_time}\n'
                           f'评论情感分析：{c_sln_comment}\n'
                           f'评论内容：{c_comment}\n\n')
        self.article.close()

