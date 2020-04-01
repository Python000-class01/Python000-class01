"""
select * from data
select * from data limit(10)
select id  from data  //id 是 data 表的特定一列
select count(id) from data
select * from data where id <1000 and  age >30 
select id , count(distinct orderid) from data group by id;
select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
select * from t1 union select * from t2
delete from t1where id=10
alter table t1 drop column name
假设文件为 csv 文件
"""

import pandas as pd

df = pd.read_csv('xxx.csv')

# select * from data
val1 = df.iloc[:,:].values

# select * from data limi(10)
val2 = df.loc[:10, :]

# select id frm data
id_val = df[['id']].values

# select count(id) from data
id_count = len(id_val)

# select * from data where id <1000 and  age >30 
val3 = df[(df['id']<1000) & (df['age']>30)].values

# select id , count(distinct orderid) from data group by id;
val4 = df[['id', 'distinct orderid']].group_by('id')

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
cat = pd.merge(t1, t2, on=['id'])

# select * from t1 union select * from t2
cat2 = pd.merge(t1, t2)

# delete from t1 where id=10
tn = t1.drop(t1['id']==10, axis=1)

# alter table t1 drop column name
tn = t1.drop(t1.comums, axis=1)