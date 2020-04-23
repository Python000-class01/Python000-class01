import pandas as pd
import pymysql
from snownlp import SnowNLP

# 建立mysql数据库连接
conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'mysql',
                        password = 'Pwd_2020',
                        database = 'testdb',
                        charset = 'utf8mb4')

cursor = conn.cursor()

comment = pd.read_sql_query('select mid, content, time from sina_comment', conn)
comment.columns = ['mid', 'content', 'time']

# 数据清理
comment.info()
comment.dropna()
comment.drop_duplicates()

# 情感分析
def _sentiment(text):
    return SnowNLP(text).sentiments

comment["sentiment"] = comment.content.apply(_sentiment)

# 处理后存入mysql（新表）
mid = comment['mid'].values.tolist()
content = comment['content'].values.tolist()
sentiment = comment['sentiment'].values.tolist()
# time时间形式转换为date形式
date = comment['time'].str[0:10].values.tolist()
# time = comment['time'].values.tolist()

clear_sql = 'truncate table sina_comment_sentiment'
cursor.execute(clear_sql)

sql = 'insert into sina_comment_sentiment(mid, content, sentiment, date) values (%s, %s, %s, %s)'
values = [i for i in zip(mid, content, sentiment, date)]
cursor.executemany(sql, values)



# 关闭mysql连接
cursor.close()
conn.commit()
conn.close()


