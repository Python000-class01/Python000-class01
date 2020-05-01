from snownlp import SnowNLP
import pandas as pd
import pymysql
import jieba.analyse
import pymysql


sql  =  'SELECT * FROM comments where insert_time >= DATE_FORMAT(NOW(), "%Y-%m-%d");'
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='sina_news',charset='utf8')
df = pd.read_sql(sql,conn)

df['sentiment'] = df['content'].apply(lambda x: SnowNLP(x).sentiments)
df['keywords'] = df['content'].apply(lambda x: list(jieba.analyse.extract_tags(x, topK=5, withWeight=False)))


class Mysql(object):

    def __init__(self, **kwargs):
        try:
            self.db = pymysql.connect(kwargs['ip'], kwargs['username'], kwargs['password'], kwargs['db'])
            self.cursor = self.db.cursor()
        except KeyError as e:
            print(f'{e} is not found' )
        except pymysql.err.InternalError:
            print('没找到数据库')

    def insert(self, **kwargs):
        table = kwargs['table']
        data = kwargs['data']
        keys = ','.join(data.keys())
        values = ','.join(str(s) for s in map(lambda key: f'"{key}"' if type(key) == str else key, data.values()))
        sql = f'REPLACE INTO {table} ({keys}) VALUES ({values});'
        self.cursor.execute(sql)
        self.db.commit()

    def close(self):
        self.db.close()



mysql = Mysql(ip='127.0.0.1', username='root', password='root', db='sina_news')


for i in range(0, len(df)):
    record = df.iloc[i]
    c_id = record['id']
    sentiment = record['sentiment']
    keywords = record['keywords']
    try:
        mysql.insert(table='sentiments', data={
            "c_id": c_id,
            "sentiment": sentiment,
        })
    except Exception as e:
        print(e)
    try:
        [mysql.insert(table='keywords', data={
            "c_id": c_id,
            "keyword": word,
        }) for word in keywords]
    except Exception as e:
        print(e)

mysql.close()
