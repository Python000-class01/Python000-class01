from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class NewsModel(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.BigInteger, primary_key=True)
    mid = db.Column(db.String)
    content = db.Column(db.Text)
    uid = db.Column(db.String)
    area = db.Column(db.String)
    nick = db.Column(db.String)
    ip = db.Column(db.String)
    newsid = db.Column(db.String)
    time = db.Column(db.Date)
    sentiments = db.Column(db.DECIMAL)
    keywords = db.Column(db.String)
    input_time = db.Column(db.Date)
