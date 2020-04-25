from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(45))
    nick = db.Column(db.String(45))
    area = db.Column(db.String(45))
    pub_time = db.Column(db.String(45))
    content = db.Column(db.String(800))
    crawl_time = db.Column(db.String(45))
    sentiment = db.Column(db.String(45))


class Figure():
    
    def histogram(dateLst, numLst):
        pass


    def pie(pos, neg):
        pass
