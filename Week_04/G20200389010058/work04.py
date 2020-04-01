import pandas as pd

data = [
    # id name age
    [1, 'ABC', 12],
    [2, 'ABC', 23],
    [3, 'ABC', 14],
    [4, 'ABC', 43],
    [5, 'ABC', 17],
    [6, 'ABC', 31],
    [7, 'ABC', 56],
    [8, 'ABC', 12],
    [9, 'ABC', 45],
    [10, 'ABC', 9],
    [11, 'ABC', 75],
]
# select * from data
df = pd.DataFrame(data)
df.columns = ['id', 'name', 'age']

# select * from data limit(10)

limit_10 = df.head(10)
print(limit_10)
print('*' * 30)

# select id  from data
field = df['id']
print(field)
print('*' * 30)

# select count(id) from data
count = df['id'].count()
print(count)
print('*' * 30)

# select * from data where id <1000 and  age >30
# where_data = df[(df['id'] < 10) & (df['age'] > 28)]
where_data = df[(df['id'] < 8) & (df['age'] > 28)]
print(where_data)

# select id , count(distinct orderid) from data group by id
df.groupby('id')['orderid'].count()

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
df.merge(t1, t2, on='id')

# select * from t1 union select * from t2
df.contact([t1, t2])

# delete from t1 where id=10
df.drop(df['id'] == 10)

# alter table t1 drop column name
df.drop(['name'], axis=1)
