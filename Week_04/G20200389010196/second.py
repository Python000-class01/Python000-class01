import pandas as pd

# select * from data
# df = pd.read_csv('./data.csv', encoding='utf-8')
# # 输出全部内容
print(df)

# select * from data limit(10)
df = pd.read_csv('./data.csv', encoding='utf-8')
print(df.head(10))

# select id from data  //id 是 data 表的特定一列
df = pd.read_csv('./data.csv', encoding='utf-8')
print(df[['id']])

# # select count(id) from data
df = pd.read_csv('./data.csv', encoding='utf-8')
print(df[['id']].count())

# select * from data where id <1000 and  age >30 
df = pd.read_csv('./data.csv', encoding='utf-8')
print(df[(df['id'] < 1000) & (df['age'] > 30)])

# select id , count(distinct orderid) from data group by id;
df = pd.read_csv('./data.csv', encoding='utf-8')
print(df.groupby(['id']).agg({'orderid': pd.Series.nunique}))

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
df1 = pd.read_csv('./data.csv', encoding='utf-8')
df2 = pd.read_csv('./data2.csv', encoding='utf-8')
print(pd.merge(df1, df2, on='id'))

# select * from t1 union select * from t2
df1 = pd.read_csv('./data.csv', encoding='utf-8')
df2 = pd.read_csv('./data2.csv', encoding='utf-8')
print(pd.concat([df1, df2]).drop_duplicates())

# delete from t1 where id=10
df = pd.read_csv('./data.csv', encoding='utf-8')
print(df[df['id'] != 10])
print(df.loc[df['id'] != 10])

# alter table t1 drop column name
df = pd.read_csv('./data.csv', encoding='utf-8')
print(df.drop(['name'], axis=1))