
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas 
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}

def login(url):
    req = requests.get(url,headers=headers)
    if req.ok:
        return req.content.decode('utf-8')
    else:
        return None
    
data = []

def page(text):
    soup = BeautifulSoup(text, 'lxml')
    for s in soup.find_all('li',class_='comment-item'):
        datalist = {'用户名':s.find('span',class_='comment-info').get_text().strip()[:-12],
                    '评分': str(s.find('span',class_='comment-info').span).strip()[-29:-28],
                    '推荐': str(s.find('span',class_='comment-info').span).strip()[-11:-9],
                    '内容': s.find('span', class_="short").get_text(),
                    '评论时间': s.find('span',class_='comment-info').get_text().strip()[-10:]}
        data.append(datalist)

def writeexcel(localfile, text):
    pandas.DataFrame(text, columns=['用户名','评分','推荐', '内容', '评论时间']).to_csv(localfile, index=False,encoding='utf_8_sig')

def main(i):
    html = login('https://book.douban.com/subject/26895993/comments/hot?p=' + str(i))
    page(str(html))

if __name__ == '__main__':
    try:
        for i in range(1,20):
            time.sleep(2)
            print('正在爬取第%s页评论' %i)
            main(i)
            time.sleep(2)
    except:
        raise Exception
    excelpath = 'book.csv'
    writeexcel(excelpath, data)
    print('爬取完毕，共爬取%s页' %i)