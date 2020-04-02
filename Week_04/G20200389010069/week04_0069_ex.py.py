# select * from data
# select * from data limit(10)
# select id  from data  //id 是 data 表的特定一列
# select count(id) from data
# select * from data where id <1000 and  age >30
# select id , count(distinct orderid) from data group by id;
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
# select * from t1 union select * from t2
# delete from t1where id=10
# alter table t1 drop column name

import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.randn(20,20))
a1 = data #select * from data
a2 = data.head(10)#select * from data limit(10)

data = pd.DataFrame(np.random.randint(3,8,size = (3,4)),index = ['year','month','day'],columns=['id','age','id3','id4'])
a3 = data['id']  # select id  from data  //id 是 data 表的特定一列
a4 = data.loc[(data2.id<1000)&(data2.age>30),:]
#select * from data where id <1000 and  age >30
data = pd.DataFrame(np.random.randint(3,9,size=(4,4)),index = [2,3,4,5],columns=['id','distinct','orderid','other'])
a5 = data[['distinct','orderid']].groupby(data['id']).count()   #select id , count(distinct orderid) from data group by id;

t1 = pd.DataFrame({'id':(1,2,3),'age' : (5,6,7)},index = ('a','b','c'),columns=('id','age'))
t2 = pd.DataFrame({'id':(1,2,3),'cd' : (5,6,7)},index = ('a','b','c'),columns=('id','cd'))

a6 = pd.merge(t1, t2, how='inner',on='id')  #select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
a7 =  pd.merge(t1, t2) #select * from t1 union select * from t2

t1 = pd.DataFrame({'id':(1,12,10),'age' : (5,6,7)},index = ('a','b','c'),columns=('id','age'))

a8 = t1[~t1['id'].isin([10])]  #delete from t1where id=10

#alter table t1 drop column name
a9 = t1.drop['name',axis =1]


print(a1,a2,a3,a4,a5,a6,a7,a8,a9)