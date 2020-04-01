select * from data
select * from data limit(10)
select id  from data  //id 是 data 表的特定一列
select count(id) from data
select * from data where id <1000 and  age >30
select id , count(distinct orderid) from data group by id;
select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
select * from t1 union select * from t2
delete from t1where id=10
alter table t1 drop column name
"""
import pandas as pd

df = pd.read_csv('data.csv')
df2 = pd.read_csv('data2.csv')
df.columns = ['age', 'orderid', 'C', 'id', 'name', 'F' ]
df2.columns = ['age', 'orderid', 'C', 'id', 'name', 'F' ]

# select * from data
print('选择data表中所有数据')
print(df)
print()

# select * from data limit(10)
# 选择data表前10行数据
print('选择data表前10行数据')
print(df[0:10])
print()

# select id  from data  //id 是 data 表的特定一列
print('选择data表id一列')
print(df['id'])
print()

# select count(id) from data
print('选择data表id一列的个数')
print(df['id'].count())
print()

# select * from data where id <1000 and  age >30
print('选择data表中id列值小于1000和age列')
print(df[(df['id'] < 1000) & (df['age'] > 100)])
print()

# select id , count(distinct orderid) from data group by id;
print('选择data表中id列和orderid的count值（需去重）')
print(df[['id', 'orderid']].groupby('id').aggregate({'orderid': pd.Series.nunique}))
print()


# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
print('选择data、data2表中id列相同的行')
print(pd.merge(df, df2, on = 'id', how = 'inner'))
print()

# select * from t1 union select * from t2
print('上下拼接data、data2表中所有元素，并且值不重复')
print(pd.concat([df, df2]).drop_duplicates())
print()

# delete from t1 where id=10
print('删除data表中id=10的行')
print(df.drop(index=df[df.id==10].index))
print()

# alter table t1 drop column name
print('删除data表中的name列')
print(df.drop(columns='name', axis=1))
print()