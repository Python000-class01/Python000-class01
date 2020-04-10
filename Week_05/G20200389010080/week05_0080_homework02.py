import pandas as pd
from snownlp import SnowNLP
import pymysql

df = pd.read_csv('name.csv')
df.columns = ['star', 'vote', 'shorts']
review = {
    '推荐': 3,
    '还行': 2,
    '很差': 1
}
df['new_star'] = df['star'].map(review)

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'pw',
    'db' : 'database'
}
def save(text):
    s = SnowNLP(text)
    conn = pymysql.connect(
        host=dbInfo['host'],
        port=dbInfo['port'],
        user=dbInfo['user'],
        password=dbInfo['password'],
        db=dbInfo['db']
    )
 
    cur = conn.cursor()
    values = (text,s.sentiments)
    sql = 'insert into short_sentiment values (%s,%s)'
    cur.execute(sql,values)
    conn.commit()

df.shorts.apply(save)