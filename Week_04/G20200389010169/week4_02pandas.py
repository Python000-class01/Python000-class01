import pandas as pd
import numpy as np
import pymysql

#table df1
sql  =  'SELECT *  FROM data1'
conn = pymysql.connect(
    host='192.168.44.132',
    port=3306,
    user='pymysql',
    passwd='pymysql',
    db='pytest',
    charset='utf8'
)
df1 = pd.read_sql(sql,conn)
print(df1)
conn.close()

##table df2
sql  =  'SELECT *  FROM data2'
conn = pymysql.connect(
    host='192.168.44.132',
    port=3306,
    user='pymysql',
    passwd='pymysql',
    db='pytest',
    charset='utf8'
)
df2 = pd.read_sql(sql,conn)
print(df2)
conn.close()
# select * from data1
df1
# select * from data1 limit(10)
df1.head(10)
# select id  from data1  //id 是 data 表的特定一列
df1['id']
# select count(id) from data1
df1['id'].count()
# select * from data1 where id <1000 and  age >30
df1[(df1['id']<1000) & (df1['age']>30)]
# select id , count(distinct orderid) from data1 group by id;
df2.groupby('age').aggregate({'orderid':'count'})
# select * from table1 t1 inner join table2 t2 on t1.id = t2.id
pd.merge(df1, df2, on = 'id', how = 'inner')
# select * from t1 union select * from t2
pd.concat([df1, df2])
# delete from t1where id=10
df1 [df1['id'] != 10 ]
# alter table t1 drop column name
df1.drop(columns = ['age'])
