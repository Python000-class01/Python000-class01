# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
import pymysql

class MySQLPipeline(object):

    def __init__(self):
        db = 'test'
        host = '10.100.3.12'
        port = 3306
        user = 'root'
        passwd = 'rootroot'


        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = (
            item['author'],
            item['date'],
            item['content'],
        )

        sql = 'INSERT INTO smzdm VALUES(%s,%s,%s)'
        self.db_cur.execute(sql, values)


