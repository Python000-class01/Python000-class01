# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model import Base,engine,loadSession
from model import proxy


class JdBookPipeline(object):
    Base.metadata.create_all(engine)

    def process_item(self, item, spider):
        a = proxy.Proxy(
            date = item['book_comment_date'],
            score= item['book_score'],
            comment= item['book_comment'],
        )
        session = loadSession()
        session.add(a)
        session.commit()
        return item