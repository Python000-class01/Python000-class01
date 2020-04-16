from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db
# 
class T1(db.Model):
    __tablename__ = 'shuping2'
# 
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String)
    rate = db.Column(db.Float)
    recom = db.Column(db.String)
    content = db.Column(db.String)
    time = db.Column(db.String)
    sentiment = db.Column(db.Float)
# 