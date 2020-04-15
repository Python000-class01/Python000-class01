# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata



class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    cid = Column(Integer, nullable=False, unique=True, server_default=FetchedValue())
    sub_id = Column(Integer, nullable=False, server_default=FetchedValue())
    star = Column(Integer, nullable=False, server_default=FetchedValue())
    comment = Column(Text, nullable=False)
    score1 = Column(Numeric(19, 18), nullable=False, server_default=FetchedValue())
    info_time = Column(Integer, nullable=False, server_default=FetchedValue())



class Manage(Base):
    __tablename__ = 'manage'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False, server_default=FetchedValue())
    psd = Column(String(40), nullable=False, server_default=FetchedValue())
    status = Column(Integer, nullable=False, server_default=FetchedValue())



class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rid = Column(Integer, nullable=False, server_default=FetchedValue())
    sub_id = Column(Integer, nullable=False, server_default=FetchedValue())
    star = Column(Integer, nullable=False, server_default=FetchedValue())
    review = Column(Text, nullable=False)
    info_time = Column(Integer, nullable=False, server_default=FetchedValue())



class ReviewsComment(Base):
    __tablename__ = 'reviews_comment'

    id = Column(Integer, primary_key=True)
    rid = Column(Integer, nullable=False, server_default=FetchedValue())
    sub_id = Column(Integer, nullable=False, server_default=FetchedValue())
    cid = Column(Integer, nullable=False, server_default=FetchedValue())
    comment = Column(Text, nullable=False)
    score1 = Column(Numeric(19, 18), nullable=False, server_default=FetchedValue())
    score2 = Column(Numeric(19, 18), nullable=False, server_default=FetchedValue())
    tag = Column(Integer, nullable=False, server_default=FetchedValue())
