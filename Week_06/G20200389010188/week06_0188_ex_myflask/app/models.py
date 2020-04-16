from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'comments3'

    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.String(10))
    comment = db.Column(db.String(5000))
    sentiment = db.Column(db.Float)
