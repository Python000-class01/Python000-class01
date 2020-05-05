import pandas as pd
import numpy as np


data1 = pd.DataFrame({
    "id":range(10) ,
    "age":np.random.randint(15,50,10),
    "orderid": np.random.randint(100,120,10)
    })

data2 = pd.DataFrame({
    "id":range(5,15) ,
    "age":np.random.randint(15,50,10),
    "orderid": np.random.randint(100,120,10)
    })

#根据以上命名的初始值，更改以下的data或t1
# 1. select * from data
data

# 2. select * from data limit(10)
data[:10]
data.shape(10)

# 3. select id  from data  //id 是 data 表的特定一列
data['id']

# 4. select count(id) from data
data['id'].count()

# 5.select * from data where id <1000 and  age >30
data1[(data1['id'] <1000) & (data1['age'] > 30)]

# 6. select id , count(distinct orderid) from data group by id;
data1.drop_duplicates('orderid').groupby('age').aggregate({'orderid': 'count'})


# 7. select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(t1, t2, on='id')

# 8. select * from t1 union select * from t2
pd.merge(t1, t2, how=outer)

# 9. delete from t1 where id=10
t1.drop(t1[t1['id'] ==10].index, inplace=True)

# 10. alter table t1 drop column name
t1.drop('name', axis=1, inplace=True)

