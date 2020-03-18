import requests
from bs4 import BeautifulSoup as bs
import csv

# hw1 安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中。
collection = []

def get_url_name(url):
    # url = 'https://movie.douban.com/top250'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}  # declare caz we want to directly use it as a dictionary
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')  # convert text to sth that bs can identified
    # print(bs_info.find_all('span',attrs={'class':'title'})[0]) # find specific position without using reg exp
    # for tags in bs_info.find_all('span',attrs={'class':'title'}):
    # print(tags.text)
    # for atags in tags.find_all('a'):
    #     print(atags.get('href'))
    #     print(atags.get('title'))
    # print(response.text)
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        comments_list = []
        titles = tags.find_all('span', attrs={'class': 'title'})
        rates = tags.find_all('span', attrs={'class': 'rating_num'})
        atags = tags.find_all('div', attrs={'class': 'hd'})
        #print(titles[0])
        #collection.append([titles[0].text])
        #print(rates[0])
        #collection.append([rates[0].text])
        for hrefs in tags.find_all('a'):
            comments_page = (hrefs.get('href'))
            comment_response = requests.get(comments_page,headers=header)
            comment_url = bs(comment_response.text, 'html.parser')
            comments = comment_url.find_all('div', attrs={'class':'comment'})
            num_url = comment_url.find_all('div', attrs={'class':'mod-hd'})
            num = num_url[0].find_all('span', attrs={'class':'pl'})
            comment_numbers=num[0].find_all('a')[0].text
            for i in range(0,5):
                short_comment = comments[i].find_all('span', attrs={'class':'short'})
                #print(short_comment)
                comments_list.append(short_comment[0].text)
        collection.append([titles[0].text,rates[0].text,comment_numbers,comments_list])








#urls = tuple(f'https://movie.douban.com/top250?start={page * 1}' for page in range(1))

## 推导式功能, 相当于
## for page in range(10)：
##     astring = 'https://book.douban.com/top250?start={ page * 25}'
##     urls = tuple(astring)







from time import sleep

# autopep8 或者其他 IDE 会自动调整 import from 到文件最开头，
# 但是有的时候我们希望在某些对象实例化以后再去进行导入，
# 所以自动移动代码位置不一定每次都是正确的

## 单独执行 python 文件的一般入口
if __name__ == '__main__':
    f = open('movies.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(['movie_name', 'rating','comment nums', 'hot comments'])
    for page in range(10):
        astring = 'https://book.douban.com/top250?start={ page * 25}'
        urls = tuple(astring)
        url = 'https://movie.douban.com/top250?start='+str(page*25)
        #print(url)
        get_url_name(url)
        sleep(10)
    for row in collection:
        print(row)
        writer.writerow(row)
    f.close()




