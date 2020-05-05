# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from decimal import Decimal
import pandas as pd
from snownlp import SnowNLP
from . import DBAccess as db


def WriteToDB(item):
    try:
        sql = 'insert into hlmshorts_new1(S_STAR,I_VOTE,S_SHORTS,I_NEWSTAR,I_SENTIMENT,S_SHORTSTIME,D_CREATETIME,C_USETAG) ' \
              'values(%s,%s,%s,%s,%s,%s,now(),"1")'
        values = (str(item['star']),
                  str(item['vote']),
                  str(item['short']),
                  str(item['new_star']),
                  str(Decimal(item['sentiment']).quantize(Decimal('0.000000'))),
                  str(item['shorttime']))
        db.executenonsql(sql, values)
        # print(sql)
        # print(values)
    except Exception as e:
        print(e)


class SentimentPipeline(object):
    def __init__(self):
        self.star_to_number = {
                '力荐': 5,
                '推荐': 4,
                '还行': 3,
                '较差': 2,
                '很差': 1
            }

    def process_item(self, item, spider):
        if item is None:
            return
        item['new_star'] = self.star_to_number[item['star']]
        item["sentiment"] = SnowNLP(item["short"]).sentiments
        WriteToDB(item)
        return item


