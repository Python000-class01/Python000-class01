import pandas as pd
import numpy as np
import pymssql

#select * from data
#pandas基础数据操作
data1 = pd.read_excel(r'datatest.xls', sheet_name=0)
print(data1)

#dataframe数据格式实现
connect = pymssql.connect('localhost','root','passwd','database', charset='utf8', use_unicode=True)
df = pd.read_sql('select * from Table',connect)

#select * from data limit(10)
print(data1[1:10])
df.loc[1:10]

#select id  from data  //id 是 data 表的特定一列
data1.columns = ['id']
print(data1['id'])
df_id = df['id']

#select count(id) from data
data1.groupby('id').count()
df.groupby('id').count()

#select * from data where id <1000 and  age >30
data1[(data1['id'] < 1000) & (data1['age'] > 30)]
df[(df['age']>30) & (df['id']<1000)]

#select id , count(distinct orderid) from data group by id;
data1.groupby('id').agg({'orderid': pd.Series.nunique})
#df.groupby(['id']).['orderid'].count()

#select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(t1, t2, left_on='id', right_on='id')

#select * from t1 union select * from t2
pd.merge(t1, t2)

#delete from t1where id=10
data1.drop(data1[data1['id'] == 10], axis=0)
df.drop[(['id'],axis=0)]

#alter table t1 drop column name
data1.drop('name', 1)
df.drop(df.columns['name'],axis = 1)