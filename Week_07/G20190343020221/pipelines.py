class NewsPipeline(object):
    def process_item(self, item, spider):
        return item

# Define your item pipelines here
#
# from scrapy import log
import logging as log

from twisted.enterprise import adbapi
import time
import sqlite3

class DbSqlitePipeline(object):

    def __init__(self):
        """Initialize"""
        self.__dbpool = adbapi.ConnectionPool('sqlite3',
                database='news.sqlite',
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
            "insert or ignore into news(content_id, ndesc, event_time, event_date, collect_time) values (?,?,?,?,?)",(
                item['content_id'],
                item['ndesc'],
                item['event_time'],
                item['event_date'],
                time.time()
                )
            )
        # log.msg("Item stored in db", level=log.DEBUG)

    def handle_error(self,e):
        # log.err(e)
        pass

import pymysql
# pymysql.install_as_MySQLdb()
from twisted.enterprise import adbapi                   # 数据库连接池
from scrapy.utils.project import get_project_settings   # 导入seetings配置
class DBHelper(object):
    def __init__(self):
        """ 读取 settings.py 中的配置，可自行修改代码进行操作"""
        settings = get_project_settings()

        dbparams = dict(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],    # port 是 int 型
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

        self.__dbpool = dbpool

    def connect(self):
        return self.__dbpool

    def insert(self, item):
        # 封装insert操作
        #sql = "insert into news (content_id, ndesc, event_time, event_date, collect_time) values (%s,%s,%s,%s,%s)"
        sql = "insert ignore into news (content_id, ndesc, event_time, event_date, collect_time) values (%s,%s,%s,%s,%s)"
        query = self.__dbpool.runInteraction(self._conditional_insert, sql, item)   # 调用插入的方法
        query.addErrback(self._handle_error)                                        # 调用异常处理方法

        # log.msg("Item stored in db", level=log.DEBUG)
        #return item

    def _conditional_insert(self, canshu, sql, item):
        # 传items的数据，写入数据库中
        params = (item['content_id'], item['ndesc'], item['event_time'], item['event_date'], time.time())
        # params = (1, 1, 1, 1, 1)
        #print(params)
        canshu.execute(sql, params)

    def _handle_error(self, failue):
        """错误处理"""
        # log.err(failue)
        #print(failue)
        pass

    def __del__(self):
        """关闭连接"""
        try:
            self.__dbpool.close()
        except Exception as ex:
            print(ex)


# from scrapyDemo.db.dbhelper import DBHelper
# 数据库的操作DBHelper类，那么我们在scrapyDemo/db目录下创建dbhelper.py 模块，记得再创建一个__init__.py哦。
# <https://segmentfault.com/a/1190000011723728>，<https://tech1024.com/original/2959>
class MysqlPipeline(object):
    # 连接数据库
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据
        self.db.insert(item)
        return item

#    def close_spider(self, spider):
#         try:
#             self.__dbpool.close()
#         except Exception as ex:
#              log.err(e)
#              #print(ex)
