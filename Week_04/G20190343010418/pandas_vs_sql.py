import pandas as pd

df = pd.DataFrame(
    {
        'id': [1, 50, 101, 235, 2459],
        'age': [18, 21, 35, 43, 61],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female'],
        'name': ['张三', '李四', '东邪', '西毒', '王重阳']
    }
)

# select * from data limit(10)
print(df.head(10))

# select id  from data  //id 是 data 表的特定一列
print(df['id'])

# select count(id) from data
print(df.count()['id'])

# select * from data where id <1000 and  age >30
print(df[(df['id'] < 1000) & (df['age'] > 30)])

# select id , count(distinct orderid) from data group by id;
print(df.groupby('id').agg({'orderid': 'count'}))

t1 = pd.DataFrame(
    {
        'id': [1, 50, 101, 235, 2459],
        'age': [18, 21, 35, 43, 61],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female'],
        'name': ['张三', '李四', '东邪', '西毒', '王重阳']
    }
)

t2 = pd.DataFrame(
    {
        'id': [1, 50, 101, 235, 245],
        'country': ['中国', '美国', '英国', '法国', '德国']
    }
)

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
t3 = pd.merge(t1, t2, on='id', how='inner')

# select * from t1 union select * from t2
t4 = pd.DataFrame(
    {
        'id': [111, 222],
        'age': [28, 31],
        'sex': ['Female', 'Male'],
        'name': ['林朝英', '杨过']
    }
)
t5 = pd.concat([t1, t4])

# delete from t1 where id=10
t6 = t1[t1['id'] != 10]

# alter table t1 drop column name
t7 = t1.drop(['name'], axis=1)
