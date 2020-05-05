# -*- encoding=utf-8 -*-
# @File: newsComments.py
# @Author：wsr
# @Date ：2020/4/22 21:33

from sqlalchemy import Column,String,Integer,DateTime

from . import Base
import datetime
class newsComments(Base):

    __tablename__ = 'comments_book'

    date = Column(String(20), primary_key=True)
    score = Column(Integer)
    comment = Column(String(500))

    def __init__(self,date,score,comment):
        self.date = date
        self.score = score
        self.comment = comment