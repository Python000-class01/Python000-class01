import requests
import lxml.etree
import os
from os import path
import numpy as np
from snownlp import SnowNLP
import csv
import pandas as pd
import pymysql
from sqlalchemy import create_engine
############ 创建数据表
from sqlalchemy import Column, Integer, String, DateTime
# 常用数据类型

from sqlalchemy.ext.declarative import declarative_base

# 添加数据，创建一个会话对象，用于执行SQL语句
from sqlalchemy.orm import sessionmaker

# 爬取页面详细信息

# 图书详细页面
url = 'https://movie.douban.com/subject/34805219/comments?status=P'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent': user_agent}

response = requests.get(url, headers=header)

# xml化处理
selector = lxml.etree.HTML(response.text)
engine = create_engine(
    "mysql+pymysql://root:hx123456@127.0.0.1:3306/test?charset=utf8",
    echo=True)
Base = declarative_base()


class DoubanMoiveEntity(Base):
    # 表名
    __tablename__ = "douban_movie"
    # 字段，属性
    id = Column(Integer, primary_key=True)
    comment = Column(String(500), unique=True)
    score = Column(Integer)


DBSession = sessionmaker(bind=engine)
session = DBSession()

try:
    f = open('douban_movie.csv', 'w', encoding='utf_8_sig', newline='')
    for i in range(1, 10):
        context = selector.xpath(
        f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()')
        score = selector.xpath(
            f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[1]/span/text()')
        csv_writer = csv.writer(f)
        csv_writer.writerow(context)
        new_data = DoubanMoiveEntity(comment=context, score=score)
        session.add(new_data)
finally:
    if f:
        f.close()
    
session.commit()
session.close()
   

# # 加载爬虫的原始评论数据
# df = pd.read_csv('douban_movie.csv')
# # 调整格式
# df.columns = ['star', 'vote', 'shorts']
# star_to_number = {
#     '力荐': 5,
#     '推荐': 4,
#     '还行': 3,
#     '较差': 2,
#     '很差': 1
# }
# df['new_star'] = df['star'].map(star_to_number)
# # 用第一个评论做测试
# first_line = df[df['new_star'] == 3].iloc[0]
# text = first_line['shorts']
# s = SnowNLP(text)
# print(f'情感倾向: {s.sentiments} , 文本内容: {text}')

# # 封装一个情感分析的函数


# def _sentiment(text):
#     s = SnowNLP(text)
#     return s.sentiments


# df["sentiment"] = df.shorts.apply(_sentiment)
# # 查看结果
# df.head()
# # 分析平均值
# df.sentiment.mean()
