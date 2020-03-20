#coding:utf-8
import requests
from  bs4 import BeautifulSoup as bs
from time import sleep
import csv

t1=[]
t2=[]
t3=[]
t4=[]
t5=[]

header={}
header['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

#获得网页图书的链接、标题和评分
def get_url_title(url):
    response=requests.get(url,headers=header)
    soup=bs(response.text,'html.parser')
    t0 = []
    for tag in soup.find_all('div',attrs={'class':'hd'}):
        #获取每个电影的链接并追加至t0中
        t0.append(tag.a.get('href'))
        #获取每个电影的名字并追加至t2中
        t2.append(tag.a.find_all('span')[0].string)
    #获取每个电影的评分并追加至t3中
    for tag in soup.find_all('span',attrs={'class','rating_num'}):
        t3.append(float(tag.string))
    return t0


#获取图书的短评数、前5条热门短评
def get_url_com(url):
    response = requests.get(url, headers=header)
    soup = bs(response.text, 'html.parser')
    #获取每个电影的短评数并追加至t4中
    st=soup.find('div',attrs={'id':'comments-section'}).find('span',attrs={'class':'pl'}).a.string
    st = st[2:]
    st = st[:len(st)-1]
    t4.append(eval(st))
    #获取每个电影的前5条热门短评并追加至t5中
    st5 = []
    for tag in soup.find('div',attrs={'id':'hot-comments'}).find_all('span',attrs={'class':'short'}):
        st5.append(tag.string)
    t5.append(st5)


#爬取10页信息
def some_page(n):
    for page in range(n):
        url=f'https://movie.douban.com/top250?start={page*25}&filter='
        t0=get_url_title(url)
        t1.extend(t0)
        for url in t0:
            get_url_com(url)
        sleep(5)
    # print(t2)
    # print(t3)
    # print(t4)
    # print(t5)
    # # print(len(t1))
    # # print(len(t2))
    # # print(len(t3))
    # # print(len(t4))
    # # print(len(t5))
    with open('film_info.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'score', 'st_num', 'st_f5'])
        for i in range(len(t2)):
            per_book = [t2[i],t3[i],t4[i],t5[i]]
            writer.writerow(per_book)

if __name__=='__main__':
    some_page(10)
























