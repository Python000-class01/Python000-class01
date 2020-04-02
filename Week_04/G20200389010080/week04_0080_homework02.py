# 作业二：

# 请将以下的 SQL 语句翻译成 Pandas 语句。


import pymysql
import pandas as pd


# select * from data
sql  =  'SELECT *  FROM data'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
data = pd.read_sql(sql,conn)
print(data)

# select * from data limit(10)
print(data.head(10))

# select id  from data  //id 是 data 表的特定一列
print(data['id'])

# select count(id) from data
print(data['id'].count())

# select * from data where id <1000 and  age >30 
print(data[(data['id']<1000) & (data['age']>30) ])

# select id , count(distinct orderid) from data group by id;
print(data.groupby('id').nunique('orderid'))

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
print(pd.merge(table1, table2, on = 'id'))

# select * from t1 union select * from t2
print(pd.concat(t1, t2))

# delete from t1where id=10
data = data[data.id != 10]
print(data)

# alter table t1 drop column name
print(data.drop(['name'], axis = 1))
