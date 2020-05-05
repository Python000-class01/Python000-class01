from sqlalchemy import Column, Integer, String, Float,Text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from app import db

class Mytable(db.Model):
    __tablename__ = 'news_em'

    id = db.Column(db.Integer, primary_key=True)
    shorts = db.Column(db.Text)
    em = db.Column(db.Float)
    day = db.Column(db.Integer)


