import requests
from bs4 import BeautifulSoup as bs
import csv
from time import sleep
header = dict()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
header['user-agent'] = user_agent
with open('result.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([['title', 'score', 'score_num', 'short1', 'short2', 'short3', 'short4', 'short5']])


def get_url_name(douban_url: str):
    response = requests.get(douban_url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    all_book_info_tags = bs_info.find_all('div', attrs={'class': 'pl2'})
    all_star_tags = bs_info.find_all('div', attrs={'class': 'star clearfix'})
    with open('result.csv', 'a', encoding='utf-8', newline='') as f1:
        writer1 = csv.writer(f1)
        for index, tags in enumerate(all_book_info_tags):
            for atag in tags.find_all('a', ):
                # 获取所有链接
                book_href = atag.get('href')
                book_title = atag.get('title')
            star_spans = all_star_tags[index].find_all('span', )
            score = star_spans[1].text
            score_num = star_spans[2].text
            data = [book_title, score, score_num]
            short5 = get_hot(book_href, 5)
            data.extend(short5)
            writer1.writerows([data])



def get_hot(hot_url: str, mum: int):
    # 获取前5短评
    response = requests.get(hot_url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    all_short_tags = bs_info.find_all('span', attrs={"class": 'short'})
    result = list()
    for index, tag in enumerate(all_short_tags):
        if index < 5:
            result.append(all_short_tags[index].text)
    return result


urls = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(10))
# 推导式功能,相当于
# for page in range(10)：
#     astring = 'https://book.douban.com/top250?start={ page * 25}'
#     urls = tuple(astring)




## autopep8 或者其他IDE 会自动调整import from 到文件最开头，
## 但是有的时候我们希望在某些对象实例化以后再去进行导入，
## 所以自动移动代码位置不一定每次都是正确的


## 单独执行python文件的一般入口
if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)