import requests
from lxml import etree
from fake_useragent import UserAgent
import pandas as pd

#使用UserAgent随机获取headers,忽略SSL证书校验
ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent': ua.random
}

#实例化session
s = requests.Session()

#获取COOKIE
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck': '',
    'name': '18810365856',
    'password': 'xxxx@xxxx',
    'remember': 'false',
    'ticket': ''
}
response = s.post(login_url,data = form_data,headers = headers)

#爬取数据
def shuju(url):
    response2 = s.get(url, headers=headers)
    selector = etree.HTML(response2.text)
    name = selector.xpath('//*[@id="content"]//span[@class="title"][1]/text()')
    pingfen = selector.xpath('//*[@id="content"]//span[@class="rating_num"]/text()')
    dp_num = selector.xpath('//*[@id="content"]//div[@class="star"]/span[4]/text()')
    x_urls = selector.xpath('//*[@id="content"]//div[@class="hd"]/a/@href')
    reping1 = []
    reping2 = []
    reping3 = []
    reping4 = []
    reping5 = []
    for url1 in x_urls:
        response3 = s.get(url1,headers = headers)
        selector1 = etree.HTML(response3.text)
        reping = selector1.xpath('//*[@id="hot-comments"]/div[@class="comment-item"]/div/p/span[1]/text()')
        reping1.append(reping[0])
        reping2.append(reping[1])
        reping3.append(reping[2])
        reping4.append(reping[3])
        reping5.append(reping[4])

#导入数据
    mylist = {
        '电影名':name,
        '评分':pingfen,
        '短评数量':dp_num,
        '热评1':reping1,
        '热评2':reping2,
        '热评3':reping3,
        '热评4':reping4,
        '热评5':reping5,
         }
    columns_name = ['电影名','评分','短评数量','热评1','热评2','热评3','热评4','热评5',]
    move = pd.DataFrame(columns=columns_name,data=mylist)
    move.to_csv('C:\\Users\\ppton\\Desktop\\move.csv', mode='a', encoding='utf-8')

#程序入口
if __name__ == "__main__":
        for i in range(10):
            page = 'https://movie.douban.com/top250?start=0' + str(i*25)
            shuju(page)





