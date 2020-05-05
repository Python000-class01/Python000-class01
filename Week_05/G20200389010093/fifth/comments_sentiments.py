import pandas as pd
from snownlp import SnowNLP
import pymysql

df=pd.read_csv('comments.csv',encoding='utf-8',header=None)
df.columns=['comments']
# df.head()

def _sentiment(text):
    s=SnowNLP(text)
    return s.sentiments

df['sentiments']=df.comments.apply(_sentiment)


##MySQL创建表语句
# drop TABLE if EXISTS book_comments;
# CREATE TABLE book_comments(
# 	id int(10) not null AUTO_INCREMENT,
# 	comments MEDIUMTEXT not null,
# 	sentiments float(4,3) not null,
# 	PRIMARY KEY(id)
# )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;    #charset需设置成utf8mb4，否则无法插入，报错InternalError: (1366, u"Incorrect string value: '\\xF0\\x9F\\x90\\x98\\xE8\\ ......


dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'douban',
    'charset' :'utf8mb4'
}


class ConnDB(object):
    def __init__(self, dbInfo,df):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.charset =dbInfo['charset']
        self.df=df

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

        sql='INSERT INTO book_comments (comments,sentiments) VALUES (%s,%s)'
        try:
            for row in df.itertuples():
                cur.execute(sql,(getattr(row,'comments'),getattr(row,'sentiments')))

            ##用range(len(df))或者range(df.shape[0])来遍历，用loc来定位到指定行、列,但得到的是'numpy.float64'类型，需转化
            # values=[(str(df.loc[i,'comments']),float(df.loc[i,'sentiments'])) for i in range(len(df))]
            # cur.executemany(sql,values)

            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

if __name__ == "__main__":
    db = ConnDB(dbInfo,df)

