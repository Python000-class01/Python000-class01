import pymysql

# 新闻评论数据数据库信息
newsCommentDbInfo = {
    'host' : '192.168.3.144',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'test',
    'table' : 'news_comment'
}

# 新闻评论数据数据库信息
nlpCommentDbInfo = {
    'host' : '192.168.3.144',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'test',
    'table' : 'news_nlp'
}

# 采集数量数据库信息
# 新闻评论数据数据库信息
pickCntDbInfo = {
    'host' : '192.168.3.144',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'test',
    'table' : 'news_pick_cnt'
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

        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                self.result.append(cur.fetchall())
            # 关闭游标
            cur.close()
            conn.commit()
        except Exception as e:
            print(e)
            print('rollback')
            conn.rollback()
        # 关闭数据库连接
        conn.close()