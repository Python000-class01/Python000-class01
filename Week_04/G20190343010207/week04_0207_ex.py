# Python进阶训练营-Week04-Homework02
# Learn Pandas

#1. select * from data
data
# 2. select * from datax limit(10)
data.head(10)
# 3. select id  from data  //id 是 data 表的特定一列
data[['id']]
# 4. select count(id) from data
data[['id']].count()
len(data[['id']])
# 5. select * from data where id <1000 and  age >30
data[(data['id'] < 1000) and (data['age'] > 30)]
# 6. select id , count(distinct orderid) from data group by id;
data.groupby('id').count()
# 7. select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(t1, t2, on='id')
# 8. select * from t1 union select * from t2
pd.concat(t1, t2)
# 9. delete from t1 where id=10
tmp = t1.drop([10], axis=0)  #删除行，默认axis=0
# 10. alter table t1 drop column name
tmp = t1.drop(['column name'], axis=1)  #删除列，必须制定 axis=1
