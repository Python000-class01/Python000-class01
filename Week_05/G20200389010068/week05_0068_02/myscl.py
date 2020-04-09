 from snownlp import SnowNLP
 import pandas as pd
 import numpy as np
 import pymysql

 info = {
     'host': '202.13.39.10',
     'port': 2309,
     'user': 'root',
     'password': '123456',
     'db': 'test'
 }


 class connect(object):
     def __init__(self, info):
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
     con = connect(dbinfo)
     df = pd.read_csv('data.csv', header=None)
     df.columns = ['bookreview']
     for index, line in df.iterrows():
         br = line.loc['bookreview']
         snow = SnowNLP(br)
         tendency = snow.sentiments
         sql = f"insert into bookreview values ({index},'{br}','{tendency}')"
         print(sql)
     print(con.run('select * from bookreview'))