#!/usr/bin/env python
"""
作业二：

请将以下的 SQL 语句翻译成 Pandas 语句。

select * from data
select * from data limit(10)
select id from data  //id 是 data 表的特定一列
select count(id) from data
select * from data where id <1000 and  age >30
select id , count(distinct orderid) from data group by id;
select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
select * from t1 union select * from t2
delete from t1where id=10
alter table t1 drop column name
"""

import pandas as pd
import numpy as np


order_df = pd.DataFrame({
    'id': range(0, 20),
    "uid": np.random.randint(1000, 10015, 20),
    "orderid": np.random.randint(20200000, 20200100, 20),
    "amount": np.random.randint(50,65,20)
    })

order2_df = pd.DataFrame({
    'id': range(0, 20),
    "uid": np.random.randint(1000, 10015, 20),
    "orderid": np.random.randint(20200000, 20200100, 20),
    "amount": np.random.randint(50,65,20)
    })

user_df = pd.DataFrame({
    'id': range(0, 20),
    "uid": np.random.randint(1000, 10015, 20),
    "username": np.random.randint(20200000, 20200100, 20),
    "age": np.random.randint(18,65,20)
    })

# select * from data
order_df

# select * from data limit(10)
order_df.head(10)
order_df[0:10]

# select id from data  //id 是 data 表的特定一列
order_df['id']

# select count(id) from data
order_df['id'].count()

# select * from data where id <1000 and  age >30
# user_df[(order_df['id'].astype('int')<1000) & (order_df['age']>30)]
user_df[(user_df['id'].astype('int')<1000) & (user_df['age']>30)]

# select id, count(distinct orderid) from data group by id;
order_df.groupby('id')['orderid'].nunique()

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(order_df, user_df, on='id', how='inner')

# select * from t1 union select * from t2
# pd.concat([order_df, order2_df])
pd.concat([order_df, order2_df]).drop_duplicates()

# delete from t1 where id=10
order_df[order_df['id'] != 10]

# alter table t1 drop column name
order_df.drop(['amount'], axis=1)
