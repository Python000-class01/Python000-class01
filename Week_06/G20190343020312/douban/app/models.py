from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class MYTABLE(db.Model):
    __tablename__ = 'mytable'

    star = db.Column(db.String(10), primary_key=True)
    shorts = db.Column(db.String(10000))
    score = db.Column(db.Integer)
    sentiment = db.Column(db.Float)
