# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class HomeworkPipeline(object):
    def open_spider(self, spider):
        self.file = open('./rrysHotDownloadedMovies.csv', 'wb')
        self.exporter = CsvItemExporter(self.file,
                                        fields_to_export=["movie_title", "ranking", "grade", "look_time", 'cover_info'])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
