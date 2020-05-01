# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
'''
    爬虫获取相关的评论id,时间，评论的详细内容
    在此做数据的相关清洗、去重及情感分析  
'''
import pandas as pd 
import pymysql
import numpy as np
from snownlp import SnowNLP

class SinanewsPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',user = "root",password = "huang171276",db="news",charset='utf8mb4')

        
    def process_item(self, item, spider):
        news_comments = item['news_comments']
        users = item['users']
        time_comments = item['time']
        def trans_comment(comment):
            if comment is None:
                return None
            else:
                string = ""
                for c in comment:
                    if c =='"':
                        string += '\\\"'
                    elif c =="'":
                        string += "\\\'"
                    else:
                         string += c
                return string
        comments = list(map(trans_comment,news_comments))
        sentiments = []
        for comment in comments:
            cmt = SnowNLP(comment)
            sentiments.append(cmt.sentiments)
        
        ###  ===========   存入mysql时根据采集的user判断去重 ==========
        for user,time,comment,sentiment in zip(users,time_comments,news_comments,sentiments):
            try:
                sql = f"INSERT INTO `news`.`sina`(`user`,`time`,`comment`,`sentiment`)  select('{user}'),('{time}'),('{comment}'),('{sentiment}') from dual where not EXISTS  (SELECT  `user` from `sina` where `user` = '{user}');"
                print(sql)
                self.conn.query(sql)
                self.conn.commit()
            except ValueError as e:
                print(e)
                self.conn.rollback()
        return item
    
    def close_spider(self,spider):
        self.conn.close   
        
