import pandas as pd
import pymysql

'''
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
'''

conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", charset="utf8", db="test")

# select * from data
sql = 'SELECT * FROM  data'
df = pd.read_sql(sql, conn)

# select * from data limit(10)
head10 = df.head(2)
# print(head10)

# select id  from data
df_id = df[['id']]
# print(df_id)

# select count(id) from data
# print(df[['id']].count())

# select * from data where id <1000 and  age >30
df1 = df[(df['id'] < 1000) & (df['age'] > 30)]
# print(df1)

# # select id , count(distinct orderid) from data group by id;
# df2 = df.groupby('id').agg({'id':'min','orderid':'count'})
df2 = df.groupby('id').agg({'orderid':'count'}).drop_duplicates()
print(df2)
#
# # select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
# table1 = pd.read_sql('SELECT * FROM  table1', conn)
# table2 = pd.read_sql('SELECT * FROM  table2', conn)
# df3 = pd.merge(table1, table2, on='id', how='inner')
# print(df3)
#
# # select * from t1 union select * from t2
# t1 = pd.read_sql('SELECT * FROM  t1', conn)
# t2 = pd.read_sql('SELECT * FROM  t3', conn)
# df4 = pd.concat([t1, t2])
# print(df4)

# # delete from t1 where id=10
# df_t11 = pd.read_sql('SELECT * FROM  t1', conn)
# df5 = df_t11 [  df_t11['id'] != 10 ]
# print(df5)
#
#
# # alter table t1 drop column name
# df_t111 = pd.read_sql('SELECT * FROM  data where 1 <> 1', conn)
# df_t111_1 = df_t111.drop( labels='id', axis=1)
# print(df_t111_1)
