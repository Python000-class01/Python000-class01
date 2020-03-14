import requests
import time
import csv

def get_douban_movie_top250(myurl):
    # 表头
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    header = {'user-agent': user_agent}

    response = requests.get(myurl,headers=header)

    from bs4 import BeautifulSoup as bs

    bs_info = bs(response.text,'html.parser')

    for tags in bs_info.find_all('div',attrs={'class':'info'}):

        #电影名称
        filmname = tags.find('span',attrs={'class':'title'}).text

        #评分
        ratenum = tags.find('div', attrs={'class': 'star'}).find_all('span')[1].text

        #短评数量
        commentnum = tags.find('div', attrs={'class': 'star'}).find_all('span')[3].text

        #电影链接
        filmhref = tags.find('div', attrs={'class': 'hd'}).find('a').get('href')

        # print(filmname)
        # print(ratenum)
        # print(commentnum)

        #进入电影链接的详情页，获取前5条热门短评
        response_detail = requests.get(filmhref, headers=header)

        time.sleep(2)
        bs_info_detail = bs(response_detail.text,'html.parser')

        comment1 = bs_info_detail.find('div',attrs={'id': 'comments-section'}).find_all('span',attrs={'class': 'short'})[0].text
        comment2 = bs_info_detail.find('div', attrs={'id': 'comments-section'}).find_all('span', attrs={'class': 'short'})[1].text
        comment3 = bs_info_detail.find('div', attrs={'id': 'comments-section'}).find_all('span', attrs={'class': 'short'})[2].text
        comment4 = bs_info_detail.find('div', attrs={'id': 'comments-section'}).find_all('span', attrs={'class': 'short'})[3].text
        comment5 = bs_info_detail.find('div', attrs={'id': 'comments-section'}).find_all('span', attrs={'class': 'short'})[4].text

        # print(comment1)
        # print(comment2)
        # print(comment3)
        # print(comment4)
        # print(comment5)

        my_data.append([filmname,ratenum,commentnum,comment1,comment2,comment3,comment4,comment5])


# 所有翻页url
url=tuple(f'https://movie.douban.com/top250?start={x*25}&filter='for x in range(10))

my_data = []
my_data.append(['电影名称', '评分', '短评数量', '热评1', '热评2', '热评3', '热评4', '热评5'])

# 遍历各页面，抓去需要的信息
for my_url in url:
    get_douban_movie_top250(my_url)

# 输出csv文件
with open('hw1-dbMovie250.csv', 'a', encoding='utf-8', newline='')as csvfile:
    write = csv.writer(csvfile)
    for my_line in my_data:
        write.writerow(my_line)
print('finish')










