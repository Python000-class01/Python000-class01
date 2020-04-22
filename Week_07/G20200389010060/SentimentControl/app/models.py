from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class Comments(db.Model):
    __tablename__ = 'news_nlp'
    content = db.Column(db.String(3000))
    user_name = db.Column(db.String(200), primary_key=True)
    time_stamp = db.Column(db.BIGINT, primary_key=True)
    score = db.Column(db.Float)
    positive = db.Column(db.Boolean)
    keywords = db.Column(db.String(3000))


class PickCnt(db.Model):
    __tablename__ = 'news_pick_cnt'
    id = db.Column(db.INT, primary_key=True)
    pick_cnt = db.Column(db.INT)


class CommentItem:
    def __init__(self, content, user_name, time_stamp, score, positive):
        self.content = content
        self.user_name = user_name
        self.time_stamp = time_stamp
        self.score = score
        self.positive = positive

