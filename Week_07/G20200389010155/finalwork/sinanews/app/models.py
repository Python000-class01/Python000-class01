from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class NewsModel(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.BigInteger, primary_key=True)
    uid = db.Column(db.String)
    area = db.Column(db.String)
    ipadd = db.Column(db.String)
    usertype = db.Column(db.String)
    agree = db.Column(db.String)
    cmttime = db.Column(db.Date)
    content = db.Column(db.Text)
    sentiments = db.Column(db.DECIMAL)
    keywords = db.Column(db.String)
    # id = db.Column(db.Integer, primary_key=True)
    # n_star = db.Column(db.Integer)
    # short = db.Column(db.String(255))
    # sentiment = db.Column(db.Float)
