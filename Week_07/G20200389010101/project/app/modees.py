from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class MYTABLE(db.Model):
    __tablename__ = 'doubanDB'

    name = db.Column(db.String(10), primary_key=True)
    grade = db.Column(db.String(10))
    comment = db.Column(db.String(10000))
    sentiment = db.Column(db.Float(10))