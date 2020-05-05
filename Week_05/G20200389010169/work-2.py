# 作业二：
# 使用 snowNLP 预测豆瓣中任意一本书评或影评的评论是正向还是负向，并将评论内容和评分使用 PyMySQL 存入 MySQL 数据库。

from snownlp import SnowNLP
from os import path
dir = path.dirname(__file__)
text = open(path.join(dir, 'bwbjcp.txt'),encoding='utf-8').read()
s = SnowNLP(text)
fx = s.sentiments
print(fx)
import pymysql

db = pymysql.connect(
    host='192.168.44.132',
    port=3306,
    user='pymysql',
    passwd='pymysql',
    db='pytest',
    charset='utf8'
)

cursor = db.cursor()
sql = "insert into douban(pingjia,fenxi) values('%s','%s')"%(text,fx)
cursor.execute(sql)
cursor.close()
db.commit()
db.close()
