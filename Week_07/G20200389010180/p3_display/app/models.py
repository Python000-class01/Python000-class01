from sqlalchemy import Column, Integer, String, Float, Date
from flask_sqlalchemy import SQLAlchemy
from app import db

class Smzdm(db.Model):
    __tablename__ = 'smzdm2'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    date = db.Column(db.Date())
    content = db.Column(db.String(1024))
    sentiment = db.Column(db.Float)