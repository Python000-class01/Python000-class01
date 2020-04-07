import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import re
import pandas as pd 

s= requests.Session()

def login_douban():
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    data={
        "ck":"",
        "name":"17604762977",
        "password":"lxm8225873",
        "remember":"true",
        "ticket":""}
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    try:
        r = s.post(login_url,headers = headers,data = data)
        r.raise_for_status()
    except:
        print('login Failed!')

    #print (r.text)


def spider_comment(scow_url):
    movie_comment=[]
    header= {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    response = requests.get(scow_url,headers=header)
    bs_info = bs(response.text, 'html.parser')
    # print(bs_info)
    for ctags in bs_info.find_all('span', attrs={'class': 'short'}):
        movie_comment.append(ctags.text+'\n')
    return movie_comment


if __name__ == '__main__':
    login_douban()
    f = open(r'毒液影评.txt', 'w', encoding='utf-8')
    for page in range(10):
        sleep(5)
        url = 'https://movie.douban.com/subject/3168101/comments?start=' + str(
			20 * page) + '&limit=20&sort=new_score&status=P'
        for i in spider_comment(url):
            f.write(i)
    print ('Done!=================================')

    






