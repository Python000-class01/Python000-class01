from sqlalchemy import BigInteger, Column, Float, String
from flask_sqlalchemy import SQLAlchemy
from app import db

class Bookshort(db.Model):
    __tablename__ = 'bookshorts'

    id = db.Column(db.BigInteger, primary_key=True)
    star = db.Column(db.String(1), info='星級')
    short = db.Column(db.String(1000), info='短評')
    sentiment = db.Column(db.Float, info='情感評分')