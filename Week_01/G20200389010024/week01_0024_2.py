import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def GetComment(url):
    response = requests.get(url,headers = header)
    bs_info = bs(response.text,'html.parser')
    CommentList=[]
    for ptag in bs_info.find_all('span',attrs={'class':'short'}):
        if not (str.isspace(ptag.contents[0])):
            CommentList.append(ptag.contents[0])
    return CommentList

def SaveFilmInfo(url):
    #请求网址内容
    response = requests.get(url,headers = header)
    bookinfoAll=[]
    #把得到的内容转成文本格式
    bs_info = bs(response.text,'html.parser')
    for tags in bs_info.find_all('div',attrs={'class':'info'}):
        for atag in tags.find_all('a',):
            bookComment = GetComment(atag.get('href'))
            booktitle=''
            for stag in atag.find_all('span',attrs={'class':'title'}):
                booktitle = booktitle+ stag.contents[0]
        for tags1 in tags.find_all('div',attrs={'class':'star'}):
            for stag in tags1.find_all('span',attrs={'class':'rating_num'}):
                bookstart = stag.contents[0]
            shortnum=(tags1.contents[7]).contents[0]
        bookinfo=[booktitle,bookstart,shortnum,bookComment[0],bookComment[1],bookComment[2],bookComment[3],bookComment[4]]
        bookinfoAll.append(bookinfo)
        bookinfo=[]
    return bookinfoAll


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
header = {}
header['user-agent'] = user_agent
listall=[]

for page in range(10):
    num = 25*page
    web = 'https://movie.douban.com/top250?start='+ str(num)
    listone =SaveFilmInfo(web)
    listall.extend(listone)

colums_name=['电影名称','评分','短评数量','前 5 条热门短评1','前 5 条热门短评2','前 5 条热门短评3','前 5 条热门短评4','前 5 条热门短评5']


book1= pd.DataFrame(columns =colums_name,  data=listall)
book1.to_csv('./book1.csv',encoding='UTF-8')
