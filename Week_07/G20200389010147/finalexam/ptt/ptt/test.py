import pymysql
conn = pymysql.connect('127.0.0.1','root','root','ptt')

#db = pymysql.connect("127.0.0.1", "root", "password", "exercise_1")

cursor = conn.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
print(cursor.execute("SELECT * FROM ptt_gossiping"))