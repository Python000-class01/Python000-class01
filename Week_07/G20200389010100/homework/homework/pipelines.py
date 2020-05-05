# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from rediscluster import RedisCluster
import pymysql
from scrapy.exceptions import DropItem
import pandas as pd

startup_nodes = [{"host": "127.0.0.1", "port": '6379'}]
redis_db = RedisCluster(
    startup_nodes=startup_nodes,
    decode_responses=True
)
redis_key = 'comment_id'


class HomeworkPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='mysql',
            password='touhou',
            database='testdb',
            charset='utf8mb4'
        )
        self.cursor = self.connect.cursor()
        redis_db.flushdb()
        if redis_db.hlen(redis_key) == 0:
            df = pd.read_sql('select mid from sina_comment', self.connect)
            for mid in df['mid'].values.tolist():
                redis_db.hset(redis_key, mid, 0)

    def insert(self, values):
        sql = 'insert into sina_comment(mid, content, time) values (%s, %s, %s)'
        self.cursor.execute(sql, values)

    def process_item(self, item, spider):
        mid = item['mid']
        content = item['content']
        time = item['time']

        if redis_db.hexists(redis_key, mid):
            raise DropItem("Duplicate item found: %s" % item)

        values = (mid, content, time)
        self.insert(values)
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
