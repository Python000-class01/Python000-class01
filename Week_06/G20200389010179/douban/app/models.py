from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'bookcomm'

    #id = db.Column(db.Integer, primary_key=True)
    #evaluate = db.Column(db.String(10))
    #shortcomm = db.Column(db.String(255))
    #grade = db.Column(db.String(25))
    id = Column(Integer, primary_key=True)
    grade = Column(String(25))
    evaluate = Column(String(10))
    shortcomm = Column(String)