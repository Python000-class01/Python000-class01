import pandas as pd

df1 = pd.read_csv('data_1.csv')
df2 = pd.read_csv('data_2.csv')

# select * from data
df1

# select * from data limit(10)
df1.head(10)

# select id from data
df1['id']

# select count(id) from data
df1.id.count()

# select * from data where id <1000 and  age >30
df1[df1['id'] < 1000 & df1['age'] > 30]

# select id , count(distinct orderid) from data group by id
df1.groupby('id').count()

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(df1, df2, on='id')

# select * from t1 union select * from t2
pd.concat([df1, df2]).drop_duplicates()

# delete from t1 where id=10
df1.drop(df['id'] == 10)

# alter table t1 drop column name
df1.drop('name', axis=1)
