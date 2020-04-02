import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import random
import pymssql
from sqlalchemy import create_engine
connect = pymssql.connect('localhost','root','passwd','database', charset='utf8', use_unicode=True)
# sql_serach="select * from Table"
# select * from data
DataFrame = pd.read_sql('select * from Table',connect)
# select * from data limit(10)
df_limit10 = DataFrame[['columns1','columns10']]
# select id  from data  //id 是 data 表的特定一列
df_id = DataFrame['id']
# select count(id) from data
df_count(id) = len(DataFrame.index)-len(DataFrame.loc[DataFrame['id']=='NaN'])
# select * from data where id <1000 and  age >30 
df_double_request = DataFrame[(DataFrame['age']>30) & (DataFrame['id']<1000)]
# select id , count(distinct orderid) from data group by id;
df_id2 = len(set(DataFrame['id'].values.tolist()))
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
df_double_table = pd.merge(DataFrame1,DataFrame2,on='id')
# select * from t1 union select * from t2
df_double_table2 = pd.merge(DataFrame1,DataFrame2,how='left')
# delete from t1where id=10
df_delete = DataFrame1.drop[(['id'],axis=0)]
# alter table t1 drop column name
df_drop = DataFrame1.drop(columns=['name'])