# encoding=utf-8
import pandas as pd
import pymysql

df = pd.read_csv('bookshorts.csv', sep='\t', encoding='utf-8')

df.columns = ['star', 'short', 'sentiment']

star_to_number = {
    '力荐': 5,
    '推荐': 4,
    '还行': 3,
    '较差': 2,
    '很差': 1
}

df['new_star'] = df['star'].map(star_to_number)

# 存入mysql
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='mysql',
    password='touhou',
    database='testdb',
    charset='utf8mb4'
)

cursor = conn.cursor()

star = df['new_star'].values.tolist()
short = df['short'].values.tolist()
sentiment = df['sentiment'].values.tolist()

# values = [(df['new_star'], df['short'], df['sentiment'])]
values = [i for i in zip(star, short, sentiment)]
cursor.executemany('insert into bookshorts(star, short, sentiment) values (%s, %s, %s)', values)

cursor.close()
conn.commit()
conn.close()
