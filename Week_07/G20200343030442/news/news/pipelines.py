# -*- coding: utf-8 -*-

import csv

import json
from logging import Logger
from twisted.enterprise import adbapi
from news.db.dbhelper import DBHelper
import codecs
from logging import log
from scrapy.utils.project import get_project_settings


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class NewsPipeline(object):

    def __init__(self):

        self.row = []
        self.article = open('./newsdownloadsinfo.txt', 'a+', encoding='utf-8')

        Header = f'新闻标题:,\t评论信息:,\n\n'
        self.article.writelines(Header) 

        self.file = open('blog.json', 'a+', encoding='utf-8')
        self.db = DBHelper()
    
    def process_item(self, item, spider):

        self.article = open('./newsdownloadsinfo.txt', 'a+', encoding='utf-8')

        new_title = item['new_title']
        new_comment = item['new_custcomment']

        output = f'{new_title}\t{new_comment}\n\n'
        self.article.write(output)
        self.article.close()

        
        # 保存为json格式 并并入库
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        self.db.insert(item)

        # 保存为csv格式
        Header_csv = ['新闻标题','评论信息']
        self.row.append((new_title,new_comment))
        with open('./newsdownloadsinfo.csv','w',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(Header_csv)
            writer.writerows(self.row)

        return item

    def close_spider(self, spider):
        self.file.close()

#注册到settings.py文件的ITEM_PIPELINES中，激活组件



