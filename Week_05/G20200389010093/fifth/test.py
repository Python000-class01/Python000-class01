import pandas as pd
from snownlp import SnowNLP
import pymysql

# df=pd.read_csv('comments.csv',encoding='utf-8',header=None)
# df.columns=['comments']
# # df.head()
#
# def _sentiment(text):
#     s=SnowNLP(text)
#     return s.sentiments
#
# df['sentiments']=df.comments.apply(_sentiment)
#
# df.to_csv('comt-sent.csv',index=False, header=False)

df=pd.read_csv('comt-sent.csv',encoding='utf-8',header=None)
df.columns=['comments','sentiments']
# df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1',
#              index =False, columns = ['comments','sentiments'])
# # print(df.head())
# # print(len(df))
# # print(df.loc[3,'comments'])
# # print(df.loc[1,'sentiments'])
#
# # #MySQL创建表语句
# # drop TABLE if EXISTS book_comments;
# # CREATE TABLE book_comments(
# # 	id int(10) not null PRIMARY KEY AUTO_INCREMENT,
# # 	comments MEDIUMTEXT,
# # 	sentiments float
# # )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '123456',
    db ='douban',
    charset ='utf8mb4'
)
# 获得cursor游标对象
cur = conn.cursor()

sql='INSERT INTO book_comments (comments,sentiments) VALUES (%s,%s)'
# try:
#用itertuples遍历dataframe每一行
for row in df.itertuples():
    cur.execute(sql,(getattr(row,'comments'),getattr(row,'sentiments')))

# 关闭游标
cur.close()
conn.commit()
# except:
#     conn.rollback()
conn.close()





