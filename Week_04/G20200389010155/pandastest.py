"""
select * from data   #从”data“表中选取所有的列
select * from data limit(10) #从”data“表中取出前10行记录
select id  from data  //id 是 data 表的特定一列，取出”data“表中的id列。
select count(id) from data   #返回指定id列的值的数目(NULL不计入)
select * from data where id <1000 and  age >30   #返回”data“表中 id小于1000，age>30的行。
select id , count(distinct orderid) from data group by id  #从”data“表中选取id列，去除orderid的重复值。
select * from table1 t1 inner_join table2 t2 on t1.id = t2.id  #取出table1和table2中id列相同的行
select * from t1 union select * from t2  #将t1和t2表中所有行（非重复）进行合并
delete from t1where id=10    #删除t1表中id值为10的行
alter table t1 drop column name #删除t1表中name 列。
"""
import pandas as pd
import numpy as np

# 聚合
"""      
data表
      id  age  orderid
0      1   20        1
1     20   16        1
2     30   35        2
3    100   40        5
4    250   32        3
5    500   29        6
6    900   50        6
7   1000   69        7
8   1500   78        8
9   1551   90        9
10  1552   66        4
11  1889   55       10
t1表
    id  age  orderid
0   10   20        1
1   20   16        1
2   30   35        2
3  100   40        5
4  250   32        3
5  500   29        6
t2表
     id  age  orderid
0    10   18        1
1    20   16        1
2  1000   69        7
3   100   66        5
4  1551   90        9
5   500   29        6
6  1889   55       10
"""
df = pd.read_csv('data.csv')
print(df)          #从”data“表中选取所有的列
print(df[0:11])    #从”data“表中取出前10行记录
print(df['id'])    #id 是 data 表的特定一列，取出”data“表中的id列。

df2=pd.DataFrame(df,columns=['id','age','orderid'])

print(df2.groupby('id').count())                #返回指定id列的值的数目(NULL不计入)

print(df2[(df2['id']<1000)& (df2['age']>30)])  #返回”data“表中 id小于1000，age>30的行。

df3=df2.drop_duplicates(subset=['orderid'])
print(df3['id'])                               #去除orderid的重复值，从”data“表中选取id列，

t1=pd.read_csv('t1.csv')
t2=pd.read_csv('t2.csv')
print(t1)
print(t2)
tmix=pd.merge(t1,t2)
print(tmix)
Datat1=pd.DataFrame(t1)
Datat2=pd.DataFrame(t2)
Datamix1=pd.merge(Datat1,Datat2,on='id')
print(Datamix1)                          #select * from table1 t1 inner_join table2 t2 on t1.id = t2.id  #取出table1和table2中id列相同的行
Datamix2=pd.merge(Datat1,Datat2,how='outer')
print(Datamix2)                          #select * from t1 union select * from t2  将t1和t2表中所有行（非重复）进行合并将t1和t2表中所有行（非重复）进行合并
print(Datat1[~Datat1['id'].isin([10])])  #delete from t1where id=10    #删除t1表中id值为10
print(Datat1.drop('orderid',axis=1))    #alter table t1 drop column name #删除t1表中name 列。这里我替换为删除t1表中orderid列


