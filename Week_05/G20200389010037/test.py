import random
import requests
import lxml.etree
import pandas as pd
import numpy  as np
from snownlp import SnowNLP
import pymysql
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
def  Find():
    num1=random.randint(0,10)
    num2=random.randint(0,25)
    url1 = 'https://book.douban.com/top250?start='+str(num1)
    res1 =requests.get(url1,headers=header)
    soup1 =lxml.etree.HTML(res1.text)
    url2 = soup1.xpath('//*[@id="content"]/div/div[1]/div/table''+str(num2)+/tbody/tr/td[2]/div[1]/a/@href')
    print(url2)
    res2 = requests.get(url2,headers=header)
    soup2 =lxml.etree.HTML(res2.text)
    ititle = soup2.xpath('//*[@id="wrapper"]/h1/span/text()')
    inum = soup2.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')
    istar = soup2.xpath('//*[@class="main-hd"]/span[1]')
    icomment_id = soup2.xpath('//*[@id="content"]/div/div[1]/div[3]/section[2]/div[2]/div/@data-cid')
    for x in range(len(icomment_id)):
        url3 = 'https://book.douban.com/j/review/'+str(icomment_id[x])
        res3 = requests.get(url3,headers=header)
        soup3 =lxml.etree.HTML(res3.text)
        icomment =soup3.xpath('//*[@class="review-content clearfix"]text()')
    iview=[]
    for i in range(len(istar)):
        comment = [istar[i],istar[i]]
        iview.append(comment)
    return ititle,inum,istar,icomment,iview

def snowniP(defer):
    star = istar
    comment_list = icomment
    df =pd.DataFrame([star,comment_list],  columns=["0","1","2","3","4","5","6","7","8","9"])
    df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    # 10c 2index  -------------    2c 10 index
    star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
    }       
    df['new_star'] = df['star'].map(star_to_number)
    def _sentiment(text):
        s = SnowNLP(text)
        return s.sentiments
    df["sentiment"] = df.shorts.apply(_sentiment)
    df.head()
    df.sentiment.mean()

def pymySQL():
    # create database pymySQL;
    conn = connect(host='localhost', port=22, database='Mysql', user='root',password='Wo123456', charset='utf8')
    cursor = conn.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS db_name"
    cursor.execute(sql)
    sql_2 = '''CREATE TABLE `comment` (
        `title` INT NOT NULL AUTO_INCREMENT,
        `num` INT ,
        `ptd` INT NOT NULL,
        `pqx` INT NOT NULL
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
    cursor.execute(sql_2)
    sql = "insert into movie1 values ('ttle','num','ptd','pqx');"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    


if __name__ == '__main__':
    defer = Find()
    snowniP(defer)
    pymySQL(defer)
