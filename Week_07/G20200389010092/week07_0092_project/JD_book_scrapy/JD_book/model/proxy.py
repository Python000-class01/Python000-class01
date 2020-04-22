# -*- coding: utf-8 -*-
from sqlalchemy import Column,String,Integer,DateTime

from . import Base
import datetime
class Proxy(Base):

    __tablename__ = 'jdbook_data'

    date = Column(String(20), primary_key=True)
    score = Column(Integer)
    comment = Column(String(500))

    def __init__(self,date,score,comment):
        self.date = date
        self.score = score
        self.comment = comment