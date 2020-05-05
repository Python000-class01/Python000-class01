import sqlalchemy as sqlmy
from sqlalchemy.orm import sessionmaker
from config import mysql_config as mc
import models as M

engine=None

def Rinsert(items):

        global engine
        if(engine is None):
                engine = sqlmy.create_engine(
                        "mysql+pymysql://"+mc['user']+":"+mc['psw']+"@"+mc['host']+":"+mc['port']+"/"+mc['db_name']+"?charset="+mc['charset'],
                        echo=False)
        DBSession = sessionmaker(bind = engine)
        session = DBSession()
        get_data = session.query(M.Review).filter(M.Review.rid==items['rid']).first()
        if(get_data is None):
                new_data = M.Review(rid=items['rid'], sub_id=items['sub_id'], star=items['star'], review=items['review'], info_time=items['info_time'])
                session.add(new_data)
                session.commit()

        else:
                #print(get_data)
                print("repeat")
        session.close()

def Allreviews():

        global engine
        if(engine is None):
                engine = sqlmy.create_engine(
                        "mysql+pymysql://"+mc['user']+":"+mc['psw']+"@"+mc['host']+":"+mc['port']+"/"+mc['db_name']+"?charset="+mc['charset'],
                        echo=False)
        DBSession = sessionmaker(bind = engine)
        session = DBSession()
        get_data = session.query(M.Review.rid).all()
        session.close()
        return get_data

def Cinsert(items):

        global engine
        if(engine is None):
                engine = sqlmy.create_engine(
                        "mysql+pymysql://"+mc['user']+":"+mc['psw']+"@"+mc['host']+":"+mc['port']+"/"+mc['db_name']+"?charset="+mc['charset'],
                        echo=False)
        DBSession = sessionmaker(bind = engine)
        session = DBSession()
        get_data = session.query(M.ReviewsComment).filter(M.ReviewsComment.cid==items['cid']).first()
        if(get_data is None):
                new_data = M.ReviewsComment(rid=items['rid'], sub_id=items['sub_id'], cid=items['cid'], comment=items['comment'], score1=items['score1'])
                session.add(new_data)
                session.commit()

        else:
                #print(get_data)
                print("repeat")
        session.close()
