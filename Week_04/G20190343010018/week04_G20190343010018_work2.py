import pandas as pd

df = pd.read_csv('test.csv')

# select * from data
value1 = df.iloc[:,:].values

# select * from data limi(10)
value2 = df.loc[:10, :]

# select id frm data
id_value = df[['id']].values

# select count(id) from data
id_count = len(id_value)

# select * from data where id <1000 and  age >30
value3 = df[(df['id']<1000) & (df['age']>30)].values

# select id , count(distinct orderid) from data group by id;
value4 = df[['id', 'distinct orderid']].group_by('id')

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
value5 = pd.merge(t1, t2, on=['id'])

# select * from t1 union select * from t2
value6 = pd.merge(t1, t2)

# delete from t1 where id=10
value7 = t1.drop(t1['id']==10, axis=1)

# alter table t1 drop column name
value8 = t1.drop(t1.comums, axis=1)