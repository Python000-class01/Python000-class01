import requests
import csv
from bs4 import BeautifulSoup
import time
csv_file = open('C:\\Users\\Administrator\\Desktop\\pac\\1017\\MMovie.csv','a',newline='',encoding='gb2312')
writer = csv.writer(csv_file)
writer.writerow(['电影名称','评分','短评数量','热门短评'])
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
Xlist = []
Ylist = []
for x in range(10):
    url = 'https://movie.douban.com/top250?start='+str(x*25) +'&filter='
    res = requests.get(url, headers=headers)
    soul = BeautifulSoup(res.text,'html.parser')
    items = soul.find_all('div',attrs={'class':'info'})
    for item in items:
        murl =  item.find('a')['href']
        title = item.find('span',attrs={'class':'title'}).text
        rate = item.find('span',attrs={'class':'rating_num'}).text
        xxx = item.find('div',class_='star').contents[7].text
        print(murl,title,rate,xxx)
        time.sleep(5)
        res_url = requests.get(murl, headers=headers)
        soul_url = BeautifulSoup(res_url.text,'html.parser')
        items_url = soul_url.find_all('div',class_='comment')
        for item_url in items_url:
            comucating = item_url.find('span',attrs={'class':'short'}).text
            Ylist.append([comucating])
            time.sleep(5)
        Xlist.append([title,rate,xxx,Ylist])
print(Xlist)
for row in Xlist:
        writer.writerow(row)
csv_file.close()
print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK---------------------------')