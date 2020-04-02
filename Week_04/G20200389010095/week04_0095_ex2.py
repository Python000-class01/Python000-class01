#!/anaconda3/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   week04_0095_ex2.py    
@Contact :   leixuewen14@126.com
@License :   (C)Copyright 2019-2020, Leith14-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/1 8:05 下午   Leith14      1.0         None
'''

import pandas as pd

datas = pd.read_excel(r'data.xls', sheet_name=0)

# select * from data
print(datas)

# select * from data limit(10)
print(datas[1:10])

# select id from data
print(datas['id'])

# select count(id) from data
print(datas['id'].count())

# select * from data where id < 1000 and  age >30
print(datas[(datas['id'] < 1000) & (datas['age'] > 30)])

# select id , count(distinct orderid) from data group by id;
print(datas.groupby('id').agg({'orderid': pd.Series.nunique}))

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(t1, t2, left_on='id', right_on='id')

# select * from t1 union select * from t2
pd.merge(t1, t2)

# delete from t1 where id=10
print(datas.drop(datas[datas['id'] == 10], axis=0))

# alter table t1 drop column name
print(datas.drop('name', 1))