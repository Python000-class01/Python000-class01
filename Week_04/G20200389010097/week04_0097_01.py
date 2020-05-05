import pandas as pd
df = pd.read_excel("xxx.xlsx")

# select * from data
print(df)
# select * from data limit(10)
print(df.head(10))
# select id  from data  //id 是 data 表的特定一列
print(df.loc[:,['id']])
# select count(id) from data
print(df['id'].count())
# select * from data where id <1000 and  age >30
print(df[(df['id'] < 1000) & (df['age'] > 30)])
# select id , count(distinct orderid) from data group by id;
df.groupby('id').count()
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
df.merge(df1,df2,on='id')
# select * from t1 union select * from t2
df.merge(df1,df2)
# delete from t1where id=10
df.drop(df[id]==10)
# alter table t1 drop column name
df.drop('name',axis=1)
