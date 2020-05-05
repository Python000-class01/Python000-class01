# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata



class HzComment(Base):
    __tablename__ = 'hz_comment'

    id = Column(Integer, primary_key=True)
    cid = Column(Integer, nullable=False, unique=True, server_default=FetchedValue())
    sub_id = Column(Integer, nullable=False, server_default=FetchedValue())
    star = Column(Integer, nullable=False, server_default=FetchedValue())
    comment = Column(Text, nullable=False)
    score1 = Column(Numeric(19, 18), nullable=False, server_default=FetchedValue())
    info_time = Column(Integer, nullable=False, server_default=FetchedValue())



class HzManage(Base):
    __tablename__ = 'hz_manage'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False, server_default=FetchedValue())
    psd = Column(String(40), nullable=False, server_default=FetchedValue())
    status = Column(Integer, nullable=False, server_default=FetchedValue())



class HzReview(Base):
    __tablename__ = 'hz_reviews'

    id = Column(Integer, primary_key=True)
    rid = Column(Integer, nullable=False, server_default=FetchedValue())
    sub_id = Column(Integer, nullable=False, server_default=FetchedValue())
    star = Column(Integer, nullable=False, server_default=FetchedValue())
    review = Column(Text, nullable=False)
    info_time = Column(Integer, nullable=False, server_default=FetchedValue())



class HzReviewsCommentCopy(Base):
    __tablename__ = 'hz_reviews_comment_copy'

    id = Column(Integer, primary_key=True)
    rid = Column(Integer, nullable=False, server_default=FetchedValue())
    sub_id = Column(Integer, nullable=False, server_default=FetchedValue())
    cid = Column(Integer, nullable=False, server_default=FetchedValue())
    comment = Column(Text, nullable=False)
    score1 = Column(Numeric(19, 18), nullable=False, server_default=FetchedValue())
    score2 = Column(Numeric(19, 18), nullable=False, server_default=FetchedValue())
    tag = Column(Integer, nullable=False, server_default=FetchedValue())



class HzSpecial(Base):
    __tablename__ = 'hz_special'

    id = Column(Integer, primary_key=True)
    special_name = Column(String(30), nullable=False)
    status = Column(Integer, nullable=False, server_default=FetchedValue())



class HzSpecialComment(Base):
    __tablename__ = 'hz_special_comment'

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, nullable=False, server_default=FetchedValue())
    special_id = Column(Integer, nullable=False, server_default=FetchedValue())
    sub_id = Column(String(15), nullable=False, server_default=FetchedValue())
    cid = Column(Integer, nullable=False, server_default=FetchedValue())
    comment = Column(Text, nullable=False)
    score1 = Column(Numeric(19, 18), nullable=False, server_default=FetchedValue())
    score2 = Column(Numeric(19, 18), nullable=False, server_default=FetchedValue())
    info_time = Column(Integer, nullable=False, server_default=FetchedValue())
    add_time = Column(Integer, nullable=False, server_default=FetchedValue())
    tag = Column(Integer, nullable=False, server_default=FetchedValue())



class HzSpecialUrl(Base):
    __tablename__ = 'hz_special_urls'

    id = Column(Integer, primary_key=True)
    special_id = Column(Integer, nullable=False, server_default=FetchedValue())
    special_url = Column(String(200), nullable=False, server_default=FetchedValue())
    spider_name = Column(String(20), nullable=False, server_default=FetchedValue())
    spider_key = Column(String(20), nullable=False)
    last_time = Column(Integer, nullable=False, server_default=FetchedValue())
