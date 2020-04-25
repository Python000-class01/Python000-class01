import os
import pandas as pd


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import Config
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()


# 读取数据
df1 = pd.read_sql('news', engine)

df2 = pd.read_sql('sentiments', engine)
df = pd.merge(df1, df2, on='content_id', how='left')

# print(df.info())
# print(df[df['sentiment'].isna()])

_data = df[df['sentiment'].isna()]
print(_data)

from snownlp import SnowNLP
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

_data["sentiment"] = _data.ndesc.apply(_sentiment)
# 查看结果
print(_data)
# # 分析平均值
print(_data.sentiment.mean())


data = _data[['content_id', 'sentiment']]
data.to_sql(name='sentiments', con=engine, if_exists='append', index=False, chunksize=100)

