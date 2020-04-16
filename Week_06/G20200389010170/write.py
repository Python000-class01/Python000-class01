import csv
import jieba
import pymysql
import pandas as pd


dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'zhao',
    'db' : 'test'
}




sqls = ['select 1', 'select VERSION()']

result = []

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
            db = self.db,

        )

        cursor = conn.cursor()
        cursor.execute("use test")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `new` (`id` int NOT NULL auto_increment PRIMARY KEY, `short` TEXT NOT NULL, `sentiment` DECIMAL (5, 4) NOT NULL )")
        with open("sentiment.csv") as my_file:
            reader = csv.reader(my_file)
            for index, short, sentiment in reader:
                if index == '':
                    continue
                else:
                    sql = "insert into new (short, sentiment) values (%s, %s)"

                    cursor.execute(sql, (short, float(sentiment)))
        conn.commit()




if __name__ == "__main__":
    db = ConnDB(dbInfo, sqls)


