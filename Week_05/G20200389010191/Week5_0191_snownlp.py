from snownlp import SnowNLP
import pymysql
import pandas as pd 
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import re
import pandas as pd 


comment = []
with open('毒液影评.txt','r') as f:
    content = list(f.read().splitlines())
# print (len(content))
senti_score = []
for i in content:
    a1 = SnowNLP(i)
    a2 = a1.sentiments
    # print (a2)
    senti_score.append(a2)

dataframe = pd.DataFrame({'comment':content,'sentiment':senti_score})
dataframe.to_csv('Venmo.csv')

url = 'https://movie.douban.com/subject/3168101/'
header= {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
response = requests.get(url,headers=header)
bs_info = bs(response.text, 'html.parser')
score = bs_info.find('strong', attrs={'class': 'll rating_num'}).text
print (score)



df = pd.read_csv('Venmo.csv')
# print (df.comment)

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Lxm8225873#',
    'db' : 'Venmo'
}


def save_mysql(comm):
    s = SnowNLP(comm)
    conn = pymysql.connect(
        host=dbInfo['host'],
        port=dbInfo['port'],
        user=dbInfo['user'],
        password=dbInfo['password'],
        db=dbInfo['db']
    )
    cur = conn.cursor()
    values = (comm,s.sentiments)
    sql = 'insert into comment values (%s,%s)'
    cur.execute(sql,values)
    conn.commit()

df.comment.apply(save_mysql)
print ('Done!')


