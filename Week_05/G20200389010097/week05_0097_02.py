import pandas as pd
from snownlp import SnowNLP
import pymysql

df = pd.read_csv('book_utf8.csv')
df.columns = ['star', 'vote', 'shorts']
star_to_number = {
    '力荐': 5,
    '推荐': 4,
    '还行': 3,
    '较差': 2,
    '很差': 1
}
df['new_star'] = df['star'].map(star_to_number)


# df_test = df[df['new_star']==3]
# test_line = df_test['shorts'].iloc[10]
# print(test_line)
# s = SnowNLP(test_line)
# print(f'sentiment:{s.sentiments},text:{test_line}')
# print(type(s.sentiments))

# def _sentiment(text):
# #     s = SnowNLP(text)
# #     return s.sentiments
dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'stonezpl',
    'db' : 'nlp'
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
    # 游标建立的时候就开启了一个隐形的事物
    cur = conn.cursor()
    values = (text,s.sentiments)
    sql = 'insert into short_sentiment values (%s,%s)'
    cur.execute(sql,values)
    conn.commit()

df.shorts.apply(save)























