import requests
import sys
import csv
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


def get_info(website):
    ua = UserAgent()
    user_agent = ua.random
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(website, headers=header)
    information = bs(response.text, 'lxml')
    return (information)


urls = tuple(
    f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

with open('C://Users/shz12/OneDrive/Desktop/douban_movie_top250.csv', 'w', encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(("片名", "评分", "评价人数", "五条热门短评"))

    for i in range(10):
        print(i)
        myurl = urls[i]
        info = get_info(myurl)
        tags = info.find_all('div', attrs={'class': 'info'})
        for atag in tags:
            title = atag.find('span', attrs={'class': 'title'}).text
            rating = atag.find('span', attrs={'class': 'rating_num'}).text
            rate_num = atag.find('div', class_='star').contents[7].text
            url = atag.find('a')['href']
            soup = get_info(url)
            main_directory = soup.find_all(
                'div', attrs={
            'id': 'hot-comments'})  # 一页当中25部电影的所有热评模块
            for sub_directory in main_directory:  # 一页当中每一部电影的热评模块
                five_comments = sub_directory.find_all('span', attrs={'class': 'short'})  # 每一部电影热评模块的五条短评
                comments = []
                for a_comment in five_comments:
                    comments.append(a_comment.text)
            writer.writerow((title, rating, rate_num, comments))
# res = requests.get(url, headers=headers)
#                                 # print(res.status_code)
#                                 # print(url)
#                                 soul = BeautifulSoup(res.text, 'html.parser')
#                                 items = soul.find_all('div', attrs={'class': 'info'})
#                                 # print(items)
#                                 for item in items:
#                                                                 urlx =   item.find('a')['href']
#                                                                 title = item.find('span', attrs={'class': 'title'}).text
#                                                                 rate = item.find('span', attrs={'class': 'rating_num'}).text
#                                                                 xxx = item.find('div', class_='star').contents[7].text
#                                                                 # ulist.append([urlx])
#                                                                 res_url = requests.get(urlx, headers=headers)
#                                                                 # print(res_url.status_code)
#                                                                 soul_url = BeautifulSoup(res_url.text, 'html.parser')
#                                                                 # print(soul1)
#                                                                 items_url = soul_url.find_all('div', class_='comment')
#                                                                 # print(items_url)
#                                                                 for item_url in items_url:
#                                                                                                 commente = item_url.find('span', attrs={'class': 'short'}).text
#                                                                                                 # print(commente)
#                                                                 # Xlist.append([commente])
#                                                                 Xlist.append(
#     [
#         title,
#         rate,
#         xxx,
#         commente])
# # print(Xlist)                
# for row in Xlist:
#                                 writer.writerow(row)
# csv_file.close()
# print('OOOOOOOOOOOOK--------------------------------------------------------------------')
