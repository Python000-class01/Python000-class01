# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from tencent.spiders.tencentSpider import TencentspiderSpider

from .settings import MYSQL_PWD, MYSQL_URL, MYSQL_POST, MYSQL_DB


class TencentPipeline(object):

    def open_spider(self, spider):
        if isinstance(spider, TencentspiderSpider):
            # 打开数据库连接
            self.connect = pymysql.connect(host=MYSQL_URL, user='root', passwd=MYSQL_PWD, db=MYSQL_DB,
                                           port=MYSQL_POST)
            self.cursor = self.connect.cursor()
            print("连接数据库成功")
            self.cursor.execute("DROP TABLE IF EXISTS comments")
            # 创建表
            sql = 'create table comments(time_ char(20), nick char(255), up int, comments char(255))'
            self.cursor.execute(sql)
            print("创建数据库成功")

    def close_spider(self, spider):
        if isinstance(spider, TencentspiderSpider):
            # 关闭数据库连接
            self.connect.close()

    def process_item(self, item, spider):
        if isinstance(spider, TencentspiderSpider):
            print('插入数据', item['time'], item['nick'], item['up'], item['comment'])
            # 插入数据
            self.cursor.execute(
                "insert into comments(time_, nick, up, comments ) values (%s, %s, %s, %s)",
                (item['time'], item['nick'], item['up'], item['comment']))
            self.connect.commit()

        return item
