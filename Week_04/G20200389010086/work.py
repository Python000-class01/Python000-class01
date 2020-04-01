import pandas as pd
import numpy as np

# select * from data
df_1 = pd.read_excel(f'1.xlsx')
df_2 = pd.read_excel(f'2.xlsx')


# select * from data limit(10)
df_1.head(10)

# select id  from data  //id 是 data 表的特定一列
df_1['id']

# select count(id) from data
df_1.id.count()

# select * from data where id <1000 and  age >30
df_1[df_1['id'] < 1000 & df_1['age'] > 30]

# select id , count(distinct order id) from data group by id;
df_1.groupby('id')['orderid'].count()

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
result = pd.merge(df_1, df_2, how='inner', on=['id'])

# select * from t1 union select * from t2
pd.concat([df_1, df_2])

# delete from t1 where id=10
df_1.drop([df_1['id'] == 10])

# alter table t1 drop column name
df_1.drop(['name'], axis=1)
