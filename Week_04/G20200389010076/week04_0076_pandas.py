
# select * from data
data

# select * from data limit(10)
data[:10]

# select id  from data
data['id']

# select count(id) from data
data['id'].count()

# select * from data where id <1000 and  age >30
data[(data.id<1000) & (data.age>30)]

# select id , count(distinct orderid) from data group by id;
data.drop_duplicates().groupby('id').aggregate({'orderid':'count'})

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(t1,t2,on='id',how='inner')

# select * from t1 union select * from t2
print(pd.concat([t1,t2]))

# delete from t1 where id=10
t1.loc[t1['id'] != 10]

# alter table t1 drop column name
df.drop('A', axis=1)