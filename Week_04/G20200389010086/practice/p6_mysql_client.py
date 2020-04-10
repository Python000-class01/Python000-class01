# mysql  连接

import pymysql

db = pymysql.connect(host='localhost', db='test', user='root', passwd='332315Yuan@',port=3306)

print(db)
