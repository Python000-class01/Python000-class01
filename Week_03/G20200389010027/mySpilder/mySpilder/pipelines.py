# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class MyspilderPipeline(object):
    def process_item(self, item, spider):
        with codecs.open("top24hours.txt","a", "utf-8") as csv:
            line = f'"{item["title"]}","{item["score"]}","{item["level"]}","{item["views"]}","{item["faceImageUrl"]}","{item["files"][0]["path"]}"\r\n'
            print(line)
            csv.write(line)
        return item
