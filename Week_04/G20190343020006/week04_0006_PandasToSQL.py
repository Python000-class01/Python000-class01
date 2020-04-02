import pandas as pd

df = pd.read_csv('data.csv')

# select * from data
print(df)

# select * from data limit(10)
print(df['data']== 10)
# select id  from data  //id 是 data 表的特定一列
print(df['id'])
# select count(id) from data
print(df['id'].count())
# select * from data where id <1000 and  age >30 
print(( df['age']>30 ) & ( df['id']<1000)) 
# select id , count(distinct orderid) from data group by id;
print(df['id'].count('orderid'))
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(t1, t2, on= 'id', how='inner')
# select * from t1 union select * from t2
pd.merge(t1, t2)
# delete from t1where id=10
df.drop(df['id'] == 10)
# alter table t1 drop column name
