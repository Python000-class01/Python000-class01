import requests
from bs4 import BeautifulSoup as bs
from os.path import exists
from sqlalchemy import create_engine

engine = create_engine(
        "mysql+pymysql://root:123456@localhost:3306/test?charset=utf8mb4", 
        echo=True)
# echo=True：用于显示SQLAlchemy在操作数据库时所执行的SQL语句情况，
# 相当于一个监视器，可以清楚知道执行情况。

############ 创建数据表
from sqlalchemy import Column, Integer, String, DateTime 
# 常用数据类型

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Mytable(Base):
    # 表名
    __tablename__ ="bookcomm"
    # 字段，属性
    id = Column(Integer, primary_key=True)
    grade = Column(String(25))
    evaluate = Column(String(10))
    shortcomm = Column(String)

Base.metadata.create_all(engine)

############## 删除表
#Base.metadata.drop_all(engine)

# 添加数据，创建一个会话对象，用于执行SQL语句
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind = engine)
session = DBSession()

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
    header = {}

    header['user-agent'] = user_agent

    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text,'html.parser')

    return bs_info

def get_movie_info(movie_url):
    bs_info = get_url_name(movie_url)
    for tags in bs_info.find_all('span',attrs={'class':'short'}):
        new_data = Mytable(shortcomm=tags.get_text())
        session.add(new_data)

urls = tuple(f'https://book.douban.com/subject/10750155/comments/hot?p={page}' for page in range(1,189))

from time import sleep

if __name__ == '__main__':
    for page in urls:
        get_movie_info(page)
        sleep(5)
    session.commit()
    session.close()