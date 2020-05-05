# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from decimal import Decimal
import threading
from snownlp import SnowNLP
from . import DBAccess as db


def WriteToDB(item):
    try:
        sql = 'select count(*) from hlmshort_stat t where t.S_SHORTSTIME = "%s"' %(str(item["shorttime"]))
        df = db.readtable(sql)
        cnt = df.iat[0, 0]
        print('sql=', sql)
        print('cnt=', cnt)
        values = (str(item["shorttime"]))
        if cnt == 0:
            sqlIns = 'insert into hlmshort_stat VALUES(%s,0,0,0)'
            db.executenonsql(sqlIns, values)
        else:
            sqlUpd = 'update hlmshort_stat t set t.i_shortcount = i_shortcount+1 where t.S_SHORTSTIME = %s'
            db.executenonsql(sqlUpd, values)
        if Decimal(item['sentiment']) > 0.5:
            sqlUpd1 = 'update hlmshort_stat t set t.i_short_positive = i_short_positive+1 where t.S_SHORTSTIME = %s'
            db.executenonsql(sqlUpd1, values)
        else:
            sqlUpd2 = 'update hlmshort_stat t set t.i_short_negative = i_short_negative+1 where t.S_SHORTSTIME = %s'
            db.executenonsql(sqlUpd2, values)
    except Exception as e:
        print(e)


class StatPipeline(object):
    def __init__(self):
        self.mutex = threading.Lock()

    def process_item(self, item, spider):
        if item is None:
            return
        if self.mutex.acquire(1):    # 上锁
            WriteToDB(item)
        self.mutex.release()  # 解锁
        return item


