import pandas as pd
import numpy as np

data=[{"id":x,"age":np.random.randint(18,45)} for x in range(1,2000)]
#select * from data
df=pd.DataFrame(data)
print(df)
#select * from data limit(10)
print(df.head(10))
#select id  from data
print(df["id"])
#select count(id) from data
print(df["id"].count())
#select * from data where id <1000 and  age >30
print(df[ ( df['id']<1000 ) & ( df['age']>30 )])
#select id , count(distinct orderid) from data group by id
data=[{"id":x,"orderid":np.random.randint(18,23)} for x in range(1,10)]
df=pd.DataFrame(data)
print(df.drop_duplicates(['orderid']).groupby('id').aggregate( {'id':(lambda n:n) , 'orderid':'count' }))


table1=pd.DataFrame([{"id":x,"age":np.random.randint(18,45)} for x in range(1,5)])
table2=pd.DataFrame([{"id":x,"age":np.random.randint(18,45)} for x in range(1,4)])
#select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
print(pd.merge(table1, table2, on= 'id', how='inner'))
#select * from t1 union select * from t2
print(pd.concat([table1, table2]))
#delete from t1 where id=10
print(table1[ table1['id']==10 ])
#alter table t1 drop column name
print(table1.drop(['id'] ,axis = 1))
