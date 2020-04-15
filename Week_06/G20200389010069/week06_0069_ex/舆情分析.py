import pandas as pd
from snownlp import SnowNLP
import pymysql


text = ['好东西，经典值得慢慢品尝 我有一本83年板古老的商务印书局的《新华词典》',
        '经典哦','读新华字典，好熟悉的感觉啊，虽然很久没看了。 那时还在上中学，我和坐在身后的同学都喜欢看新华字典，尤其是周二开校务会时，老师不容许桌上放任何书，书桌里的字典就成了我们打发时光的最好伙伴。',
        '布基纳法索吧。呵呵。',
        '记忆中，小学一年级时买的字典使用时间最长。还有一本不知是第几版的，老的都掉了皮皮。字典在学生时代可谓功不可没，现在读的次数极了。但是却读的兴趣很大了。旧象楼主说的一样。',
        '新华字典里每页都有不认识的字，真是学无止境呀',
        '哈哈，有趣',
        '喜欢有趣或擅于发现趣味的人～',
        '成语字典里面故事更多，更精彩呢 ',
        '我小时候好像最喜欢一本彩图百科字典……漂亮~'
        ]
text =str(text)

s = SnowNLP(text)
s1 = s.sentiments
print(s1)


dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'rootroot',
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
    db = ConnDB(dbInfo, sqls)
    print(result)
