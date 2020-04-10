# -*- coding:utf-8 -*-
from snownlp import SnowNLP
import pandas as pd
import numpy as np
import pymysql.cursors


def sen(text):
    s=SnowNLP(text)
    return s.sentiments


df=pd.read_csv("./doubancomments.csv")
df['sen']=df['comment'].map(sen)
arr=np.array(df)
arr=arr.tolist()

connection = pymysql.connect(host='localhost', 
                             user='user',
                             password='password',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    for line in arr:
        sql=f"INSERT INTO cmm(comment,sen) VALUES(%s, %s)"
        cursor.execute(sql, (line[1], line[2]))
connection.commit()
connection.close()