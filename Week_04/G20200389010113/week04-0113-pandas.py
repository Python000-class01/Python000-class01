import pandas as pd 


df1 = pd.read_csv('a.csv')
df1.columns = ['a', 'b', 'c', 'd', 'e', 'f']

df2 = pd.read_csv('b.csv')
df2.columns = ['a', 'b', 'c', 'd', 'e', 'f']

# select * from data
print(df1)

# select * from data limit(10)
print(df1.head[:10])

# select id from data
print(df1['a'])

# select count(id) from data
print(df1['a'].count())

# select * from data where id < 1000 and age > 30
print(df1[(df1['a'] < 1000) & (df1['d'] > 30)])

# select id, count(distinct orderid) from data group by id
print(df1[['a', 'd']].groupby('a').aggregate({'b': pd.Series.nunique}))\

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
print(pd.merge(df1, df2, on = 'a', how = 'b'))

# select * from t1 union select * from t2
print(pd.concat([df1, df2]).drop_duplicates())

# delete from t1 where id=10
print(df1.drop(index=df1[df1.id==10].index))

# alter table t1 drop column name
print(df1.drop(columns='name', axis=1))