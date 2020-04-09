# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pandas as pd 
import pymysql
class MoviePokemanPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',user = "root",password = "h******",db="test",charset='utf8mb4')

    def process_item(self,item,spider):
        movie_name = item['movie_name']
        short_comment = item['short_comment']
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
        rank = item['rank']
        for rank,comment in zip(rank,comment):  
            sql = f"INSERT INTO `test`.`movie`(`rank_movie`, `comment_movie`) VALUES ('{rank}', '{comment}')"
    
            print(sql)
            self.conn.query(sql)
            self.conn.commit()
        return item
    
    def close_spider(self,spider):
        self.conn.close
        




