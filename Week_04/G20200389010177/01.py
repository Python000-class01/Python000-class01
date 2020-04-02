import pandas as pd
import numpy as np

# select * from data
df = pd.DataFrame(pd.read_excel('xxx.xlsx'))

# select * from data limit(10)
df.head(10)

# select id  from data  //id 是 data 表的特定一列
df['id']

# select count(id) from data
df.id.count()

# select * from data where id <1000 and  age >30
df[(df['id']<1000) & (df['age']>30)]

# select id , count(distinct orderid) from data group by id
df.groupby('id')['orderid'].count()

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
df.merge(t1, t2, on='id')

# select * from t1 union select * from t2
df.contact([t1, t2])

# delete from t1 where id=10
df.drop(df['id']==10)

# alter table t1 drop column name
df.drop(['name'], axis=1)

