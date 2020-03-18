import requests
from bs4 import BeautifulSoup as Bs
from time import sleep
import csv
import pandas as pd


def get_bs_info(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    return Bs(response.text, "html.parser")

#前5条热门短评
def get_urls_comment(url):
    i = 0
    comment = []
    comments = get_bs_info(url).find('div', attrs={'id': 'hot-comments'})

    for short in comments.find_all('span', attrs={'class': 'short'}):
        r = str(str(i + 1) + ':' + short.text.replace('\r', '').replace('\n', ';'))
        comment.append(r)
        i += 1
        if i == 5:
            break
    return comment


def get_urls_all(myurl):
    for tags in get_bs_info(myurl).find_all('div', attrs={'class': 'info'}):
        for atag in tags.find_all('a'):
            # 短评链接
            url2 = atag.get('href')
            # 影名
            file = atag.find('span')
            filename = file.text
        for btag in tags.find_all('div', attrs={'class': 'star'}):
            # 评分
            score = btag.find('span', attrs={'class': 'rating_num'}).text
            # 影评人数
            num = btag.find_all('span')[-1].text[0:-3]

        review = get_urls_comment(url2)
        row = [filename, score, num]
        row.extend(review)
        print(row)
        with open('./comment.csv', 'a', newline='', encoding='utf-8_sig') as f:
            w = csv.writer(f)
            w.writerow(row)
        sleep(0.5)

if __name__ == '__main__':
     urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))
     for page in urls:
         data = get_urls_all(page)

         row1 = ["名称", "评分", "短评数量", "热评1", "热评2", "热评3", "热评4", "热评5"]

         df_data = pd.DataFrame(data=data, columns=row1)

         df_data.to_csv("./week1.csv", encoding="utf-8-sig")
         sleep(5)