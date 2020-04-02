# -*- encoding=utf-8 -*-
# @File: week04_0108_ex.py
# @Author：wsr
# @Date ：2020/3/31 19:21
import pymysql
import pandas as pd

# select * from data
sql = 'SELECT *  FROM user_test'
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='test', charset='utf8')
df_user = pd.read_sql(sql, conn)

data=[[3, 23 ,170],[8, 34,165]]
columns = ['id', 'age','height']
t2 = pd.DataFrame(data=data,columns=columns)

# select * from data limit(10)
print(df_user.head(10))
print(df_user[:10])

#select id  from data  //id 是 data 表的特定一列
ids = df_user['id']
print(ids)

#select count(id) from data
count = len(df_user['id'])
print(count)

#select * from data where id <1000 and  age >30
r5 = df_user[(df_user['id']< 13) & (df_user['age']>22)]

#select id , count(distinct orderid) from data group by id;
r6 = df_user.groupby('id').agg({'age': pd.Series.nunique}).index


#select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
r7 = pd.merge(df_user,t2,on='id')
print(r7)

#select * from t1 union select * from t2
df1 = pd.DataFrame(df_user)
df2 = pd.DataFrame(t2)
pd.concat([df1, df2]).drop_duplicates()

t3 = df_user.loc[:100]
t4 = df_user.loc[100:200]
r8 = pd.concat([df1,df2])

#delete from t1where id=10
tips = df_user.loc[df_user['id'] == 9]


#alter table t1 drop column name
r10 = df_user.drop('age',axis = 1)