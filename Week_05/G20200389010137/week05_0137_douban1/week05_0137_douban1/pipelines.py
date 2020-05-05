# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from threading import Thread, Lock
lock = Lock()

class Week050137Douban1Pipeline(object):

    def __init__(self):
        self.csvfile = open('./douban.csv', 'w', encoding='utf-8', newline='')
        self.fieldnames = ['star', 'short_content']
        self.writer = csv.writer(   self.csvfile,
                                    delimiter=',',
                                    quotechar='\'', quoting=csv.QUOTE_MINIMAL
                                    )
        self.writer.writerow(self.fieldnames)

    def process_item(self, item, spider):
        star = item['star']
        shortContent = item['shortContent']
        self.writer.writerow([star, shortContent])
        return item

    def close_spider(self, spider):
        # print('关闭.................')
        self.csvfile.close()

import pymysql
pymysql.install_as_MySQLdb()
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings
class DBHelper(object):
    def __init__(self):
        """ 读取 settings.py 中的配置，可自行修改代码进行操作"""
        settings = get_project_settings()

        dbparams = dict(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )

        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

        self.__dbpool = dbpool

    def connect(self):
        return self.__dbpool

    def insert(self, item):

        sql = "insert into book(star, short_content) values(%s, %s)"
        query = self.__dbpool.runInteraction(self._conditional_insert, sql, item)
        query.addErrback(self._handle_error)

        return item

    def _conditional_insert(self, canshu, sql, item):

        params = (item['star'], item['shortContent'])
        canshu.execute(sql, params)

    def _handle_error(self, failue):
        """错误处理"""
        print(failue)

    def __del__(self):
        """关闭连接"""
        try:
            self.__dbpool.close()
        except Exception as ex:
            print(ex)


# from scrapyDemo.db.dbhelper import DBHelper
# 数据库的操作DBHelper类，那么我们在scrapyDemo/db目录下创建dbhelper.py 模块，记得再创建一个__init__.py哦。
# <https://segmentfault.com/a/1190000011723728>
class MysqlPipeline(object):
    # 连接数据库
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据
        self.db.insert(item)
        return item

    # def close_spider(self, spider):
    #     try:
    #         self.__dbpool.close()
    #     except Exception as ex:
    #         print(ex)