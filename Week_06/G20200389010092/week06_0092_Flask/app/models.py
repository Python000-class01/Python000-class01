from sqlalchemy import Column, Float, Integer, Text
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'bwbj'

    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.Text)
    shorts = db.Column(db.Text)
    #score = db.Column(db.Float(asdecimal=True))
    sentiment = db.Column(db.Float(asdecimal=True))
