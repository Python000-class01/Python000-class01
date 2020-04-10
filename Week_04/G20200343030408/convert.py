# importing pandas package
import pandas as pd


# making data frame from csv file
data = pd.read_csv("age-single.csv", index_col="Name")



# select * from data
r = data[:][:] # retrieving columns by indexing operator
# select * from data limit(10)
r = data.head(10)
print(r)
# select id  from data  //id 是 data 表的特定一列
r = data[['id']]
# select count(id) from data
r = len(data['id'])
# select * from data where id <1000 and  age >30
r = data[(data.id < 1000) & (data.age > 30)]
# select id , count(distinct orderid) from data group by id;
r = data.groupby(['id'])
['orderid'].nunique().reset_index(name='distinct_orderid_count')
print(r)

data_1 = {'id':  ['1', '2',...],
        'col2': ['3', '4',...],
        }
data_2 = {'id':  ['8', '9',...],
        'col2': ['7', '6',...],
        }
t1 = pd.DataFrame (data_1, columns = ['id','col2'])
t2 = pd.DataFrame (data_2, columns = ['id','col2'])
# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
ret = pd.merge(t1, t2, on='id', how='inner')
# select * from t1 union select * from t2
ret = pd.concat([t1, t2], axis=0).drop_duplicates().reset_index()
# delete from t1where id=10
t1 = t1[t1.id != 10].reset_index(drop=True)
# alter table t1 drop column name
del t1['name']