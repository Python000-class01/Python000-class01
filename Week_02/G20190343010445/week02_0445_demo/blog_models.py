# coding: utf-8
from sqlalchemy import Column, Date, Integer, Numeric, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class BlogPost(db.Model):
    __tablename__ = 'blog_post'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer)
    created = db.Column(db.Date)
    title = db.Column(db.String(20))
    body = db.Column(db.String(400))



class BlogUser(db.Model):
    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(100))



class DoubanMovie(db.Model):
    __tablename__ = 'douban_movie'

    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(20))
    movie_link = db.Column(db.String(100))
    movie_rating_level = db.Column(db.String(20))
    movie_rating_num = db.Column(db.Numeric(10, 0))
    movie_rating_persons = db.Column(db.Integer)



class MovieComment(db.Model):
    __tablename__ = 'movie_comments'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    movie_comment = db.Column(db.String(400))
