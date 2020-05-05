# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
import pandas as pd
from sqlalchemy import create_engine
from snownlp import SnowNLP

movie_data = []


class DoubanPipeline(object):
    # 链接数据库
    def __init__(self, ):
        dbparms = dict(
            host='localhost',
            db='test',
            user='root',
            passwd='gentoo',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        # 指定擦做数据库的模块名和数据库参数参数
        self.dbpool = adbapi.ConnectionPool("pymysql", **dbparms)



    # 使用twisted将mysql插入变成异步执行
    def process_item(self, item, spider):
        # 从item中导入
        name = item['name']
        grade = item['grade']
        time = item['time']
        comment = item['comment']
        support_num = item['support_num']

        s = SnowNLP(comment)
        # print(s.sentiments)
        # 根据短评进行情感分析

        try:
            data = pd.DataFrame({"name": name, "grade": grade, "comment": comment, "sentiment": s.sentiments}, index=[0])
            # print(data)

            # 将数据写入mysql的数据库，但需要先通过sqlalchemy.create_engine建立连接,且字符编码设置为utf8，否则有些latin字符不能处理
            connect = create_engine('mysql+pymysql://root:gentoo@localhost:3306/test?charset=utf8')
            pd.io.sql.to_sql(data, 'doubanDB', connect, schema='test', if_exists='append')
        except Exception as err:
            print('导入失败')
            print(err)