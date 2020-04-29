import sys
import os 
import path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting.setting import GlobalSetting

from sqlalchemy import Column, Integer, String, Float, Text
from flask_sqlalchemy import SQLAlchemy
from app import db

'''
class T1(db.Model):
    __tablename__ = "black_swan" #'t1'

    id = db.Column(db.Integer, primary_key=True)
    n_star = db.Column(db.Integer)
    short = db.Column(db.String(255))
    sentiment = db.Column(db.Float)
'''
class CommmetsData(db.Model):
    __tablename__ = GlobalSetting.mysql_cleaned_data_table

    user_id = db.Column(db.Integer, primary_key=True)
    raw_text = db.Column(db.Text)
    cleaned_text = db.Column(db.Text)
    sentiment_score = db.Column(db.Float)
    time_stamp = db.Column(db.Text)
    
