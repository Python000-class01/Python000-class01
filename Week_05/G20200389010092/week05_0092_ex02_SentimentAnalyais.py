####################
# 《不完美的她》剧评
# https://movie.douban.com/subject/33446498/comments?start=0&limit=20&sort=time&status=P
# 评价 //div[@class="comment-item"][i]//span[@class="comment-info"]/span[2]/@title
# 评论 //div[@class="comment-item"][i]//div[@class="comment"]//p/span/text()

import requests
import lxml.etree
import pandas as pd
from time import sleep
from snownlp import SnowNLP
from sqlalchemy import create_engine
import pymysql

####################
# 获取短评数据
def get_movie_data(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    for i in range(1, 21):
        movie_score = selector.xpath(
            f"//div[@class='comment-item'][{i}]//span[@class='comment-info']/span[2]/@title")
        movie_comment = selector.xpath(
            f"//div[@class='comment-item'][{i}]//div[@class='comment']//p/span/text()")
        movie_data.append(movie_score + movie_comment)


urls = tuple(
    f'https://movie.douban.com/subject/33446498/comments?start={ page * 20 }&limit=20&sort=new_score&status=P' for page in range(10))  # 把所有url存在元组中

movie_data = []

####################
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

####################
# 将评分、评论、情感分析结果存入mysql
def to_sql(df):
    engine = create_engine(
        "mysql+pymysql://{}:{}@{}/{}".format('root', '******', 'localhost:3306', 'test'))
    con = engine.connect()
    df.to_sql(name='test', con=con, if_exists='append', index=False)


if __name__ == '__main__':
    for page in urls:
        get_movie_data(page)
        sleep(6)
    df = sentiment_analyais(movie_data)
    to_sql(df)
