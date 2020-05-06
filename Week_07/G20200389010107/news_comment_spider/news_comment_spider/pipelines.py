# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import sys
import os 
import path
import re
import pandas
from snownlp import SnowNLP

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from setting.setting import GlobalSetting


class NewsCommentSpiderPipeline(object):
    
    def __init__(self):
        self._db = pymysql.connect(host=GlobalSetting.mysql_host,
            user=GlobalSetting.mysql_user,passwd=GlobalSetting.mysql_password)
        self._cursor = self._db.cursor()
        sql = f"create database if not exists {GlobalSetting.mysql_database} default character set utf8mb4 collate utf8mb4_unicode_ci"
        self._cursor.execute(sql)
        self._cursor.execute("use %s" % GlobalSetting.mysql_database)
        sql = f"create table if not exists {GlobalSetting.mysql_raw_data_table}( \
            id INT AUTO_INCREMENT PRIMARY KEY, \
            comment_text text, \
            time_stamp text)"
        self._cursor.execute(sql)  

    
    def process_item(self, item, spider):
        
        sql = f"INSERT INTO {GlobalSetting.mysql_raw_data_table} (comment_text, time_stamp) VALUES (%s, %s)"
        self._cursor.execute(sql, (item["comment_text"], item["time_stamp"]))
        #print("DEBUG", sql)
        #input("DEBUG.....")
        return item

    def close_spider(self, spider):
        self._db.commit()
        self._cursor.close()
        self._db.close()




class SentimentCalculationPipeline(object):
    
    def __init__(self):
        self._db = pymysql.connect(host=GlobalSetting.mysql_host,
            user=GlobalSetting.mysql_user,passwd=GlobalSetting.mysql_password)
        self._cursor = self._db.cursor()
        sql = f"create database if not exists {GlobalSetting.mysql_database} default character set utf8mb4 collate utf8mb4_unicode_ci"
        self._cursor.execute(sql)
        self._cursor.execute("use %s" % GlobalSetting.mysql_database)
        sql = f"create table if not exists {GlobalSetting.mysql_cleaned_data_table}( \
            user_id INT AUTO_INCREMENT PRIMARY KEY, \
            raw_text text, \
            cleaned_text text, \
            sentiment_score float, \
            time_stamp text)"
        self._cursor.execute(sql)  

    
    def process_item(self, item, spider):
        raw_text = item["comment_text"]
        time_stamp = item["time_stamp"]
        cleaned_text = self.clean_text(raw_text)
        sentiment_score = SnowNLP(cleaned_text).sentiments
        sql = f"INSERT INTO {GlobalSetting.mysql_cleaned_data_table} \
            (raw_text, cleaned_text, sentiment_score, time_stamp) VALUES (%s, %s, %s, %s)"
        self._cursor.execute(sql, (raw_text, cleaned_text, sentiment_score, time_stamp))
        return item
    
    
    def clean_text(self, raw_text):
        cleaned_text = raw_text.replace("\n", " ")
        cleaned_text = cleaned_text.replace("\r", " ")
        fil = re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5.，,。？“”]+', re.UNICODE)
        cleaned_text = fil.sub(' ', cleaned_text)
        return cleaned_text

    def close_spider(self, spider):
        self._db.commit()
        self._cursor.close()
        self._db.close()

