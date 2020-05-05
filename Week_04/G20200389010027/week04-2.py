import pandas as pd
df1 = pd.read_csv('movie.douban.com_top250.csv')

#select * from data
print(df1)
#select * from data limit(10)
print(df1[:10])

#select id  from data  //id 是 data 表的特定一列
print(df1['subject_id'])

#select count(id) from data
print(df1['subject_id'].count())

#select * from data where id <1000 and  age >30 
print( df1[ (df1['subject_id'] < 2000000) & (df1['rating_num'] >9) ])


#select id , count(distinct orderid) from data group by id;
df2 = pd.read_csv('movie.douban.com_top250_comment.csv')
print(df2.groupby('subject_id').vote.nunique())

#select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
print(df1.merge(df2, left_on='subject_id', right_on='subject_id'))

#select * from t1 union select * from t2
print(pd.concat([df1, df2]))

#delete from t1where id=10
indexes = df1[df1['subject_id'] == 1292052].index
print(indexes)
df1.drop(indexes, inplace=True)
print(df1)

#alter table t1 drop column name
df1.drop('comment_cnt', axis = 1, inplace=True)
print(df1)