from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BigInteger, Column, Float, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comments(db.Model):
    __tablename__ = 'douban_comments'

    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.Integer)
    short = db.Column(db.String(255))
    feelings = db.Column(db.Float)
