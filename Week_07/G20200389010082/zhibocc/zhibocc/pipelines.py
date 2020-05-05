# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from snownlp import SnowNLP
import pymysql


dbInfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'db': 'geektime'
}


class ConnDB(object):
    def __init__(self):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    def run(self, sql, val):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        cur = conn.cursor()
        try:
            # print(sql, val)
            cur.executemany(sql, val)
            conn.commit()
        except:
            conn.rollback()
            raise
        conn.close()


def reviews_snow_nlp(review_text):
    snp = SnowNLP(review_text)
    return snp.sentiments


def sql_generator():
    return "INSERT INTO news_comments (col_comment, col_sentiments, col_title, col_time, col_link, col_today) VALUES (%s,%s,%s,%s,%s,%s)"


class ZhiboccPipeline(object):
    def process_item(self, item, spider):
        title = item['title']  # 新闻名称
        news_time = item['time']  # 新闻排名
        news_today = item['today']
        news_link = item['link']  # 新闻链接
        comment_list = item['comment_list']  # 新闻评论
        if comment_list:
            sql_val = tuple((comment, str(reviews_snow_nlp(comment)), title, news_time, news_link, news_today) for comment in comment_list)
            db_object = ConnDB()
            db_object.run(sql=sql_generator(), val=sql_val)
        return item

