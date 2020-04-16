from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'new'

    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(255))
    sentiment = db.Column(db.Float)
