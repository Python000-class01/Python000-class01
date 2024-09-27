reated on 2020年3月11日

@author: 86151
'''

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

def doubanTopMovie(url,k1 = 'movieName',k2 = 'movieScore',k3 = 'movieCommonLink'):
    movieList = []
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
    r1 = requests.get(url,headers=header)
    soup = BeautifulSoup(r1.text,'html.parser')
    ret = soup.find_all('div',class_='item')
    for k in ret:
        titleName = ""
        score = ""
        herf = k.a['href']
        for l in k.find_all('span',class_=['title','other','rating_num']):
            if 'title' in l['class']:
                titleName += l.string
            if 'other' in l['class']:
                titleName += l.string
            if 'rating_num'  in l['class']:
                score = l.string  
        movieList.append({k1:titleName,k2:score,k3:herf})
    return movieList                

def doubanMovieCommon(url,k1 = 'commonNum',k2 = 'hotcommon' ):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
    hotCommon = []
    commonMesag = {}
    r1 = requests.get(url,headers=header)
    soup = BeautifulSoup(r1.text,'html.parser')
    ret = soup.find_all('div',id='hot-comments')
    for k in ret:
   #print(k.find_all('span',class_='short'))
      for l in k.find_all('span',class_='short'):
        #print(l.string)
        hotCommon.append(l.string)
        #print("****************")
       #print(l.string))
    #print(hotCommon)
    urltemp = url + 'comments?status=P'
    ret1 = soup.find('a',href=urltemp)     
    commonMesag[k1] = ret1.string
    commonMesag[k2] = hotCommon
    #print(commonMesag)
    return commonMesag


url1 = 'https://movie.douban.com/top250?start=0&filter='
url2 = 'https://movie.douban.com/subject/1292052/'
movieList = []
doubanTopMovie = doubanTopMovie(url1)
#print(doubanTopMovie)
for l in doubanTopMovie:
    url = l.get('movieCommonLink')
    commonMesag = doubanMovieCommon(url)
    commonMesag.get('commonNum')
    commonMesag.get('hotcommon')
    movieList.append({'movieName':l.get('movieName'),'movieScore':l.get('movieScore'),'commonNum':commonMesag.get('commonNum'),'hotcommon':commonMesag.get('hotcommon')})
#print(movieList) 
df = pd.DataFrame(movieList)
df.to_csv('pandas_new.csv',encoding="utf-8")

   
    

    
