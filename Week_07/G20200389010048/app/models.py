from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT,DECIMAL

from app import db

class T1(db.Model):

    __tablename__ = 'news_comments'

    nc_mid = db.Column(db.String(50), primary_key=True)  # 评论的mid
    nc_uid = db.Column(db.String(20))  # 评论用户id
    nc_nickname = db.Column(db.String(100))  # 评论用户名
    nc_content = db.Column(LONGTEXT)  # 评论内容
    nc_sentiment = db.Column(DECIMAL(12,10))  # 评论内容的情感分析分数
    nc_time = db.Column(db.String(25))  # 评论时间
    nc_time2 = db.Column(db.String(25))  # 评论时间（秒数）
    nc_utime = db.Column(db.String(25))  # 采集时间
