# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np

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
"""
t1 = pd.DataFrame(np.random.randint(low=5, high=12, size=(50, 3)), columns=['id', 'age', 'orderid'])
t2 = pd.DataFrame(np.random.randint(low=5, high=12, size=(50, 3)), columns=['id', 'age', 'orderid'])
print(t1)  # select * from t1
print(t2)  # select * from t2

# select * from t1 limit 10
print(t1.head(10))

# select id from t1
print(t1['id'])

# select count(id) from t1
print(t1['id'].count())

# select * from data where id <1000 and  age >30
print(t1[(t1.id < 1000) & (t1.age > 30)])

# # select id , count(distinct orderid) from data group by id;
d = t1.groupby(['id']).agg({'orderid': pd.Series.nunique})
d['id'] = d.index
d = d[['id', 'orderid']]
print(d)

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id, how=inner,outer,left,right
print(pd.merge(t1, t2, how='inner', left_on=['id'], right_on=['id']))

# select * from t1 union select * from t2
print(pd.concat([t1, t2]))

#delete from t1 where id=10
print(t1.drop(t1[t1.id == 10].index))

#alter table t1 drop column name
del t1['id']
print(t1)
