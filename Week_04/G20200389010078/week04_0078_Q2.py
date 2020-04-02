# select * from data
# select * from data limit(10)
# select id  from data  //id 是 data 表的特定一列
# select count(id) from data
# select * from data where id <1000 and  age >30
# select id , count(distinct orderid) from data group by id;
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
# select * from t1 union select * from t2
# delete from t1where id=10
# alter table t1 drop column name

import pandas as pd

df = pd.DataFrame(data)

result1 = df
result2 = df.head(10)
result3 = df[['id']]
result4 = df.groupby('id').aggregate({'id': 'count'})
result5 = df[(df['id'] < 1000) & (df['age'] > 30)]
result6 = df.groupby('id').aggregate({'distinct orderid': 'count'})
result7 = pd.merge(pd.DataFrame(t1), pd.DataFrame(t2), on='id', 'how'='inner')
result8 = pd.merge(pd.DataFrame(t1), pd.DataFrame(t2), 'how'='outer')
result9 = pd.DataFrame(t1)[df['id']!=10]
result10 = [''] * len(pd.DataFrame(t1).columns)

