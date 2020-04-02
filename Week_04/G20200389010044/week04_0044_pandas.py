import pandas as pd

# 读取数据
df = pd.read_csv("DataFile_Path.csv")

# select * from data
print(df)

# select * from data limit(10)
print(df[:10])

# select id  from data  //id 是 data 表的特定一列
print(df['id'])

# select count(id) from data
print(df['id'].count())

# select * from data where id <1000 and  age >30 
print(df[ (df['id'] < 1000) & (df['age'] > 30) ]

# select id , count(distinct orderid) from data group by id;
df1 = df.groupby("id").orderid.nunique()
print(df1)

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
df = df1.merge(df2, how = "inner", on = "id")
print(df)

# select * from t1 union select * from t2
df = pd.concat([df1, df2])
print(df)

# delete from t1 where id=10
df1 = df.drop(df[ df['id'] == '10' ].index)
print(df1)

# alter table t1 drop column name
df.columns = [''] * len(df.columns)
print(df)

