
import pandas as pd
import pymysql

ip = '192.168.99.100'
port = 3306
user = 'root'
passwd = 'admin'
dbname = 'PANDASTEST'
order_table_name = 'order_tlb'
customer_table_name = 'customer_tlb'
sql_order = 'select * from order_tlb'
sql_customer = 'select * from customer_tlb'

#select * from order_tlb;
#连接Mysql数据库读取表数据
conn = pymysql.connect(host=ip,port=port,user=user,passwd=passwd,db=dbname,charset='utf8')
df = pd.read_sql(sql=sql_order, con=conn)
print(df)
"""
      orderid  customerid   value        date
0           1           1    78.2  2020-01-07
1           2           2  3627.2  2020-01-07
2           3          47  2230.0  2020-03-01
3           4          42  6398.4  2020-01-25
4           5          95  3994.1  2020-02-28
...       ...         ...     ...         ...
"""

#存入csv文件以便后续分析
df.to_csv('order.csv')


#select * from order_tlb limit 10;
df2 = pd.read_csv('order.csv')[0:10]
print(df2)
"""
   Unnamed: 0  orderid  customerid   value        date
0           0        1           1    78.2  2020-01-07
1           1        2           2  3627.2  2020-01-07
2           2        3          47  2230.0  2020-03-01
3           3        4          42  6398.4  2020-01-25
4           4        5          95  3994.1  2020-02-28
5           5        6          96  1691.0  2020-02-24
6           6        7          74  6467.7  2020-02-03
7           7        8          35  1434.4  2020-03-24
8           8        9          53  8112.4  2020-03-08
9           9       10          10  6345.9  2020-03-21
"""

#select DISTINCT customerid from order_tlb;
df3 = pd.read_csv('order.csv').drop_duplicates(['customerid'])['customerid']
print(df3)
"""
0        1
1        2
2       47
3       42
4       95
      ...
401     21
440    112
458    100
481      4
698     36
Name: customerid, Length: 120, dtype: int64
"""

#select count(orderid) from order_tlb;
size = pd.read_csv('order.csv')['orderid'].shape[0]
print(size)
"""
5002
"""

#select * from order_tlb where date < '2020-03-01' and value > 2000;
df4 = pd.read_csv('order.csv')
df5 = df4[ ( df4['date']<'2020-03-01' ) & ( df4['value']>2000 )   ]
print(df5)
"""
      Unnamed: 0  orderid  customerid   value        date
1              1        2           2  3627.2  2020-01-07
3              3        4          42  6398.4  2020-01-25
4              4        5          95  3994.1  2020-02-28
6              6        7          74  6467.7  2020-02-03
10            10       11          99  9522.8  2020-01-19
...          ...      ...         ...     ...         ...
4993        4993     4994          69  2026.5  2020-01-26
4994        4994     4995          70  2056.5  2020-01-25
4999        4999     5000          32  2551.8  2020-02-20
5000        5000     5001         106  3851.5  2020-01-10
5001        5001     5002          81  4352.0  2020-01-14

[2673 rows x 5 columns]
"""

#select customerid , count(distinct orderid) from data group by customerid;
df6 = df4.groupby('customerid').count().iloc[:, [1]]
print(df6)
"""
            orderid
customerid
1                45
2                47
3                33
4                35
5                47
...             ...
116              41
117              41
118              36
119              54
120              30

[120 rows x 1 columns]
"""


#select * from order_tlb t1 inner join customer_tlb t2 on t1.customerid = t2.customerid
#读取Mysql customer表并存储为本地csv文件
#conn = pymysql.connect(host=ip,port=port,user=user,passwd=passwd,db=dbname,charset='utf8')
df7 = pd.read_sql(sql=sql_customer, con=conn)
df7.to_csv('customer.csv')
df8 = pd.read_csv('order.csv')
df9 = pd.merge(df8, df7, on='customerid')
print(df9)
"""
      Unnamed: 0  orderid  customerid   value        date  age   sex     job
0              0        1           1    78.2  2020-01-07   23  MALE  WORKER
1             95       96           1  2606.7  2020-01-19   23  MALE  WORKER
2            326      327           1  8692.6  2020-01-01   23  MALE  WORKER
3            351      352           1  3438.6  2020-03-13   23  MALE  WORKER
4            363      364           1  8883.9  2020-02-13   23  MALE  WORKER
...          ...      ...         ...     ...         ...  ...   ...     ...
4997        4557     4558          36  1096.2  2020-02-27   66  MALE    NULL
4998        4559     4560          36  7698.7  2020-03-14   66  MALE    NULL
4999        4711     4712          36  4017.5  2020-01-12   66  MALE    NULL
5000        4879     4880          36   743.2  2020-02-06   66  MALE    NULL
5001        4929     4930          36  9577.5  2020-03-18   66  MALE    NULL

[5002 rows x 8 columns]
"""

#select * from order_tlb union select * from customer_tlb;
df10 = pd.concat([df8, df7], axis=0, ignore_index=True)
print(df10)
"""
      Unnamed: 0  orderid  customerid   value        date   age   sex   job
0            0.0      1.0           1    78.2  2020-01-07   NaN   NaN   NaN
1            1.0      2.0           2  3627.2  2020-01-07   NaN   NaN   NaN
2            2.0      3.0          47  2230.0  2020-03-01   NaN   NaN   NaN
3            3.0      4.0          42  6398.4  2020-01-25   NaN   NaN   NaN
4            4.0      5.0          95  3994.1  2020-02-28   NaN   NaN   NaN
...          ...      ...         ...     ...         ...   ...   ...   ...
5117         NaN      NaN         116     NaN         NaN  52.0  MALE  NULL
5118         NaN      NaN         117     NaN         NaN  34.0  MALE  NULL
5119         NaN      NaN         118     NaN         NaN  74.0  MALE  NULL
5120         NaN      NaN         119     NaN         NaN  94.0  MALE  NULL
5121         NaN      NaN         120     NaN         NaN  70.0  MALE  NULL

[5122 rows x 8 columns]
"""

#delete from order_tlb where orderid=2
df11 = pd.read_csv('order.csv')
df12 = df11 [  df11['orderid'] !=2 ]
print(df12)
"""
      Unnamed: 0  orderid  customerid   value        date
0              0        1           1    78.2  2020-01-07
2              2        3          47  2230.0  2020-03-01
3              3        4          42  6398.4  2020-01-25
4              4        5          95  3994.1  2020-02-28
......
"""

#alter table orderid drop column date
df13 = pd.read_csv('order.csv')
print(df13.head(3)) 
"""
   Unnamed: 0  orderid  customerid   value        date
0           0        1           1    78.2  2020-01-07
1           1        2           2  3627.2  2020-01-07
2           2        3          47  2230.0  2020-03-01
"""
df14 = df13.drop(['date'] ,axis = 1)
print(df14.head(3))
"""
   Unnamed: 0  orderid  customerid   value
0           0        1           1    78.2
1           1        2           2  3627.2
2           2        3          47  2230.0
"""