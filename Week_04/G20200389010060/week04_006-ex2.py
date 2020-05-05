# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 下午12:13
# @Author  : Mat
# @Email   : ZHOUZHENZHU406@pingan.com.cn
# @File    : week04_0060-ex2.py

import pandas as pd
import numpy as np


# 定义测试数据
group = [10, 20, 30,40]
data = pd.DataFrame({
    "id": [group[x] for x in np.random.randint(0,len(group),15)],
    "age": np.random.randint(15,50,15),
    "orderid": np.random.randint(15,50,15)
    })
print(data)


#select * from data
ret = data[:][:]
print('\n-------------------------------')
print('select * from data')
print(ret)
print('-------------------------------\n')


#select * from data limit(10)
ret = data.head(10)
print('\n-------------------------------')
print('select * from data limit(10)')
print(ret)
print('-------------------------------\n')


#select id  from data  //id 是 data 表的特定一列
ret = data[['id']]
print('\n-------------------------------')
print('select id  from data')
print(ret)
print('-------------------------------\n')


#select count(id) from data
ret = len(data['id'])
print('\n-------------------------------')
print('select count(id) from data')
print(ret)
print('-------------------------------\n')


#select * from data where id <1000 and  age >30
ret = data[(data.id < 1000) & (data.age > 30)]
print('\n-------------------------------')
print('select * from data where id <1000 and  age >30')
print(ret)
print('-------------------------------\n')



#select id , count(distinct orderid) from data group by id;
ret = data.groupby(['id'])['orderid'].nunique().reset_index(name='distinct_orderid_count')
print('\n-------------------------------')
print('select id , count(distinct orderid) from data group by id;')
print(ret)
print('-------------------------------\n')



# 定义测试数据
group = [10, 20, 30]
t1 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),15)],
    "name": [f'name{i}' for i in range(15)],
    "age":np.random.randint(15,50,15),
    "orderid":np.random.randint(15,50,15)
    })
# 定义测试数据
group = [10, 20, 30]
t2 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),15)],
    "name": [f'name{i}' for i in range(15)],
    "age":np.random.randint(15,50,15),
    "orderid":np.random.randint(15,50,15)
    })
#print(data)


print('t1:')
print(t1)

print('\nt2')
print(t2)


#select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
ret = pd.merge(t1, t2, on='id', how='inner')
print('\n-------------------------------')
print('select * from table1 t1 inner_join table2 t2 on t1.id = t2.id')
print(ret)
print('-------------------------------\n')


#select * from t1 union select * from t2
ret = pd.concat([t1, t2], axis=0).drop_duplicates().reset_index()
print('\n-------------------------------')
print('select * from t1 union select * from t2')
print(ret)
print('-------------------------------\n')



#delete from t1 where id=10
t1 = t1[t1.id != 10].reset_index(drop=True)
print('\n-------------------------------')
print('delete from t1 where id=10')
print(t1)
print('-------------------------------\n')


#alter table t1 drop column name
del t1['name']
print('\n-------------------------------')
print('alter table t1 drop column name')
print(t1)
print('-------------------------------\n')
