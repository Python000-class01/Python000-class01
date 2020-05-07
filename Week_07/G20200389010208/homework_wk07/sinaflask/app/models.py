from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20))
    short = db.Column(db.String(255))
    timestamp = db.Column(db.String(255))
    sentiment = db.Column(db.Float)