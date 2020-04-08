import os
import re
from os import path
import numpy as np
import jieba.analyse
from wordcloud import wordcloud,STOPWORDS,ImageColorGenerator
import PIL
from matplotlib import pyplot as plt
import requests
import random
from bs4 import BeautifulSoup
class findcontent(object):
    def __init__(self):
        pass
    def B_url(self):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
            }
        num_1 = int(input('input a number between 0-10 '))
        b_url = 'https://book.douban.com/top250?start='+str(num_1)
        b_res = requests.get(b_url,headers= headers)
        soul =  BeautifulSoup(b_res.text,'html.parser')
        items = soul.find_all('div',attrs={'class':'pl2'})
        url_list = []
        for item in items:
            b_url = item.find('a')['href']
            url_list.append(b_url)
        return url_list
    def R_url(self):
        B_num = self.B_url()
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
            }
        num_2 = int(input('input a number between 0-25 '))
        r_url = B_num[num_2]
        r_res = requests.get(r_url,headers = headers)
        soup = BeautifulSoup(r_res.text,'html.parser')
        projs = soup.find_all('div',attrs={'class':'review-short'})
        numing = soup.find('strong').text
        return projs,numing
    def flow_R(self):
        Xin = self.R_url()
        Yin = Xin[0]
        Zin = Xin[1]
        CONTent = []
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        try:
            for item in Yin:
                tag_id = item.find('a')['id'][7:-5]
                url = 'https://book.douban.com/review/'+str(tag_id)
                res = requests.get(url,headers=headers)
                review_s = BeautifulSoup(res.text,'html.parser')
                content_s = review_s.find('div',attrs={'class':'review-content clearfix'}).text
                CONTent.append([content_s])
        except IndexError:
            print('没找着，从新运行')
        return CONTent,Zin
if __name__ == '__main__':
    begining = findcontent()
    returning = begining.flow_R()
    content = returning[0]
    Num = returning[1]
    print(type(content))
    contents = 0
    for x in range(len(content)):
        contents = str(contents) + str(content[x])
    tfidf = jieba.analyse.extract_tags(contents,topK=10,withWeight=False)  
    wordcloud.random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None)
    num=random.randint(1,20)
    image1 = PIL.Image.open(r'C:\\Users\\Administrator\\Desktop\\pac\\1017\\ciyun\\item'+ str(num)+'.JPG')
    MASK = np.array(image1)
    WC = wordcloud.WordCloud(font_path = 'STFANGSO.TTF',max_words=2000,mask = MASK,height= 400,width=400,background_color='white',repeat=False,mode='RGBA')
    st1 = re.sub('[，。、“”‘ ’]','',str(tfidf))
    conten = ' '.join(jieba.lcut(st1))
    con = WC.generate(conten)
    plt.imshow(con)
    WC.to_file('C:\\Users\\Administrator\\Desktop\\pac\\1017\\ciyun\\test'+str(num)+'.png')
    plt.axis("off")