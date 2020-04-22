# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sqlite3
# from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem


class ZhihuScrapyPipeline(object):
    def __init__(self, sqlite_file, sqlite_table):
        # filter duplicate item
        # self.ids_seen = set()
        
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file = crawler.settings.get('SQLITE_FILE'),
            sqlite_table = crawler.settings.get('SQLITE_TABLE', 'items'),
        )

    def open_spider(self, spider):
        # self.file = open('douban.json', 'ab')
        # self.exporter = JsonItemExporter(self.file, encoding='utf-8')
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()
        # self.exporter.start_exporting()

    def close_spider(self, spider):
        # self.exporter.finish_exporting()
        # self.file.close()
        self.conn.close()

    def process_item(self, item, spider):
        # if item['id'] in self.ids_seen:
        #     raise DropItem('Duplicate item found: %s' % item)
        # else:
        #     self.ids_seen.add(item['id'])
        #     self.exporter.export_item(item)
        #     return item
        check_sql = 'select id from ? where id = ?'
        self.cur.execute(check_sql, [self.sqlite_table, item['id']])
        if self.cur.fetchone():
            raise DropItem('Duplicate item found: %s' % item)
        else:
            insert_sql = 'insert into ? values (?, ?, ?)'
            self.cur.execute(insert_sql, [self.sqlite_table, item['id'], item['user_name'], item['content']])
            self.conn.commit()

            return item

