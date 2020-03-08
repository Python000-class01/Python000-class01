# import requests
# from bs4 import BeautifulSoup
# res_foods = requests.get('http://www.xiachufang.com/explore/')
# bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# list_foods = bs_foods.find_all('div',class_='info pure-u')
# list_all = []
# for food in list_foods:
#     tag_a = food.find('a')
#     name = tag_a.text[17:-13]
#     URL = 'http://www.xiachufang.com'+tag_a['href']
#     tag_p = food.find('p',class_='ing ellipsis')
#     ingredients = tag_p.text[1:-1]
#     list_all.append([name,URL,ingredients])
# print(list_all)
# x = [2,4,6,8,9,0,7]
# y = [2,5,8,6]
# z = []
# for num in y:
#     print(num)
#     z.append([num,x])
#     print(z)
# import requests
# import csv
# from bs4 import BeautifulSoup
# import time
# csv_file = open('C:\\Users\\Administrator\\Desktop\\pac\\1017\\MMovie.csv','a',newline='',encoding='utf-8')
# writer = csv.writer(csv_file)
# writer.writerow(['电影名称','评分','短评数量','热门短评'])
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# }
# Xlist = []
# Ylist = []
# for x in range(10):
#     url = 'https://movie.douban.com/top250?start='+str(x*25) +'&filter='
#     res = requests.get(url, headers=headers)
#     soul = BeautifulSoup(res.text,'html.parser')
#     items = soul.find_all('div',attrs={'class':'info'})
#     for item in items:
#         murl =  item.find('a')['href']
#         title = item.find('span',attrs={'class':'title'}).text
#         rate = item.find('span',attrs={'class':'rating_num'}).text
#         xxx = item.find('div',class_='star').contents[7].text
#         print(murl,title,rate,xxx)
#         time.sleep(5)
#         res_url = requests.get(murl, headers=headers)
#         soul_url = BeautifulSoup(res_url.text,'html.parser')
#         items_url = soul_url.find_all('div',class_='comment')
#         for item_url in items_url:
#             comucating = item_url.find('span',attrs={'class':'short'}).text
#             Ylist.append([comucating])
#             time.sleep(5)
#         Xlist.append([title,rate,xxx,Ylist])
# print(Xlist)
# for row in Xlist:
#         writer.writerow(row)
# csv_file.close()
# print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK---------------------------')
        
        
# res = requests.get(url, headers=headers)
# print(res.status_code)
# soul = BeautifulSoup(res.text,'html.parser')
# items = soul.find_all('div',attrs={'class':'info'})
# for item in items:
#     murl = item.find('a')['href']
#     title = item.find('span',attrs={'class':'title'}).text
#     # print(murl)
#     time.sleep(5)
#     print(murl,title)



# a = [1,2,3]
# b = a
# a=[7]
# print(a)
# print(b)


# from bs4 import BeautifulSoup

# res = requests.get(url)
# print(res.status_code)



# import requests
# import json

# r = requests. post('http://httpbin.org/get', data = {'key':'value'})
# r.json()


import requests
url_get = ' http://httpbin.org/get'
url_post = 'http://httpbin.org/post'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
data = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    'key4':'value4',
    'key5':'value5',
    'key6':'value6',
    'key7':'value7'
}
res_get = requests.get(url_get,headers=headers,data=data)
res_post = requests.post(url_post,headers=headers,data=data)
print(res_get.status_code)
print(res_post.status_code)
# print(res_get)
# print(res_post)
print(res_get.json())
print(res_post.json())
