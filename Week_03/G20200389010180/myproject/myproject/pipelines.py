# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

# class MyprojectPipeline(object):
#     def process_item(self, item, spider):
#         return item

class CsvPipeline(object):
    def __init__(self):
        self.file = open("rrys_output.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='gb18030')

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
