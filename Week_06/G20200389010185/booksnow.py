from snownlp import SnowNLP
import pandas as pd
import os
import string
from sqlalchemy import create_engine


yp = os.path.join(os.path.dirname(os.path.abspath(__file__)),"cj1.txt")
books = pd.read_table(yp)

star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1,
    'None' : 3,
}
books['score'] = books['star'].map(star_to_number)

emotion = []
for short in books['shorts']:
    s = SnowNLP(short)
    emotion.append(s.sentiments)


books['emotions'] = emotion
print(books)


#入库

engine = create_engine(
        "mysql+pymysql://python:123456@14.14.14.20:3306/python?charset=utf8",
        echo=True)


pd.io.sql.to_sql(books,'emotion',con=engine,schema='python',if_exists='append')
engine.dispose()
