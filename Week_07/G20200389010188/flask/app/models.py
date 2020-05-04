from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'comments'

    id       = db.Column(db.Integer, primary_key=True)
    star     = db.Column(db.String(3))
    shorts  = db.Column(db.String(1500))
    name     = db.Column(db.String(100))
    category = db.Column(db.String(3))
