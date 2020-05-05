# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlalchemy as sqlmy
from sqlalchemy.orm import sessionmaker
from .config import mysql_config as mc
from .models import Comment as cc

class DoubanPipeline(object):
    def __init__(self):
        self.engine = sqlmy.create_engine(
                        "mysql+pymysql://"+mc['user']+":"+mc['psw']+"@"+mc['host']+":"+mc['port']+"/"+mc['db_name']+"?charset="+mc['charset'],
                        echo=False)
    def process_item(self, item, spider):
        print(item)
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        get_data = session.query(cc).filter(cc.cid == item['cid']).first()
        if (get_data is None):
            new_data = cc(sub_id=item['sub_id'], cid=item['cid'],comment=item['comment'],star=item['star'], score1=item['score1'], info_time=item['info_time'])
            session.add(new_data)
            session.commit()

        else:
            # print(get_data)
            print("repeat")
        session.close()
        return item
