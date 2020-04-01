import pandas as pd
import pymysql

# select * from data 
sql  =  'SELECT *  FROM mytable'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df = pd.read_sql(sql,conn)
     
# select * from data limit(10)
df.head(10)

# select id  from data  //id 是 data 表的特定一列
df['id']

# select count(id) from data
df.shape[0]

# select * from data where id <1000 and  age >30 
df[ ( df['id']<1000 ) & ( df['age']>30 )   ]

# select id , count(distinct orderid) from data group by id;
df.drop_duplicates(['id','orderid'])
df.groupby('id').aggregate( {'id':'count' , 'orderid':'unique' })

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(table1, table2, on= 'id', how='inner')

# select * from t1 union select * from t2
pd.concat([t1, t2])

# delete from t1 where id=10
df[(df['id']!=10)]

#alter table t1 drop column name
df.drop(['name'], axis = 1)