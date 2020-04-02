import pandas as pd
import numpy as np
import pymysql
# select * from data
sql  =  'SELECT *  FROM mytable'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df = pd.read_sql(sql,conn)
# select * from data limit(10)
df.head(10)
# select id  from data  //id 是 data 表的特定一列
df['id']
# select count(id) from data
df.shape
# select * from data where id <1000 and  age >30
df[df['id'] < 1000 & df[age] > 30]
# select id , count(distinct orderid) from data group by id;
df.drop_duplicates(subset='orderid')
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
sql1 =  'SELECT *  FROM mytable'
conn1 = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df1 = pd.read_sql(sql1,conn1)

sql2  =  'SELECT *  FROM mytable'
conn2 = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df2 = pd.read_sql(sql2,conn2)

pd.merge(df1, df2, on='id', how='inner')
# select * from t1 union select * from t2
pd.concat([df1, df2], ignore_index=True).drop_duplicates()
# delete from t1 where id=10
df[df['id'] != 10]
# alter table t1 drop column name
df.drop(columns=['name'])