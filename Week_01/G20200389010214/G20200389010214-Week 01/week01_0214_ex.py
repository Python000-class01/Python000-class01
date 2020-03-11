import requests
import lxml.etree

def get_Movie():
    move_info = []
    for i in range(10):
        url='https://movie.douban.com/top250?start='+str(i*25) #各页面url
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
        header = {}
        header['user-agent'] = user_agent
        response = requests.get(url,headers=header)
        selector = lxml.etree.HTML(response.text)
        name = selector.xpath('//ol[@class="grid_view"]//div[@class ="hd"]/a/span[1]/text()')        #电影名
        link = selector.xpath('//ol[@class="grid_view"]//div[@class ="hd"]/a/@href')  #电影详情链接
        average = selector.xpath('//ol[@class="grid_view"]//div[@class="star"]/span[2]/text()')  #平均得分
        evaluate = selector.xpath('//ol[@class="grid_view"]//div[@class="star"]/span[4]/text()') #评论数量

        for num in range(len(name)):
            move_info.append((name[num],average[num],evaluate[num],link[num]))
    print("move ==>",move_info)
    columns_name = ['电影名','得分','评论数量','链接']
    import pandas as pd
    # book1 = pd.DataFrame(columns=columns_name,data = name)
    book1 = pd.DataFrame(columns=columns_name, data=move_info)
    book1.to_csv('./filmlist.csv', encoding='gbk')

get_Movie()


import json
url = 'http://httpbin.org/get'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
header = {}
header['user-agent'] = user_agent
response = requests.get(url, headers=header)
print("json->",response.json())
print("json=>",json.dumps(response.text))


url = 'http://httpbin.org/get'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
header = {}
header['user-agent'] = user_agent
response = requests.get(url, headers=header)
print("json->",response.json())
print("json=>",json.dumps(response.text))