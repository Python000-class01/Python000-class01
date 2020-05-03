# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
import hashlib

db = SQLAlchemy()



class Comment(db.Model):
    __tablename__ = 'hz_comment'

    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, nullable=False, unique=True, server_default=db.FetchedValue())
    sub_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    star = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment = db.Column(db.Text, nullable=False)
    score1 = db.Column(db.Numeric(19, 18), nullable=False, server_default=db.FetchedValue())
    info_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class Manage(db.Model):
    __tablename__ = 'hz_manage'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    psd = db.Column(db.String(40), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    def md5_password(string):
        m = hashlib.md5()
        m.update(string.encode())
        return m.hexdigest()



class Review(db.Model):
    __tablename__ = 'hz_reviews'

    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sub_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    star = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    review = db.Column(db.Text, nullable=False)
    info_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class HzReviewsCommentCopy(db.Model):
    __tablename__ = 'hz_reviews_comment_copy'

    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sub_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    cid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment = db.Column(db.Text, nullable=False)
    score1 = db.Column(db.Numeric(19, 18), nullable=False, server_default=db.FetchedValue())
    score2 = db.Column(db.Numeric(19, 18), nullable=False, server_default=db.FetchedValue())
    tag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class HzSpecial(db.Model):
    __tablename__ = 'hz_special'

    id = db.Column(db.Integer, primary_key=True)
    special_name = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class HzSpecialComment(db.Model):
    __tablename__ = 'hz_special_comment'

    id = db.Column(db.Integer, primary_key=True)
    special_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    url_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sub_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    cid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment = db.Column(db.Text, nullable=False)
    score1 = db.Column(db.Numeric(19, 18), nullable=False, server_default=db.FetchedValue())
    score2 = db.Column(db.Numeric(19, 18), nullable=False, server_default=db.FetchedValue())
    info_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    def daily_count():

        cc= db.session.execute(r"SELECT count(*) as count,FROM_UNIXTIME(info_time,'%Y-%m-%d') as info_date FROM `hz_special_comment` GROUP BY info_date ORDER BY info_time asc")
        xAxis = [] 
        series = [] 
        for i in list(cc):
            xAxis.append(i[0]) 
            series.append(i[1]) 
        print(xAxis)
        print(series)  
        return {"xAxis":xAxis,"series":series}



class HzSpecialUrl(db.Model):
    __tablename__ = 'hz_special_urls'

    id = db.Column(db.Integer, primary_key=True)
    special_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    special_url = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    spider_name = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    spider_key = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    last_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
