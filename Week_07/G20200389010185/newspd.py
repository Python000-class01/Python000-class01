from snownlp import SnowNLP
import pandas as pd
import os
import string
from sqlalchemy import create_engine

pingjia = os.path.join(os.path.dirname(os.path.abspath(__file__)),"pingjia.txt")
shorts = pd.read_table(pingjia)
# print(shorts.drop_duplicates())
em = []
for short in shorts['shorts']:
    s = SnowNLP(short)
    em.append(s.sentiments)
shorts['em'] = em

print(shorts.drop_duplicates().iloc[33])

engine = create_engine(
        "mysql+pymysql://python:123456@14.14.14.20:3306/python?charset=utf8mb4",
        echo=True)

pd.io.sql.to_sql(shorts.drop_duplicates(),'news_em',con=engine,schema='python',index=False,if_exists='append')
engine.dispose()
