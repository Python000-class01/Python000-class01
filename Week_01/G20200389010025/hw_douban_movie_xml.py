# 爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中
import requests
from bs4 import BeautifulSoup as bs
import csv
import lxml

# 根据电影链接地址，获取每部电影的电影名称、评分、短评数量和前 5 条热门短评，并返回
def get_movie_info_xml(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # 字典 需要声明
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl, headers=header)
    selector = lxml.etree.HTML(response.text)
    # 获取电影名称
    name = selector.xpath('//div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()')
    # print(name)
    # # 获取评分
    rating_num = selector.xpath('//div[@class="rating_self clearfix"]/strong/text()')
    # print(rating_num)
    # 获取短评数量
    votes = selector.xpath('//div[@class="rating_sum"]/a/span/text()')
    # print(votes)
    # # 获取前 5 条热门短评
    com_list = []
    for stags in selector.xpath('//div[@id="hot-comments"]//span[@class="short"]'):
        com_list.append(stags.text)
    movieinfo = [name, rating_num, votes] + com_list
    return movieinfo

# 获取本url地址上所有的电影链接，并返回
def get_movie_url_xml(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # 字典 需要声明
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    selector = lxml.etree.HTML(response.text)

    # html = lxml.etree.fromstring(response.text)
    # atag = html.xpath('//div[@class="item"]//div[@class="hd"]/a/@href')
    atags = selector.xpath('//div[@class="item"]//div[@class="hd"]/a/@href')
    return atags

def write_csv(filename, filecontents):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        cw = csv.writer(f)
        cw.writerow(filecontents)

# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(1))
from time import sleep

if __name__ == '__main__':
    # 将豆瓣电影top250的信息生成到csv文件中
    # csv文件名称
    csvfilename = 'top250电影信息表-xml.csv'
    # csv文件表头
    csvfileheader = ['序号', '电影名称', '评分', '短评数量'] + [f'热门短评{i}' for i in range(5)]
    # print(csvfileheader)
    write_csv(csvfilename, csvfileheader)
    # csv文件内容（一页上的内容）
    # # 处理每页上的电影信息(测试时用)
    # rownum = 1
    # for movieurl in get_movie_url_html('https://movie.douban.com/top250'):
    #     csvfilecontents = [f'{rownum}'] + get_movie_info_xml(movieurl)
    #     write_csv(csvfilename, csvfilecontents)
    #     rownum += 1

    rownum = 1
    for page in urls:
        for movieurl in get_movie_url_xml(page):
            print(rownum)
            csvfilecontents = [f'{rownum}'] + get_movie_info_xml(movieurl)
            write_csv(csvfilename, csvfilecontents)
            sleep(1)
            rownum += 1
        sleep(5)
