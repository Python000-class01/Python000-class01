from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(45))
    nick = db.Column(db.String(45))
    area = db.Column(db.String(45))
    # time = db.Column(db.String(45))
    content = db.Column(db.String(800))
    sentiment = db.Column(db.String(45))
