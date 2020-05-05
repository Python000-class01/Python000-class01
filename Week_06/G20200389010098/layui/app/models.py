# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
import hashlib

db = SQLAlchemy()



class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, nullable=False, unique=True, server_default=db.FetchedValue())
    sub_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    star = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment = db.Column(db.Text, nullable=False)
    score1 = Column(db.Numeric(19, 18), nullable=False, server_default=FetchedValue())
    info_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class Manage(db.Model):
    __tablename__ = 'manage'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    psd = db.Column(db.String(40), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

    def md5_password(string):
        m = hashlib.md5()
        m.update(string.encode())
        return m.hexdigest()



class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sub_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    star = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    review = db.Column(db.Text, nullable=False)
    info_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class ReviewsComment(db.Model):
    __tablename__ = 'reviews_comment'

    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sub_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    cid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment = db.Column(db.Text, nullable=False)
    score1 = db.Column(db.Numeric(19, 18), nullable=False, server_default=db.FetchedValue())
    score2 = db.Column(db.Numeric(19, 18), nullable=False, server_default=db.FetchedValue())
    tag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
