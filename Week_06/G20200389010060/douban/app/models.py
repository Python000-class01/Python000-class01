from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from douban.app import db

class Comments(db.Model):
    __tablename__ = 'sentiment'
    item_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(3000))
    score = db.Column(db.Float)
    sentiments = db.Column(db.Float)


class CommentItem:
    def __init__(self, item_id, comment, score, sentiments):
        self.item_id = item_id
        self.comment = comment
        self.score = score
        self.sentiments = sentiments
