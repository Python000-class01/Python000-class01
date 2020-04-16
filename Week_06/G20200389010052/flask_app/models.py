from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class shortinfo(db.Model):
    __tablename__ = 'shortinfo'

    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(255))
    short = db.Column(db.String(255))
    sentiment = db.Column(db.Float)
