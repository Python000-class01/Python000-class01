import pandas as pd
import numpy as np
import pymssql
import MySQLdb

connect = pymssql.connect(server='39.106.00.0',port='1469',user='sa',password='tom1', database ='Ched')
sql = 'select * from data'
df = pd.read_sql(sql,connect)

# select * from data
df
# select * from data limit(10)
df.loc[0:9]
# select id  from data  //id 是 data 表的特定一列
df['id']
# select count(id) from data
df['id'].count()
# select * from data where id <1000 and  age >30 
df[ (df['id']<1000]) & (df['age']>30) ]
# select id , count(distinct orderid) from data group by id;
df[['id','orderid']].groupby('id').agg({'orderid':pd.Series.nunique})
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(df1, df2, on = 'id', how = 'inner')
# select * from t1 union select * from t2
pd.concat([df1, df2])
# delete from t1 where id=10
df1.drop(df1[df1.id=10].index)
# alter table t1 drop column name
df1.drop(df.columns['name'], axis = 1) 
