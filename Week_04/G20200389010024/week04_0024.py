import pandas as pd
data = pd.read_csv



select * from data
data['*']

select * from data limit(10)
data [1:10,'*']

select id  from data  //id 是 data 表的特定一列
data_loc['id']

select count(id) from data
data.groupby('id'.sum())

select * from data where id <1000 and  age >30 
D1 = data[data['id'<1000]]
D2 = D1[D1['age'>30]]
D2['*']


select id , count(distinct orderid) from data group by id;


select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
t3 = pd.merge(t1['*'],t2['*'],on ='id')


select * from t1 union select * from t2
t3 = pd.merge(t1['*'],t2['*'])


delete from t1 where id=10
t1.drop(['id',values = 10])


alter table t1 drop column name
t1.drop('column name',axis=1)