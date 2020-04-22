# 连接数据库
import pymysql
import pandas as pd
from snownlp import SnowNLP

sql  =  'SELECT *  FROM movie_comment'
conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'kk',
                        password = 'password',
                        database = 'testdb',
                        charset = 'utf8mb4')
df_movie = pd.read_sql(sql,conn)

cursor = conn.cursor()

df_movie.columns = ['id1', 'comment']


# 数据清洗
df_movie.dropna()
df_movie.drop_duplicates(subset=comment)



# 情感分析
def _sentiment(text):
    return SnowNLP(text).sentiments

df_movie["sentiment"] = df_movie.comment.apply(_sentiment)

# 处理后存入mysql（新表）
id1 = df_movie['id1'].values.tolist()
comment = df_movie['content'].values.tolist()
sentiment = df_movie['sentiment'].values.tolist()


sql = 'insert into movie_comment_sentiment(mid, content, sentiment, time) values (%s, %s, %s)'
values = [i for i in zip(id1, comment, sentiment)]
cursor.executemany(sql, values)


# 关闭mysql连接
cursor.close()
conn.commit()
conn.close()