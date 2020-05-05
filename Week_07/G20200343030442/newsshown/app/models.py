from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'article_res'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    comment = db.Column(db.String(400))
    score = db.Column(db.String(20))
