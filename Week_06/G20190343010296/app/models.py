from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class Comments(db.Model):
    __tablename__ = 'movie_comment_nlp'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(3000))
    score = db.Column(db.Float)
    positive = db.Column(db.Boolean)


class CommentItem:
    def __init__(self, id, content, score, positive):
        self.id = id
        self.content = content
        self.score = score
        self.positive = positive
