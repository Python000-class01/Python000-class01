# coding: utf-8
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BilibiliComment(Base):
    __tablename__ = 'bilibili_comments'

    id = Column(BIGINT(20), primary_key=True)
    comment_date = Column(INTEGER(11))
    member_name = Column(String(100))
    member_id = Column(String(50))
    comment_text = Column(VARCHAR(10000))
    comment_id = Column(String(50))


class BilibiliCommentsClean(Base):
    __tablename__ = 'bilibili_comments_clean'

    id = Column(BIGINT(20), primary_key=True)
    comment_date = Column(INTEGER(11))
    member_name = Column(String(100))
    member_id = Column(String(50))
    comment_text = Column(String(10000))
    comment_id = Column(String(50))



 

