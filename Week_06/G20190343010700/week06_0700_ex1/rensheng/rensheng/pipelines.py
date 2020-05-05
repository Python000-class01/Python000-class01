# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd 
import pymysql

class RenshengPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',user = "root",password = "******",db="book",charset='utf8mb4')

    def process_item(self, item, spider):
        star_rank = item['star']
        short_comment = item['short']
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
        comment = list(map(trans_comment,short_comment))
        starts = []
        for star in star_rank:
            if len(star) == 2:
                starts.append(star)
            else:
                starts.append(0)
        for star,comment in zip(starts,comment):  
            sql = f"INSERT INTO `book`.`rensheng`(`star_rank`, `comment`) VALUES ('{star}', '{comment}')"
            print(sql)
            self.conn.query(sql)
            self.conn.commit()
        return item
    
    def close_spider(self,spider):
        self.conn.close
        