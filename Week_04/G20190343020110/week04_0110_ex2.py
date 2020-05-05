import pandas as pd
data = [{'id': 50,'orderid': 1,'account': 'Jones LLC', 'age':18},
         {'id': 99,'orderid': 2,'account': 'Alpha Co', 'age':50},
        {'id': 102,'orderid': 3, 'account': 'Blue Inc', 'age': 20}]
data2 = [{'id': 50, 'orderid': 1, 'account': 'Jones LLC', 'age': 18},
        {'id': 99, 'orderid': 2, 'account': 'Alpha Co', 'age': 50},
        {'id': 102, 'orderid': 3, 'account': 'Blue Inc', 'age': 20}]

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
#select * from data
print(df.head())
#select * from data limit(10)
print(df.head(10))
#select id  from data
print(df['id'].head())
#select count(id) from data
print(df['id'].count())
#select * from data where id <1000 and  age >30
print(df[(df['id'] < 1000) & (df['age'] > 30)])
#select id, count(distinct orderid) from data group by id
print(df.groupby('id')['orderid'].count())
#select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
print(pd.merge(df, df2, on='id'))
#select * from t1 union select * from t2
print(pd.concat([df, df2]))
# delete from t1where id=10
print(df.loc[df['id'] == 50])
#alter table t1 drop column name
print(df.drop(columns='account'))
