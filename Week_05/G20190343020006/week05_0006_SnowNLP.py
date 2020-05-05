import pandas as pd
from snownlp import SnowNLP
import pymysql

result = []

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '109d328',
    'db' : 'snowtest'
}
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = '109d328',
                       database = 'snowtest',
                       charset = 'utf8mb4'
                        )



class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

        self.run()

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

if __name__ == "__main__":
    strings = pd.read_csv('review.csv').to_string()
    s = SnowNLP(strings)
    rank = s.sentiments
    sql = ['select * from rankinfo', "insert into rankinfo(id,rank,contents) values(1,0.44,'sdasdasdasd')"]
    db = ConnDB(dbInfo, sql)
    print(result)
    con1 = conn.cursor()
    sql2 = con1.execute("insert into rankinfo(id,rank,contents) values(1,0.44,'sdasdasdasd')")

