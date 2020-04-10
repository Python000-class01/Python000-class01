from pandas import pandas as pd
import snownlp
import pymysql
import sqlalchemy import create_engine

df = pd.read_csv('./book_douban/comment_4913064.txt')
df["sentiments"]= df["content"].map(lambda c : snownlp.SnowNLP(c).sentiments)
engine = create_engine('mysql+pymysql://192.168.2.189:root@Aa1234')
df.to_sql(name='test_snownlp', con=engine, chunksize=1000, if_exists='replace', index=None)
