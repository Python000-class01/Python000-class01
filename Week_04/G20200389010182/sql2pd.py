import pandas as pd
import numpy as np

dfs = pd.read_csv('student.csv')
dfc = pd.read_csv('score.csv')

dfs.columns = ['id', 'name', 'sex', 'birth', 'department', 'address']
dfc.columns = ['stu_id', 'c_name', 'grade']

# 
# select * from data
dfs

# select * from data limit(3)
dfs[1:4]

# select id  from data  //id 是 data 表的特定一列
dfs['name']

# select count(id) from data
dfs['id'].count()

# select * from data where id <1000 and  age >30 
dfs[(dfs['id']<906) & (dfs['birth']>1987)]

# select id , count(distinct orderid) from data group by id;
dfs.groupby('birth').aggregate({'birth':'count'})

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(dfs, dfc, left_on ='id', right_on='stu_id', how='inner')

# select * from t1 union select * from t2
pd.concat([dfs,dfc])

# delete from t1where id=10
dfs.drop(index=[7,8])

# alter table t1 drop column name
dfs.drop(['id'], axis=1)