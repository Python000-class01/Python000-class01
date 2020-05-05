#### ============      从pymysql 读取数据       ===========
import pymysql
import pandas as pd
import numpy as np
from snownlp import SnowNLP
from sqlalchemy import create_engine

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = '*****',
                       database = 'book',
                       charset = 'utf8mb4'
                        )
con1 = conn.cursor()
count = con1.execute('select * from rensheng;')
print(f'查询到 {count} 条记录')
result = con1.fetchall()

####  ============    数据清洗        ===========
message = list(result)
print(message[0])
star = []
comment = []
for i in range(len(message)):
    star.append(message[i][1])

for i in range(len(message)):
    comment.append(message[i][3])
# print(len(comment))
c = {'star':star,'comment':comment}
# print(c)
data = pd.DataFrame(c)



star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}

####  ============    情感分析        ===========
data['star'] = data['star'].map(star_to_number)

def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments
data["sentiment"] = data.comment.apply(_sentiment)


####  ============    更新mysql数据库        ===========
sentiments = data["sentiment"].to_list()
star_rank = data['star'].to_list() 
I = range(1,count+1)
for sentiment,star,i in zip(sentiments,star_rank,I):
    print(sentiment,star,i)
    query = "UPDATE rensheng SET sentiment = {},star = {} WHERE Id = '{}'".format(sentiment,star,i)
    print(query)
    con1.execute(query)
conn.commit()
con1.close()
conn.close()













