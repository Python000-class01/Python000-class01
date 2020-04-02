'''
第一题因为不会使用Linux，且时间原因没有做

'''

#取前10行
data.head(10) 

# 取ID这一列
data[['id']]  

#统计ID列非空个数
data.id.count() 

# 显示 id <1000 同时 age > 30 的行
data[(data['id'] < 1000) & (data['age'] > 30)]

# 按ID分组，统计 orderid 不重复的个数
data.groupby('id')['orderid'].nunique()

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
output = pd.merge(t1, t2, on='id')

# select * from t1 union select * from t2
output = pd.concat([t1, t2])

# delete from t1 where id=10
t1[t1['id'] != 10]

# alter t1 drop column name
t1.drop(columns=['name'])