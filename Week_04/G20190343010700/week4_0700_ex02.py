'''
select * from data
select * from data limit(10)
select id  from data  //id 是 data 表的特定一列
select count(id) from data
select * from data where id <1000 and  age >30
select id , count(distinct orderid) from data group by id;##  这句话没看懂 去重吗？
select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
select * from t1 union select * from t2
delete from t1 where id=10
alter table t1 drop column name
'''

import pandas as pd

###  ============  select * from data    ============
df = pd.read_csv('mydata.csv',sep = '', encoding='uft-8')

###  ============  select * from data limit(10)  ============
df_10 = df[:10,]
#### ------- 直接读取  ------------
df_10 =pd.read_csv('mydata.csv',sep = '',nrow=10,encoding='uft-8')

###   ============  select id  from data  //id 是 data 表的特定一列   ============
id = df['id']

###   ============  select count(id) from data    ============
count_id = df['id'].count()

###   ============  select * from data where id <1000 and  age >30    ============
df_2 = df[(df['id']<1000 ) & (df['age']>30)]

###   ============   select id , count(distinct orderid) from data group by id   ============
df['id'].goupby('id').drop_duplicates().count()  ## 这个没啥把握

###    ============  select * from table1 t1 inner_join table2 t2 on t1.id = t2.id  ============
pd.merge(table1,table2,left_on='t1.id', right_in = 't2.id', how = 'inner')

###   ============   select * from t1 union select * from t2   ============
pd.merge(t1,t2, how = 'outer')

###   ============   delete from t1 where id=10   ============
df.drop(t1['id']==10, axis = 0 )

####   ============  alter table t1 drop column name   ============  
df = pd.read_csv('mydata.csv',sep = '', header = false, encoding='uft-8')
t1.drop('name',axis=1)