import pandas as pd
import pymysql

sql = 'select * from data'
conn = pymysql.connect('ip','name','pass','data','charset=utf8')
df = pd.read_sql(sql,conn)



select * from data
- df

select * from data limit(10)
- df.loc[0:9]

select id  from data  //id 是 data 表的特定一列
- df['id']

select count(id) from data
- df['id'].count()

select * from data where id <1000 and  age >30 
- df[ (df['id']<1000]) & (df['age']>30) ]

select id , count(distinct orderid) from data group by id;
- df[['id','orderid']].groupby('id').agg({'orderid':pd.Series.nunique})

select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
- pd.merge(df1, df2, on = 'id', how = 'inner')

select * from t1 union select * from t2
- pd.concat([df1, df2])

delete from t1 where id=10
- df1.drop(df1[df1.id=10].index)

alter table t1 drop column name
- df1.drop(df.columns['name'], axis = 1)