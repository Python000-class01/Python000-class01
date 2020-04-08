from snownlp import SnowNLP
from os import path
import pymysql

dir = path.dirname(__file__)
text = open(path.join(dir, 'bwbjcp.txt'),encoding='utf-8').read()
s = SnowNLP(text)
fx = s.sentiments
print(fx)

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