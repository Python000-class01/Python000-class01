from snownlp import SnowNLP
import pandas as pd
import pymysql

DB_NAME = 'test'
TABLE_NAME = 'movie_comment_nlp'


# 封装一个情感分析的函数
def get_sentiments(text):
    s = SnowNLP(text)
    return s.sentiments

dbInfo = {
    'host' : '192.168.3.144',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : DB_NAME
}


class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls
        self.result = []

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
                self.result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except Exception as e:
            print(e)
            print('rollback')
            conn.rollback()
        # 关闭数据库连接
        conn.close()

if __name__ == "__main__":
    df = pd.read_csv('../movei_comment_data/当幸福来敲门800影评.csv')
    df = df.dropna()

    print('calculating sentiments  ...')
    df['sentiments'] = df.comment_content.apply(get_sentiments)
    df['good_or_bad'] = df.sentiments > 0.8
    print('calculating sentiments over')
    print(f'value shape {df.shape}')

    print('saving db ...')
    commands = []
    commands.append(f'drop table if exists {TABLE_NAME}')
    commands.append(f'create table {TABLE_NAME} (content varchar(3000) character set utf8, score double, positive bool) default charset=utf8')
    for row in df.values:
        comment = ''
        for ch in row[2]:
            if ch == '\'' or ch == '"':
                continue
            comment += ch

        commands.append(f'insert into {TABLE_NAME} (content, score, positive) values ("{comment}", {row[3]}, {"true" if row[4] else "false"})')

    db = ConnDB(dbInfo, commands)
    print('saving db over')