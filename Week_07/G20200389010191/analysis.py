# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import matplotlib.dates as mdate
from matplotlib import style
plt.style.use('fivethirtyeight')

import pandas as pd

engine = create_engine('mysql+pymysql://root:Lxm8225873#@localhost:3306/Tencent')

sql = '''
      select * from comments
      '''
df =pd.DataFrame(pd.read_sql_query(sql, engine))
df["time_"]  = pd.to_datetime(df["time_"])
df['day'] = df.time_.dt.date

def score(comments):
    return SnowNLP(comments).sentiments  
def keywords(sentense):
    s = SnowNLP(sentense)
    return s.keywords(10)

df=df[df.comments.str.len()>0]

df['score'] = df.comments.map(score)
df['keywords'] = df.comments.map(keywords)
df['mark']  = df.score.apply(lambda x: "Positive" if x>0.8 else "Negative")

df_commentsNum = df.groupby('day')['day'].count()
df_commentsPercent =df.groupby("mark")['mark'].count()
plt.figure(figsize=(16,8))
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0))
ax1.bar(df_commentsNum.index,df_commentsNum.values,label="Daily comment")
ax2.pie( df_commentsPercent.values,labels=df_commentsPercent.index,autopct='%1.1f%%')

ax1.set_title("Daily Comment")
ax2.set_title("Proportion")
ax1.xaxis.set_major_formatter((mdate.DateFormatter("%Y-%m-%d")))
plt.subplots_adjust(hspace=0.5)
# plt.show()
plt.savefig('Public opinion.jpg')

df.to_sql('mydf', engine, index=True)
print ('Done!')