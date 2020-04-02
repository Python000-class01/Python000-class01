import pandas as pd
import numpy as np
import seaborn as sns

data=[['male',170],['female',165]]
columns = ['sex','height']
t2 = pd.DataFrame(data=data,columns=columns)

df = sns.load_dataset('titanic')

# select * from data
r1 = df

# select * from data limit(10)
r2 = df.loc[:10]

# select id  from data  //id 是 data 表的特定一列
r3 = df['embark_town']

# select count(id) from data
r4 = len(df)

# select * from data where id <1000 and  age >30 
r5 = df[(df['age']>60) & (df['sex']=='male')]

# select id , count(distinct orderid) from data group by id;
r6 = df.groupby('sex').agg({'embark_town': pd.Series.nunique}).index

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
r7 = pd.merge(df,t2,on='sex')

# select * from t1 union select * from t2
t3 = df.loc[:100]
t4 = df.loc[100:200]
r8 = pd.concat([t3,t4])

# delete from t1 where id=10
r9 =df.drop(df[(df['age']>30)].index)

# alter table t1 drop column name
r10 = df.drop('parch',axis = 1)

print(r10)