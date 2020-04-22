# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import datetime
from snownlp import SnowNLP
import pandas as pd
import pymysql
import jieba.analyse


class SinacommentsPipeline(object):

    def __init__(self, ip, username, password, db):
        self.ip = ip
        self.username = username
        self.password = password
        self.db = db
        
    @classmethod
    def from_crawler(cls, crawler):
        MYSQL = crawler.settings.get('MYSQL')
        return cls(
            ip = MYSQL['ip'],
            username = MYSQL['username'],
            password = MYSQL['password'],
            db = MYSQL['db']
        )

    def open_spider(self, spider):
        try:
            self.db = pymysql.connect(self.ip, self.username, self.password, self.db)
            self.cursor = self.db.cursor()
            self.time = self.getNewestTime()
        except KeyError as e:
            print(f'{e} is not found' )
        except pymysql.err.InternalError:
            print('没找到数据库')

    def close_spider(self, spider):
        self.db.close()

    def insert(self, **kwargs):
        table = kwargs['table']
        data = kwargs['data']
        keys = ','.join(data.keys())
        values = ','.join(str(s) for s in map(lambda key: f'"{key}"' if type(key) == str else key, data.values()))
        sql = f'REPLACE INTO {table} ({keys}) VALUES ({values});'
        self.cursor.execute(sql)
        self.db.commit()

    def getNewestTime(self):
        sql = 'SELECT time FROM comments order by time desc limit 1;'
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        return res[0] if res and len(res) > 0 else None

    def process_item(self, item, spider):
        time = datetime.datetime.strptime(item['time'], '%Y-%m-%d %H:%M:%S')
        # print(item)
        if self.time: 
            if time > self.time:
                print('inserting')
                self.insert(table='comments', data={
                    "mid": item['mid'], 
                    "content": item['content'], 
                    "user": item['nick'], 
                    "area": item['area'], 
                    "time": item['time']
                })
                sentiment = SnowNLP(item['content']).sentiments
                keywords = list(jieba.analyse.extract_tags(item['content'], topK=5, withWeight=False))
                self.insert(table='sentiments', data={
                    "c_id": item['mid'],
                    "sentiment": sentiment
                })
                [self.insert(table='keywords', data={
                    "c_id": item['mid'],
                    "keyword": word,
                }) for word in keywords]
        else:
            print('inserting')
            self.insert(table='comments', data={
                    "mid": item['mid'], 
                    "content": item['content'], 
                    "user": item['nick'], 
                    "area": item['area'], 
                    "time": item['time']
                })
            sentiment = SnowNLP(item['content']).sentiments
            keywords = list(jieba.analyse.extract_tags(item['content'], topK=5, withWeight=False))
            self.insert(table='sentiments', data={
                "c_id": item['mid'],
                "sentiment": sentiment
            })
            [self.insert(table='keywords', data={
                "c_id": item['mid'],
                "keyword": word,
            }) for word in keywords]
        return item
