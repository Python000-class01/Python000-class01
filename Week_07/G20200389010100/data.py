import pandas as pd
import pymysql
from snownlp import SnowNLP

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='mysql',
    password='touhou',
    database='testdb',
    charset='utf8mb4'
)

cursor = conn.cursor()

comment = pd.read_sql_query('select mid, content, time from sina_comment', conn)
comment.columns = ['mid', 'content', 'time']

comment.info()
comment.dropna()
comment.drop_duplicates()


def _sentiment(text):
    return SnowNLP(text).sentiments


comment["sentiment"] = comment.content.apply(_sentiment)

mid = comment['mid'].values.tolist()
content = comment['content'].values.tolist()
sentiment = comment['sentiment'].values.tolist()
date = comment['time'].str[0:10].values.tolist()
# time = comment['time'].values.tolist()

clear_sql = 'truncate table comment_sentiment'
cursor.execute(clear_sql)

sql = 'insert into comment_sentiment(mid, content, sentiment, date) values (%s, %s, %s, %s)'
values = [i for i in zip(mid, content, sentiment, date)]
cursor.executemany(sql, values)

# 关闭mysql连接
cursor.close()
conn.commit()
conn.close()
