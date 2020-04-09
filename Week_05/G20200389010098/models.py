# coding: utf-8
from sqlalchemy import Column, Text, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(INTEGER(10), primary_key=True)
    rid = Column(INTEGER(10), nullable=False, unique=True, server_default=text("'0'"))
    sub_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    star = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    review = Column(Text, nullable=False)
    info_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class ReviewsComment(Base):
    __tablename__ = 'reviews_comment'

    id = Column(INTEGER(10), primary_key=True)
    rid = Column(INTEGER(10), nullable=False, unique=True, server_default=text("'0'"))
    sub_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    cid = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    comment = Column(Text, nullable=False)
    score1 = Column(DECIMAL(19, 18), nullable=False, server_default=text("'0.000000000000000000'"))
    score2 = Column(DECIMAL(19, 18), nullable=False, server_default=text("'0.000000000000000000'"))
    tag = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
