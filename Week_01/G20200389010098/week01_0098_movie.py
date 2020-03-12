import requests
from bs4 import BeautifulSoup as bs
import re
import csv
from time import sleep
from fake_useragent import UserAgent
import time

#调试
def z(data):
    print(data)
    exit()

#统一http请求
def getHttp(url):
    ua = UserAgent()
    headers = {
        'User-Agent':  ua.random
    }
    print(ua.random)
    res = requests.get(url, headers=headers)
    if (res.status_code==200):
        return bs(res.text, 'lxml')
    else:
        return False
def getComment(url):
    bs_info=getHttp(url+'comments?sort=new_score&status=P')
    comment=[re.sub(r'\s+', '', x.text) for x in bs_info.find_all('span',{'class':'short'}, limit=5)]
    return comment
def maker(url):
    global num
    bs_info = getHttp(url)
    title=[x.find('span',{'class':'title'}).text for x in bs_info.find_all('div',{'class':'hd'})]
    href=[x.find('a').get('href') for x in bs_info.find_all('div',{'class':'hd'})]
    star=[x.text for x in bs_info.find_all('span',{'class':'rating_num'})]
    comment_num = [x.contents[7].text[:-3] for x in bs_info.find_all('div',{'class':'star'})]
    #非常喜欢用select，但是find_all速度是2到3倍，放弃
    #comment_num = [x.text[:-3] for x in bs_info.select("body div.star span:last-child")]
    print('列表读取完毕')
    sum= []
    for i in range(0,25):
        comment_top5=getComment(href[i])
        print(f'{num}、{title[i]}评论读取完毕')
        #sleep(1)
        print(comment_top5)
        sum.append([title[i],star[i],comment_num[i],
                    comment_top5[0],
                    comment_top5[1],
                    comment_top5[2],
                    comment_top5[3],
                    comment_top5[4]])
        num+=1
    return sum
urls=tuple([f'https://movie.douban.com/top250?start={str(x)}' for x in range(0,226,25)])

if __name__ == '__main__':
    num = 1
    data=[]
    for page in urls:
        data=data+maker(page)
    with open("douban_movie250" + ".csv", "w+", newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['电影名', '评分', '短评数量','评论1','评论2','评论3','评论4','评论5'])
        for i in data:
            writer.writerow(i)
        print('csv写入完毕')