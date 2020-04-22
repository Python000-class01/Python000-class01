# -*- encoding=utf-8 -*-
# @File: __init__.py
# @Author：wsr
# @Date ：2020/4/22 21:31

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWD = '123456'
DB_NAME = 'comments'
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8&connect_timeout=10'

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

#返回数据库会话
def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session