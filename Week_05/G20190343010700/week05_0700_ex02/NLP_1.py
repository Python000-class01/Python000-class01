#### ============      从pymysql 读取数据       ===========
import pymysql
import pandas as pd
import numpy as np
from snownlp import SnowNLP

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'h******',
                       database = 'test',
                       charset = 'utf8mb4'
                        )
con1 = conn.cursor()
count = con1.execute('select * from movie;')
print(f'查询到 {count} 条记录')
result = con1.fetchall()


####  ============    数据清洗        ===========
message = list(result)
rank = []
comment = []
for i in range(len(message)):
    rank.append(message[i][0])
# print(len(rank))
for i in range(len(message)):
    comment.append(message[i][1])
# print(len(comment))
c = {'rank':rank,'comment':comment}
# print(c)
data = pd.DataFrame(c)
# data2 = pd.DataFrame([rank,comment],index=("rank","comment"))
# print(data)

star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}

####  ============    情感分析        ===========
data['new_rank'] = data['rank'].map(star_to_number)
first_line = data[data['new_rank'] == 3].iloc[0]
text = first_line['comment']
s = SnowNLP(text)
print(f'情感倾向: {s.sentiments} , 文本内容: {text}')
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments
data["sentiment"] = data.comment.apply(_sentiment)
print(data.sentiment.mean())