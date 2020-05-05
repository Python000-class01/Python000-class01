from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'sina'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(255))
    comment = db.Column(db.String(3000))
    sentiment = db.Column(db.Float)
    time = db.Column(db.Date)
    
