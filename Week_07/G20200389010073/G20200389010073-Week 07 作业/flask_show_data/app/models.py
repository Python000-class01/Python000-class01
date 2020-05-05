from sqlalchemy import Column, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'douban_reviews'

    id = db.Column(db.Integer, primary_key=True)
    c_Name = db.Column(db.String(255))
    c_Time = db.Column(db.DateTime)
    c_Mark = db.Column(db.String(255))
    c_Sln_comment = db.Column(db.String(255))
    c_Comment = db.Column(db.String(255))
    created_at = db.Column(db.String(255))
