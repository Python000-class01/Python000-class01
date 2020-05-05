# 作业二：
# 请将以下的 SQL 语句翻译成 Pandas 语句。
# select * from data
data

# select * from data limit(10)
data.head(10)

# select id  from data  //id 是 data 表的特定一列
data['id']

# select count(id) from data
data['id'].count()

# select * from data where id <1000 and  age >30 
data[ (data['id']<1000) & (data['age']>30) ]

# select id , count(distinct orderid) from data group by id;
data.groupby('id').orderid.nunique()


# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(table1, table2, on = 'id', how='inner')

# select * from t1 union select * from t2
data = pd.concat[(t1, t2])
data.drop_duplicates()

# delete from t1where id=10
t1.drop( t1[t1.id == 10 ].index)

# alter table t1 drop column name
t1.drop( ['name'] , axis=1 )