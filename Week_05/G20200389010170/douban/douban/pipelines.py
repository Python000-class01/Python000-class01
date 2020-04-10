# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        short = item['short'] + "\n"
        # self.result = open("./result.txt", 'a+', encoding="utf-8")
        # self.result.write(str(short))
        # self.result.close()
        return item
