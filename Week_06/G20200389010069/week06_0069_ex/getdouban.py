import requests
from bs4 import BeautifulSoup as bs



url = 'https://book.douban.com/subject/34822422/reviews'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3706.400 SLBrowser/10.0.3974.400'}
respons = requests.get(url,headers=headers)
bs_info = bs(respons.text,'html.parser')
print(bs_info)
shortcontent = bs_info.find_all('div',attrs={'class':"short-content"})

with open('ciyu.txt','w',encoding='utf-8') as f :
    for i in shortcontent:
        i = i.get_text()
        f.write(i)









