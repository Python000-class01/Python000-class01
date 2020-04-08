from snownlp import SnowNLP
import pandas as pd
import os
from sqlalchemy import create_engine

#设置需要分析文件
yp = os.path.join(os.path.abspath("."),"cj1.txt")
#读取每条评论分别进行情感测试
qg = []
pj = []
for dp in open(yp,encoding="utf-8"):
    s = SnowNLP(dp)
    qg.append(s.sentiments)
    pj.append(dp)
#将数据整理为dataframe
text = pd.DataFrame({'qinggan':qg,'duanping':pj})

#入库

engine = create_engine(
        "mysql+pymysql://python:123456@14.14.14.20:3306/python?charset=utf8",
        echo=True)


pd.io.sql.to_sql(text,'qgfx',con=engine,schema='python',if_exists='append')
engine.dispose()




