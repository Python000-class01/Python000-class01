import pandas as pd
import numpy as np

data = pd.DataFrame({'id': np.random.randint(15, 50, 20),
                            'B': pd.Timestamp('20130102'),
                            'C': pd.Series(1, index=list(range(20)), dtype='float32'),
                            'orderid': np.random.randint(1, 1000, 20),
                            'F': 'foo'})
# select * from data
data

# select * from data limit(3)
data.head(10)

# select id  from data  //id 是 data 表的特定一列
data[['id']]

# select count(id) from data
data['id'].count()

# select * from data where id <1000 and  age >30
data[(data.id < 1000) & (data.age > 30)]

# select id , count(distinct orderid) from data group by id;
ret = data.groupby(['id'])['orderid'].nunique()


group = [10, 20, 30]
t1 = pd.DataFrame({
    "id": [group[x] for x in np.random.randint(0, len(group), 20)],
    "name": [f'name{i}' for i in range(20)],
    "age": np.random.randint(15, 50, 20),
    "orderid": np.random.randint(15, 50, 20)
})

group = [10, 20, 30]
t2 = pd.DataFrame({
    "id": [group[x] for x in np.random.randint(0, len(group), 20)],
    "name": [f'name{i}' for i in range(20)],
    "age": np.random.randint(15, 50, 20),
    "orderid": np.random.randint(15, 50, 20)
})

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(t1, t2, on='id', how='inner')

# select * from t1 union select * from t2
pd.concat([t1, t2], axis=0)

# delete from t1 where id=10
t1[t1['id'] != 10]

# alter table t1 drop column name
t1.drop(t1.columns['name'], axis=1)




