from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT, VARCHAR

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base
from app import db
from sqlalchemy.orm import sessionmaker



class T1(db.Model):
    __tablename__ = 't1'

    id = Column(Integer, primary_key=True)
    n_star = Column(Integer)
    short = Column(String(255))
    sentiment = Column(Float)

class Sentiment(db.Model):
    __tablename__ = 'sentiment'

    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer)
    sentiment = Column(Float)

class BilibiliComment(db.Model):
    __tablename__ = 'bilibili_comments'

    id = Column(BIGINT(20), primary_key=True)
    comment_date = Column(Integer)
    member_name = Column(String(100))
    member_id = Column(String(50))
    comment_text = Column(VARCHAR(10000))
    comment_id = Column(String(50))


class BilibiliCommentsClean(db.Model):
    __tablename__ = 'bilibili_comments_clean'

    id = Column(BIGINT(20), primary_key=True)
    comment_date = Column(INTEGER(11))
    member_name = Column(String(100))
    member_id = Column(String(50))
    comment_text = Column(String(10000))
    comment_id = Column(String(50))

