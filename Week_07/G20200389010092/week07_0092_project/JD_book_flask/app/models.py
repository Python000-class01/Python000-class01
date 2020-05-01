from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'jdbook_sentiment_analyais_data'

    date = db.Column(db.String(255, 'utf8_general_ci'), primary_key=True)
    score = db.Column(db.Integer)
    comment = db.Column(db.String(255, 'utf8_general_ci'))
    sentiment = db.Column(db.Float)
