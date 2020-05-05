# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class MoviePipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        rank =item['num']
        title = item['title']
        level = item['level']
        resource_views = item['resource_views']
        self.items =open('./Movie.txt','a',encoding='utf-8')
        writety = f'{rank}\t{title}\t{level}\t{resource_views}\n'
        self.items.write(writety)
        self.items.close()
        return item
