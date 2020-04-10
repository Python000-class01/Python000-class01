import pandas as pd

df1 = pd.read_csv('test.csv')

# select * from data
df1

# select * from data limit(10)
df1.head(10)

# seledt id  from data  //id是data表的特定一列
df1['id]

# select count(id) from data
df1['id'].numique()

# select * from data where id <1000 and  age >30 
df1[  (df1['id'] <1000)  &( df1['age'] >30 )   ]

# select id , count(distinct orderid) from data group by id;
df1.groupby('id')['orderid'].nunique()

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
df.merge(table1, table2, on = 'id', how = 'inner')


# select * from t1 union select * from t2
order_union = df1.concat([t1, t2]).drop_duplicates()


# delete from t1where id=10
df1[ df1['id'] != 10 ]

# alter table t1 drop column name
df1.drop(['name'], inplace = True, axis =1)







