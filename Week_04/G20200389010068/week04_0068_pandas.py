import pandas as pd
import numpy as np
# week 04
# pandas

group = [10, 20, 30]
data = pd.DataFrame({
    "id": [group[x] for x in np.random.randint(0,len(group),15)],
    "age": np.random.randint(15,50,15),
    "orderid": np.random.randint(15,50,15)
    })
# select * from data
# res = data[:][:]
print('select * from data')
print (data)


# select * from data limit(10)
print('select * from data limit(10)')
print(data.head(10))

# data[1:10]

# select id  from data
print('select id  from data  ')
print(data['id'])

# select count(id) from data
data['id'].count()
# select * from data where id <1000 and  age >30
data[(data['id']<1000) & (data['age']>30)]
# select id , count(distinct orderid) from data group by id;
data.groupby('id').aggregate({'id':'count'})

group = [10, 20, 30]
t1 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),15)],
    "name": [f'name{i}' for i in range(15)],
    "age":np.random.randint(15,50,15),
    "orderid":np.random.randint(15,50,15)
    })
# 定义数据
group = [10, 20, 30]
t2 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),15)],
    "name": [f'name{i}' for i in range(15)],
    "age":np.random.randint(15,50,15),
    "orderid":np.random.randint(15,50,15)
    })


# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(t1, t2, on='id', how='inner')
# select * from t1 union select * from t2
pd.concat([t1,t2])
# delete from t1 where id=10
t1 = t1[t1.id != 10].reset_index(drop=True)
# alter table t1 drop column name
del t1['name']