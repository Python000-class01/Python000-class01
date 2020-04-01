import pymysql
import pandas as pd
'''
用pandas pymysql连接数据库，并获取数据
sql  = "select * from data"
conn = pymysql.connect('ip','name','passwd','dbname','charset=utf8')
data = pd.read_sql(sql,conn,)
'''
#用pandas读取csv
data2 = pd.read_csv('C:\\Users\\ppton\\Desktop\\aaa.csv')

#读取dataFrame对象中所有数据---jop1
# print(data2)

#读取前十行数据---jop2
# print(data2[1:11])

#读取特定的一列数据例如  列的名字叫做IP---jop3
# print(data2['ip'])

#读取特定一行的数据 例如IP为"172.20.9.32"的数据---jop4
# print(data2[data2['ip'] == "172.20.9.32"])

#按条件读取  select * from data where id <1000 and  age >30 ---jop5
# print(data2[(data2['连接数'] < 200) & (data2['磁盘使用百分比'] > 50)])

#select id , count(distinct orderid) from data group by id ---jop6
# print(data2.groupby('os').count())

#select * from table1 t1 inner_join table2 t2 on t1.id = t2.id ---jop7
# pd.merge(table1,table2,on = 'id',how = 'inner')

#select * from t1 union select * from t2 ---jop8
# pd.merge(table1,table2,on = 'id',how = 'outer')

#delete from t1where id=10 --jop9
# data3 = data2[data2['id'] != "10"]

#alter table t1 drop column name ---jop10
# data2.drop(columns=['os'])





