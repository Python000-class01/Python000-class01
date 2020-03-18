import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
from time import sleep

url_list = [] #save href of each movie
rate_list = []#rate list)
comment_list = []#short comment list
movie_list = []#movie name list
commnet_num_list = []#the number of short comment
data_list = []


def get_myurl(scow_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(scow_url,headers=header)
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        for atag in tags.find_all('a',):
            movie_href =atag.get('href')
            res = requests.get(movie_href,headers=header)
            comment_info = bs(res.text,'html.parser')
            for ctags in comment_info.find_all('div', attrs={'class': 'comment'}):
                movie_comment = ctags.find(name = 'span',class_='short').text
                #print (movie_comment)
                comment_list.append(movie_comment)
            rtags = comment_info.find('div', attrs={'class': 'mod-hd'})
            movie_evel = rtags.find('span',attrs={'class':'pl'}).find('a').text
            commnet_num_list.append(movie_evel)
            #print (movie_evel)
            #url_list.append(movie_href)
            #print (movie_href)
            movie_name = atag.find(name = 'span',class_ = 'title').text
            movie_list.append(movie_name)
           # print (movie_name)
    for rtags in bs_info.find_all('div', attrs={'class': 'star'}):
        movie_score = rtags.find(name = 'span',class_='rating_num').text
        rate_list.append(movie_score)
    


#def func(listTemp, n):
#    for i in range(0, len(listTemp), n):
#        yield listTemp[i:i + n]


urls = tuple(f'https://movie.douban.com/top250?start={page *25}&filter=' for page in range(10))


if __name__ == '__main__':
    for page in urls:
        get_myurl(page)
        sleep(5)
#temp = func(comment_list,5)
c1=comment_list[0:len(comment_list):5]
c2=comment_list[1:len(comment_list):5]
c3=comment_list[2:len(comment_list):5]
c4=comment_list[3:len(comment_list):5]
c5=comment_list[4:len(comment_list):5]
d = zip(movie_list,rate_list,commnet_num_list,c1,c2,c3,c4,c5)
data_list = list(d)

csv_file = open('/Users/liximing/Documents/Testing-Python/GeekBang_python/Week 01/TOP250_v1.csv','w',newline='', encoding= 'utf-8')
writer=csv.writer(csv_file)
writer.writerow(['电影名称','评分','短评数量','热门短评1','热门短评2','热门短评3','热门短评4','热门短评5'])
for i in data_list:
    writer.writerow(i)

csv_file.close()
#dataFrame = pd.DataFrame({'电影名称':movie_list,'评分':rate_list,'短评数量':commnet_num_list,'热门短评':temp})
#dataFrame.to_csv('/Users/liximing/Documents/Testing-Python/GeekBang_python/week1/TOP25.csv',sep=',')

print('==============================================')
