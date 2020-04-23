# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class SinaCommentSentiment(db.Model):
    __tablename__ = 'sina_comment_sentiment'

    id = db.Column(db.BigInteger, primary_key=True)
    mid = db.Column(db.String(36), nullable=False, info='评论编号')
    content = db.Column(db.String(1000), info='评论内容')
    sentiment = db.Column(db.Float, info='情感評分')
    date = db.Column(db.String(10), info='评论日期')
