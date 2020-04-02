#region 作业要求
# 请将以下的 SQL 语句翻译成 Pandas 语句。
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
#endregion

import pandas as pd
import numpy as np

form_data_1 = pd.DataFrame({
    'id': range(0, 2000),
    'goods': range(0, 2000),
    'price': np.random.randint(0, 100, 2000)
})
form_data_2 = pd.DataFrame({
    'id': range(1000, 3000),
    'goods': range(1000, 3000),
    'price': np.random.randint(4, 500, 2000)
})
order_df = pd.DataFrame({
    'id': range(0, 20),
    "uid": np.random.randint(1000, 10015, 20),
    "orderid": np.random.randint(20200000, 20200100, 20),
    "amount": np.random.randint(50, 65, 20)
})

order2_df = pd.DataFrame({
    'id': range(0, 20),
    "uid": np.random.randint(1000, 10015, 20),
    "orderid": np.random.randint(20200000, 20200100, 20),
    "amount": np.random.randint(50, 65, 20)
})

user_df = pd.DataFrame({
    'id': range(0, 20),
    "uid": np.random.randint(1000, 10015, 20),
    "username": np.random.randint(20200000, 20200100, 20),
    "age": np.random.randint(18, 65, 20)
})
if __name__ == "__main__":
    # select * from data
    print('select * from data')
    print(form_data_1)
    print('\n')

    # select * from data limit(10)
    print('select * from data limit(10)')
    print(form_data_1[0:10])
    print('\n')

    # select id from data
    print('select id from data')
    print(form_data_1['id'])
    print('\n')

    # select count(id) from data
    print('select count(id) from data')
    print(form_data_1['id'].count())
    print('\n')

    # select * from data where id <1000 and  age >30
    print('select * from data where id <1000 and  age >30')
    print(form_data_1[(form_data_1['id'] < 1000)
                      & (form_data_1['price'] > 30)])
    print('\n')

   
    # select id, count(distinct orderid) from data group by id;
    print('select id, count(distinct orderid) from data group by id')
    print(form_data_1.groupby('id')['price'].nunique())
    print('\n')

    # select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
    print('select * from table1 t1 inner_join table2 t2 on t1.id = t2.id')
    print(pd.merge(form_data_1, form_data_2, on='id', how='inner'))
    print('\n')

    # select * from t1 union select * from t2
    print('select * from t1 union select * from t2')
    print(pd.concat([form_data_1, form_data_2]).drop_duplicates())
    print('\n')

    # delete from t1 where id=10
    print('delete from t1 where id=10')
    print(form_data_1[form_data_1['id'] != 10])
    print('\n')

    # alter table t1 drop column name
    print('alter table t1 drop column name')
    print( form_data_1.drop(['price'], axis=1))
    print('\n')