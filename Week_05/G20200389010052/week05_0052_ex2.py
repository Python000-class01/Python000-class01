from snownlp import SnowNLP
import pandas as pd
import numpy as np
import pymysql

dbinfo = {
    'host': '10.211.55.5',
    'port': 3306,
    'user': 'root',
    'password': 'pwd123',
    'db': 'test'
}


class conndb(object):
    def __init__(self, dbinfo):
        self.host = dbinfo['host']
        self.port = dbinfo['port']
        self.user = dbinfo['user']
        self.password = dbinfo['password']
        self.db = dbinfo['db']

    def run(self, sql):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8mb4'
        )
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchone()
            cur.close()
            conn.commit()
            return result
        except:
            conn.rollback()
        conn.close()


if __name__ == "__main__":
    conndb_ = conndb(dbinfo)
    df = pd.read_csv('data.csv', header=None)
    df.columns = ['bookreview']
    for index, line in df.iterrows():
        # print(line.loc['bookreview'])
        br = line.loc['bookreview']
        snow = SnowNLP(br)
        # print(snow.words)
        # print(list(snow.tags))
        tendency = snow.sentiments
        sql = f"insert into bookreview values ({index},'{br}','{tendency}')"
        print(sql)
        # print(conndb_.run(sql))
    print(conndb_.run('select * from bookreview'))