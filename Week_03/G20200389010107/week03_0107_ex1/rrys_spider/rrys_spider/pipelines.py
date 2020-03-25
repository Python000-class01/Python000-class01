# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter

result_json_path = "result.json"


class RrysSpiderPipeline(object):

    def open_spider(self, spider):
        self.file = open(result_json_path, "wb")
        self.exporter = JsonItemExporter(
            self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        print(f"spider result is saved to {result_json_path}")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
