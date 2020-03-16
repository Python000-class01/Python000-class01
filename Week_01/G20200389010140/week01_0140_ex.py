import requests
import csv
from time import sleep
from bs4 import BeautifulSoup as bs

def record_in_csv(datas):
    with open('result2.csv','a+') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(datas)

# Python 使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
   user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
   header = {}
   header['user-agent'] = user_agent
   response = requests.get(myurl,headers=header)
   bs_info = bs(response.text, 'html.parser')

   # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
   for tags in bs_info.find_all('div', attrs={'class': 'pl2'}):
       for atag in tags.find_all('a',):
           # 获取所有链接
           data = (atag.get('href'))+(atag.get('title'))
           print(data)
           record_in_csv(data)


# 生成包含所有页面的元组
urls = tuple('https://book.douban.com/top250?start=%d'%page for page in range(0,100,25))


if __name__ == '__main__':
   for page in urls:
       print(page)
       print("================================================================")
       get_url_name(page)
       sleep(8)