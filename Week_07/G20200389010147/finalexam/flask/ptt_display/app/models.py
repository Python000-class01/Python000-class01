from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class gossiping(db.Model):
    __tablename__ = 'gossiping'

    # id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), primary_key=True)
    cmt = db.Column(db.String(200), primary_key=True)
    cmttime = db.Column(db.String(100))
