from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class T1(db.Model):
    __tablename__ = 't1'

    id = Column(Integer, primary_key=True)
    n_star = Column(Integer)
    short = Column(String(255))
    sentiment = Column(Float)
