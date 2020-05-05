import  requests
from bs4 import BeautifulSoup as bs
import csv

movie_headers = ['url', 'movie', 'comment1', 'comment2', 'comment3', 'comment4', 'comment5', 'star', 'comment_count']
movie_rows = []

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')
    # print(bs_info.find_all('div', attrs={'class': 'pl2'})[0])

    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    for info in bs_info.find_all('div', attrs={'class': 'info'}):
        info_tmp = []
        for tags in info.find_all('div', attrs={'class': 'hd'}):
            for atag in tags.find_all('a',):
                # print(atag)
                # 获取电影链接
                print(atag.get('href'))
                info_tmp.append(atag.get('href'))
                # 获取电影名称
                for title_tag in atag.find_all('span', attrs={'class': 'title'})[0]:
                    print(title_tag)
                    info_tmp.append(title_tag)
                # 获取详细页内的热门评论
                response_sub = requests.get(atag.get('href'), headers=header)
                bs_info_sub = bs(response_sub.text, 'html.parser')
                for info_sub in bs_info_sub.find_all('div', attrs={'id': 'hot-comments'}):
                    for hot_comment in info_sub.find_all('div', attrs={'class': 'comment-item'}):
                        for comment_item in hot_comment.find_all('span', attrs={'class': 'short'})[0]:
                            print(comment_item)
                            info_tmp.append(comment_item)
        for stars in info.find_all('div', attrs={'class': 'star'}):
            # print(stars)
            # 获取评分
            for comments_rate in stars.find_all('span')[1]:
                print(comments_rate)
                info_tmp.append(comments_rate)
            # 获取评论总数
            for comments_count in stars.find_all('span')[3]:
                print(comments_count)
                info_tmp.append(comments_count)
        # print(info_tmp)
        movie_rows.append(info_tmp)

    with open('geek1_movie.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(movie_headers)
        f_csv.writerows(movie_rows)
    
# 生成包含所有页面的元组
# f-string用法
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(2))
# urls = 'https://movie.douban.com/top250?start=&filter='
print(urls)

from time import sleep

if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)