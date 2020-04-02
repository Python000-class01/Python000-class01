# 请将以下的 SQL 语句翻译成 Pandas 语句。
import pymysql
import pandas as pd
sql  =  'SELECT *  FROM data'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df = pd.read_sql(sql,conn)
conn.close()

# select * from data  查询出date表中所有数据
df

# select * from data limit(10)  查询date表中前10条数据
df.head(10)

# select id  from data  //id 是 data 表的特定一列  查询data表中的id列
df['id']

# select count(id) from data   查询data表中id的行数
df['id'].count()

# select * from data where id <1000 and  age >30  查询data表中id<1000同时age>30的数据
df[ ( df['id']<1000 ) & ( df['age']>30 )   ]

# select id , count(distinct orderid) from data group by id;  从表data中查询id，orderid不重复数量，并用id列排序
df.dorp_duplicates(subset = 'orderid')

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id  通过id内连接t1和t2（横向合并）
sql_t1  =  'SELECT *  FROM t1'
conn_t1 = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df_t1 = pd.read_sql(sql_t1,conn_t1)
conn_t1.close()

sql_t2  =  'SELECT *  FROM t2'
conn_t2 = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df_t2 = pd.read_sql(sql_t2,conn_t2)
conn_t2.close()

pd.merge(df_t1, df_t2, on = 'id', how = 'inner')

# select * from t1 union select * from t2  合并t1和t2，并去除重复的数据 （纵向合并）
pd.concat([df_t1, df_t2], ignore_index = True).drop_duplicates()

# delete from t1 where id=10  删除t1表中id=10的数据
df [  df['id'] != 10 ]

# alter table t1 drop column name  在t1表中删除name列
df.drop(columns = ['name'])



