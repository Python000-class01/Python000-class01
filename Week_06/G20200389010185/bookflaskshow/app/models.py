from sqlalchemy import Column, Integer, String, Float,BIGINT,Text
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'emotion'

    index = db.Column(db.BIGINT, primary_key=True)
    shorts = db.Column(db.Text)
    score = db.Column(db.BIGINT)
    emotions = db.Column(db.Float)
