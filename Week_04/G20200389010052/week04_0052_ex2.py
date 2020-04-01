import pandas as pd
import numpy as np

df1 = pd.DataFrame([
                    [1, '小蓝', 28, 'F'],
                    [2, '小红', 12, 'M'],
                    [3, '小绿', 20, 'M'],
                    [10, '小紫', 35, 'M']
                    ])
df1.columns = ['id','name','age','sex']

df2 = pd.DataFrame([
                    [1, 'xxx'],
                    [2, 'yyy'],
                    [3, 'zzz']
                    ])
df2.columns = ['id', 'addr']

df3 = pd.DataFrame([
                    [5, '小黑', 100, 'F'],
                    [6, '小白', 100, 'M'],
                    ])
df3.columns = ['id','name','age','sex']

try:
    # select * from data
    print(df1)
    # select * from data limit(10)
    print(df1[0:10])
    # select id  from data  //id 是 data 表的特定一列
    print(df1['id'])
    # select count(id) from data
    print(df1['id'].count())
    # select * from data where id <1000 and  age >30
    print(df1[ (df1['id']<1000) & (df1['age']>30) ])
    # select id , count(distinct orderid) from data group by id;
    print(df1.drop_duplicates(subset='sex').sort_values('id'))
    # select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
    print(pd.merge(df1, df2, on ='id', how='inner'))
    # select * from t1 union select * from t2
    print(pd.concat([df1, df3]))
    # delete from t1where id=10
    print(df1[df1['id']!=10])
    # alter table t1 drop column name
    print(df1.drop(columns=['sex']))
except Exception as e:
    print(e)