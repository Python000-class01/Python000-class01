# 爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中
import requests
from bs4 import BeautifulSoup as bs
import csv

# 根据电影链接地址，获取每部电影的电影名称、评分、短评数量和前 5 条热门短评，并返回
def get_movie_info_html(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # 字典 需要声明
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')
    # print(bs_info.get('h1'))
    # 获取电影名称
    name = bs_info.find_all('span',attrs={'property':'v:itemreviewed'})[0].text
    # 获取评分
    rating_num = bs_info.find_all('strong',attrs={'class':'ll rating_num'})[0].text
    # 获取短评数量
    votes = bs_info.find_all('span',attrs={'property':'v:votes'})[0].text
    # 获取前 5 条热门短评
    com_list = []
    for hottags in bs_info.find_all('div', attrs={'class':'comment'}):
        for ctags in hottags.find_all('p', ):
            for stags in hottags.find_all('span', attrs={'class':'short'}):
                com_list.append(stags.text)
    movieinfo = [name, rating_num, votes] + com_list
    return movieinfo

# 获取本url地址上所有的电影链接，并返回
def get_movie_url_html(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # 字典 需要声明
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')

    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    for hdtags in bs_info.find_all('div', attrs={'class': 'hd'}):
        # print(hdtags)
        for atag in hdtags.find_all('a',):
            # 获取所有链接
            # print(atag.get('href'))
            yield atag.get('href')


def write_csv(filename, filecontents):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        cw = csv.writer(f)
        cw.writerow(filecontents)

from time import sleep
    # 生成包含所有页面的元组
    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

if __name__ == '__main__':
    # 将豆瓣电影top250的信息生成到csv文件中
    # csv文件名称
    csvfilename = 'top250电影信息表-html.csv'
    # csv文件表头
    csvfileheader = ['序号', '电影名称', '评分', '短评数量'] + [f'热门短评{i}' for i in range(5)]
    # print(csvfileheader)
    write_csv(csvfilename, csvfileheader)
    # csv文件内容（一页上的内容）
    # # 处理每页上的电影信息(测试时用)
    # rownum = 1
    # for movieurl in get_movie_url_html('https://movie.douban.com/top250'):
    #     csvfilecontents = [f'{rownum}'] + get_movie_info_html(movieurl)
    #     write_csv(csvfilename, csvfilecontents)
    #     rownum += 1

    rownum = 1
    for page in urls:
        for movieurl in get_movie_url_html(page):
            print(rownum)
            csvfilecontents = [f'{rownum}'] + get_movie_info_html(movieurl)
            write_csv(csvfilename, csvfilecontents)
            sleep(1)
            rownum += 1
        sleep(5)







