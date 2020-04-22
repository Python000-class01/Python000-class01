import sqlite3

from snownlp import SnowNLP
import pandas as pd
import jieba.analyse


sql  =  'SELECT * FROM zhihu_comment'
conn = sqlite3.connect('zhihu_scrapy/zhihu.db')
c = conn.cursor()
df = pd.read_sql(sql, conn)

df['sentiment'] = df['comment'].apply(lambda x: SnowNLP(x).sentiments)
df['keywords'] = df['comment'].apply(lambda x: list(jieba.analyse.extract_tags(x, topK=5, withWeight=False)))

for i in range(0, len(df)):
    record = df.iloc[i]
    c_id = record['id']
    sentiment = record['sentiment']
    keywords = record['keywords']
    try:
        c.execute('update zhihu_comment set sentiment = ?, keywords = ? where id = ?', [sentiment, keywords, c_id])
        conn.commit()
    except Exception as e:
        print(e)
    

conn.close()