#coding=utf-8
import pandas as pd
from snownlp import SnowNLP

# 加载爬虫的原始评论数据
# df = pd.read_csv('shorts.csv', encoding="unicode_escape")
df = pd.read_csv('shorts.csv', encoding="gbk")
# 调整格式
df.columns = ['id', 'title', 'score', 'num', 'shorts']

# 用第一个电影做测试
# first_line = df[df['score'] == 9.7].iloc[0]
# text = first_line['shorts']

text = df['shorts']

# s = SnowNLP(text)
# print(f'情感倾向: {s.sentiments}, 文本内容： {text}')

# 封装一个情感分析的函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

df["sentiment"] = df.shorts.apply(_sentiment)

# 查看结果
# print(df.head())
# print(df["shorts"].values.tolist())
# print(df["sentiment"].values.tolist())
shorts = df["shorts"].values.tolist()
sentiments = df["sentiment"].values.tolist()
# 分析平均值
# print(df.sentiment.mean())

# 训练模型
# from snownlp import sentiment
# sentiment.train('neg.txt','pos.txt')
# sentiment.save('sentiment.marshal')

# 存入mysql
import pymysql
conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'mysql',
                        password = 'Pwd_2020',
                        database = 'testdb',
                        charset = 'utf8mb4')

cursor = conn.cursor()

values = [i for i in zip(shorts, sentiments)]
# print(values)
cursor.executemany('insert into sentiment(shorts, sentiment) values(%s, %s)', values)

cursor.close()
conn.commit()
conn.close()