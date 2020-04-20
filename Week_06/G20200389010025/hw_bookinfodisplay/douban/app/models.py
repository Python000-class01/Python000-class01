from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class HLMShorts(db.Model):
    __tablename__ = 'HLMShorts'

    id = db.Column(db.Integer, primary_key=True)
    s_star = db.Column(db.String(255))
    i_vote = db.Column(db.String(11))
    s_shorts = db.Column(db.String(4000))
    i_newstar = db.Column(db.String(11))
    i_sentiment = db.Column(db.String(11))
