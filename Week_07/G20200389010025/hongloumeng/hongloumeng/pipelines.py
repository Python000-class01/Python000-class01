# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql
from . import DBAccess as db

def WriteToDB(item):
    try:
        sql = 'insert into hlmshorts_new(S_STAR,I_VOTE,S_SHORTS,S_SHORTSTIME,D_CREATETIME,C_USETAG) ' \
              'values(%s,%s,%s,%s,now(),"1")'
        values = (str(item['star']),
                  str(item['vote']),
                  str(item['short']),
                  str(item['shorttime']))
        db.executenonsql(sql, values)
    except Exception as e:
        print(e)


# def executenonsql(sql, value):
#     conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", charset="utf8", db="test")
#     """
#         连接mysql数据库（写），并进行写的操作
#         """
#     try:
#         cursor = conn.cursor()
#     except Exception as e:
#         print(e)
#         return False
#     try:
#         cursor.execute(sql, value)
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         print(e)
#         # logging.error('数据写入失败:%s' %e)
#         return False
#     finally:
#         cursor.close()
#         conn.close()
#     return True

class DoubanbookPipeline(object):
    def __init__(self):
        # self.article = None
        self.star_to_number = {
                '力荐': 5,
                '推荐': 4,
                '还行': 3,
                '较差': 2,
                '很差': 1
            }

    def process_item(self, item, spider):
        print('12345676 start')
        WriteToDB(item)
        print('12345676 end')
        return item


