# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class ClearPipeline(object):
    # def __init__(self):
        # self.article = None

    def process_item(self, item, spider):
        print('短评长度：', len(item['short']))
        if len(item['short']) > 0:
            return item

