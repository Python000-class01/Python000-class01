import pymysql
import pandas as pd
from sqlalchemy import create_engine

conn = create_engine('mysql+pymysql://root:root@localhost:3306/test',encoding='utf8')

df1 = pd.read_csv('book.csv')

# pd.io.sql.to_sql(df, 'shuping', conn, if_exists = 'replace')
#　ALTER DATABASE skills CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
#  ALTER TABLE shuping CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
df1.to_sql('shuping', conn, if_exists = 'append', index=False)

# mapd={'testcol':["date"],'dd':['2017/01/01']}
# df=pd.DataFrame(mapd)
# df.to_sql('testpd',con=conn, if_exists='append', index=False)