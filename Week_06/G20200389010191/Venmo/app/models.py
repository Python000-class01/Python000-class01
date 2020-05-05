from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class comment(db.Model):
    __tablename__ = 'comment'

    short = db.Column(db.String(3000))
    sentiment = db.Column(db.Float)
