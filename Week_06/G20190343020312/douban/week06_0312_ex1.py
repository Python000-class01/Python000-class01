import requests
import lxml.etree
import pandas as pd
from time import sleep
from snownlp import SnowNLP
from sqlalchemy import create_engine
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



movie_data = []

# 获取短评数据
def get_short_comment(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    header = {
            'user-agent':user_agent
    }
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    for i in range(1, 5):
        movie_score = selector.xpath(
            f"//div[@class='comment-item'][{i}]//span[@class='comment-info']/span[2]/@title")
        movie_comment = selector.xpath(
            f"//div[@class='comment-item'][{i}]//div[@class='comment']//p/span/text()")
        movie_data.append(movie_score + movie_comment)


urls = tuple(f'https://movie.douban.com/subject/1292052/comments?start={page * 20}&limit=20&sort=new_score&status=P' for page in range(5))  


# 根据短评进行情感分析
def sentiment_analyais(data):
    column_name = ['star', 'shorts']  # 定义列名
    df = pd.DataFrame(columns=column_name, data=data)
    print(df.head())
    # 加载爬虫的原始评论数据
    star_to_number = {
        '力荐': 5,
        '推荐': 4,
        '还行': 3,
        '较差': 2,
        '很差': 1
    }
    df['score'] = df['star'].map(star_to_number)
    df = df.dropna(how='any')

    # 封装一个情感分析的函数
    def _sentiment(text):
        s = SnowNLP(text)
        return s.sentiments

    df["sentiment"] = df.shorts.apply(_sentiment)

    # 分析平均值
    print(df.sentiment.mean())

    return df

# 将评分、评论、情感分析结果存入mysql
def save_to_mysql(df):
    engine = create_engine(
            "mysql+pymysql://root:gentoo@localhost:3306/test?charset=utf8", echo=True)
    conn = engine.connect()
    df.to_sql(name='mytable', con=engine, if_exists='append', index=False, index_label=False)


if __name__ == '__main__':
    for url in urls:
        get_short_comment(url)
    df = sentiment_analyais(movie_data)
    save_to_mysql(df)
