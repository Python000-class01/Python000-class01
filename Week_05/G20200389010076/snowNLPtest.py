#coding:utf-8
from snownlp import SnowNLP
import pandas as pd
import numpy as np
from week05_homework.db import DB

def sen(text):
    s=SnowNLP(text)
    return s.sentiments



df=pd.read_csv("./doubancomments.csv")
df['sen']=df['comment'].map(sen)
arr=np.array(df)
arr=arr.tolist()

db=DB()
for line in arr:
    sql=f"INSERT INTO cmm(comment,sen) VALUES('{line[1]}','{line[2]}')"
    db.insert(sql)
