# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

# class PttPipeline(object):
    
#     def __init__(self):
#         pass
#     # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常

#     def process_item(self, item, spider):
#         title = item['title']
#         cmt = item['cmt']
#         output = f'{title}\t{cmt}\n\n'
#         self.article = open('./ptt_gossiping.txt', 'a+', encoding='utf-8')
#         self.article.write(output)
#         self.article.close()
#         return item

class PttPipeline(object):
    # pass
    # def __init__(self):
    #     pass
    # def open_spider(self, spider):
    #     # Database Settings
    #     db = spider.settings.get('MYSQL_DB_NAME')
    #     host = spider.settings.get('MYSQL_DB_HOST')
    #     port = spider.settings.get('MYSQL_PORY')
    #     user = spider.settings.get('MYSQL_USER')
    #     password = spider.settings.get('MYSQL_PASSWORD')
    #     # Database Connecting
    #     self.connection = pymysql.connect(
    #         host = host,
    #         port = port,
    #         user = user,
    #         password= password,
    #         db = db,
    #         cursorclass= pymysql.cursors.DictCursor
    #         )

    # def close_spider(self, spider):
    #     self.connection.close()

    # def process_item(self, item, spider):
    #     pass

    # def insert_to_mysql(self, item):
    #     values = (
    #         item['title'],
    #         item['cmt']
    #         )
    #     with self.connection.cursor() as cursor:
    #         sql = 'INSERT INTO gossiping (title, cmt) VALUES (%s, %s)'
    #         cursor.execute(sql, values)
    #         self.connection.commit()

    # 打开数据库
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME','ptt')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '')

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
            item['title'],
            item['cmt'],
        )

        sql = 'INSERT INTO gossiping (title, cmt) VALUES (%s,%s)'
        self.db_cur.execute(sql, values)