# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class BookDoubanPipeline(object):
    def process_item(self, item, spider):
        with codecs.open(f'comment_{spider.bookid}.txt','a','utf-8') as csv:
            line = f'"{item["idx"]}","{item["content"]}","{item["star"]}"\r\n'
            print(line)
            csv.write(line)
