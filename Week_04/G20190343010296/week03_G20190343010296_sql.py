import numpy as np
import pandas as pd

group = ['x','y','z']

data = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "id":np.random.randint(0,11,10),
    "age":np.random.randint(15,50,10),
    "salary":np.random.randint(5,50,10),
    })

data2 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "id":np.random.randint(0,10,10),
    "age":np.random.randint(15,50,10),
    "salary":np.random.randint(5,50,10),
    })
	
# select * from data
print(data.loc[:])

# select * from data limit(10)
print(data.head(10))

# select id  from data  //id 是 data 表的特定一列
print(data['id'])

# select count(id) from data
print(data['id'].count())

# select * from data where id <1000 and  age >30 
print(data[(data['id']<1000) & (data['age']>30)])

# select id , count(distinct orderid) from data group by id;
print(data.groupby('id').count()) 

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
print(pd.merge(data, data2, on='id', how='inner'))

# select * from t1 union select * from t2
print(pd.concat([data, data2]))

# delete from t1where id=10
indexNames = data[data['id']==10].index
data.drop(indexNames , inplace=True)
print(data)

# alter table t1 drop column name
data.drop(['id'], axis=1, inplace=True)
print(data)