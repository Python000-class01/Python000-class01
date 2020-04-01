# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json

class Hour24HotmovierrysPipeline(object):

    def open_spider(self, spider):
        self.file = open('./hot_movie.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        print('process_item', item)
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item
