# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class T1(db.Model):
    __tablename__ = 't1'

    id = db.Column(db.BigInteger, primary_key=True)
    n_star = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    short = db.Column(db.String(400), nullable=False, server_default=db.FetchedValue())
    sentiment = db.Column(db.Float(12), nullable=False, server_default=db.FetchedValue())



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password_hash = db.Column(db.String(255))
