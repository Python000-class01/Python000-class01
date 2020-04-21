# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsPipeline(object):
    def process_item(self, item, spider):
        return item

# Define your item pipelines here
#
from scrapy import log
from twisted.enterprise import adbapi
import time
import sqlite3

class DbSqlitePipeline(object):

    def __init__(self):
        """Initialize"""
        self.__dbpool = adbapi.ConnectionPool('sqlite3',
                database='/Volumes/S1-Document/Flask-Train/flask06-gentelella/instance/news.sqlite',
                check_same_thread=False)

    def shutdown(self):
        """Shutdown the connection pool"""
        self.__dbpool.close()

    def process_item(self,item,spider):
        """Process each item process_item"""
        query = self.__dbpool.runInteraction(self.__insertdata, item, spider)
        query.addErrback(self.handle_error)
        return item

    def __insertdata(self,tx,item,spider):
        """Insert data into the sqlite3 database"""
        # spidername=spider.name
        # for img in item['images']:
        # tx.execute("select * from news where content_id = ?", (item['content_id'],))
        # result = tx.fetchone()
        # if result:
        #     log.msg("Already exists in database", level=log.DEBUG)
        # else:
        tx.execute(
            # "insert into news(content_id, desc, event_time, event_date, collect_time) values (?,?,?,?,?)",(
            "insert or ignore into news(content_id, desc, event_time, event_date, collect_time) values (?,?,?,?,?)",(
                item['content_id'],
                item['desc'],
                item['event_time'],
                item['event_date'],
                time.time()
                )
            )
        log.msg("Item stored in db", level=log.DEBUG)

    def handle_error(self,e):
        log.err(e)