import pandas as import pd

df = pd.DataFrame({"id": [None, 3, 1, 4],
                    "name": [None, 2, 4, 3],
                    "age": [4, 3, None, 31],
                    "height": [5, 4, 2, None]})
df1 = pd.DataFrame({"id": ['10', 3, 1, 4],
                    "name": [None, 2, 4, 3],
                    "age": [4, 3, 8, 31],
                    "orderid": [5, 5, 2, None]})

# select * from data
print(df1)
print(df1.loc[:])
# select * from data limit(10)
print(df1.head(10))
# select id  from data  //id 是 data 表的特定一列
print(df1['id'])
# select count(id) from data
print(df1['id'].count())
# select * from data where id <1000 and  age >30
print(df1[(df1['id']<1000) & (df1['age']>30)])
# select id , count(distinct orderid) from data group by id;
count = df1.groupby('id').agg({'orderid': pd.Series.nunique})
print(count)
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
print(pd.merge(df, df1, on='id'))
# select * from t1 union select * from t2
print(pd.merge(df, df1))
# delete from t1 where id=10
# print(df1[df1['id'] == 10]).dropna(axis=0)
df1 = df1.astype(str)
print(df1[~df1['id'].str.contains('10')])
# alter table t1 drop column name
print(df1.drop(['age'], axis=1))
