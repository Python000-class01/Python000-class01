#--coding:utf-8--

import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
# 获取详情页面url
def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.find('ol', class_='grid_view').find_all('li')
    detail_urls = []
    for li in lis:
        detail_url = li.find('a')['href']
        # print(detail_url)
        detail_urls.append(detail_url)
    return detail_urls
#解析详情页面内容，
#把获取的链接放到列表作为返回值调用的时候用

def parse_detail_url(url,f):
    # 解析详情页面内容
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    # 电影名
    name = list(soup.find('div', id='content').find('h1').stripped_strings)
    name = ''.join(name)
    #评分数量
    num = soup.find('div', attrs={'class':'rating_sum'}).find('span').string
    #print(num)
    # 评分
    score = soup.find('strong', class_='ll rating_num').string
    #print(score)
    #前五短评
    b =str(' ')
    for tags in soup.find_all('div', class_='comment'):
        for tag in tags.find_all('span', class_='short'):
            a = tag.get_text()
            b += a
            #print(b) 这个地方有点瑕疵  循环出来的有不止五个 我想拼接好后到同一个字符串一起写入 这个地方应该有点问题
    sleep(5)
    f.write('{},{},{},{}\n'.format(name,num,score,b))

def main():
    base_url = 'https://movie.douban.com/top250?start={}&filter='
    with open('Topfhy.csv','a',encoding='utf-8') as f:
        for x in range(0,11):
            url = base_url.format(25*x)
            detail_urls = get_detail_urls(url)
            for detail_url in detail_urls:
               parse_detail_url(detail_url,f)


if __name__ == '__main__':
    main()

第二个作业
#使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，对 http://httpbin.org/post 进行 POST 方式请求，
# 并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。
import requests
import json
url = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/post'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3706.400 SLBrowser/10.0.3974.400'
}

geturl = requests.get(url,headers = headers)
#print(geturl.text)
print(geturl.json()) #requsets自带的函数
#result = json.dump(geturl)
#print(result) #json库 返库
data = {'nicai':222,'mima':3333}  #data参数
posturl = requests.post(url2,headers =headers,data=json.dumps(data)) #data 转化成json格式
print(posturl.json())