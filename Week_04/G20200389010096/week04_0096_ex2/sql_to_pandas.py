import pandas as pd
import numpy as np

def print_header(statement):
    print(f'\n#### {statement}')

group=[300, 600, 900, 1200, 1500]
data=pd.DataFrame({
    "id": [group[x] for x in np.random.randint(0, len(group), 16)],
    "age": np.random.randint(20, 60, 16),
    "orderid": np.random.randint(1000, 2000, 16)
    })

print_header(f'select * from data')
print(data.loc[:,])

print_header(f'select * from data limit(10)')
print(data.head(10))

print_header(f'select id from data')
print(data[['id']])

print_header(f'select count(id) from data')
print(data['id'].count())

print_header(f'select * from data where id <1000 and age >30')
print(data[(data['id'] < 1000) & (data['age'] > 30)])

print_header(f'select id, count(distinct orderid) from data group by id')
print(data.groupby(['id'])['orderid'].nunique().reset_index(name='distinct_orderid_count'))

group=[10, 20, 30, 40, 50]
t1=pd.DataFrame({
  "id": [group[x] for x in np.random.randint(0, len(group), 10)],
  "name": [f'n{i}' for i in range(10)],
  "age": np.random.randint(20, 60, 10),
  "orderid": np.random.randint(1000, 2000, 10)
  })
t2=pd.DataFrame({
  "id": [group[x] for x in np.random.randint(0, len(group), 10)],
  "name": [f'n{i}' for i in range(10)],
  "age": np.random.randint(20, 60, 10),
  "orderid": np.random.randint(1000, 2000, 10)
  })

print_header(f't1')
print(t1.loc[:,])

print_header(f't2')
print(t2.loc[:,])

print_header(f'select * from table1 t1 inner_join table2 t2 on t1.id = t2.id')
print(pd.merge(t1, t2, on='id', how='inner'))

print_header(f'select * from t1 union select * from t2')
print(pd.concat([t1, t2]).drop_duplicates())

print_header(f'delete from t1 where id=10')
t1 = t1[t1['id'] != 10].reset_index(drop=True)
print(t1)

print_header(f'alter table t1 drop column name')
t1.drop(['name'], axis=1, inplace=True)
print(t1)