import pandas as pd
import numpy as np

df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
print(df1)

df2 = pd.read_excel(r'0321.xlsx')
df2.head(10)

df2['id']

df2.groupby('id').count()

df2[( df2['id'] < 1000) & (df2['age'] < 30)]

group = ['x','y','z']
table1 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

table2 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    })

pd.merge(table1, table2, on='id', how='inner')

pd.concat([table1, table2])

df1[df1['id'] != 10]

df1.drop(df1.columns['name'],axis=1)