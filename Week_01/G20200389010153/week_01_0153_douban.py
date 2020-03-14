# 需求：获得豆瓣电影名字、评分、短评数量和前五条热门短评
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import csv

# Python 使用 def 定义函数，url_tmp 是函数的参数
def get_url_content(url_tmp):
    # header声明为字典
    header = {}
    # 定义 header 为字典，需要指定类型
    header['user-agent'] = user_agent

    response = requests.get(url_tmp, headers=header)
    return response.text


def get_movie_detail(url_tmp):

    page_content = get_url_content(url_tmp)
    # response.text 为网页内容，文本文件，以'html.parser'的语法进行分析，是python内置的语法分析，速度为中等。还可以使用'lxml'，第三方语法分析，速度更快
    bs_info = bs(page_content, 'html.parser')

    # Python 中使用 for in 形式的循环,Python 使用缩进来做语句块分隔
    ## 混合使用模块和 for 的功能，因为 tags atag 对象既能支持 find_all 又拥有迭代功能，对象有继承的功能
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        # 获取a标签
        # atag = tags.contents[1]
        # print(atag)
        for atag in tags.find_all('a', ):
            # 获取所有链接
            movie_href = atag.get('href')
            print(movie_href)
            for spantag in tags.find_all('span', ):
                # line = line + ',' + title
                print(spantag)
                print(spantag.get_text())
            movie_url_list.append(movie_href)


def resolve_movie_info(url_tmp):
    content = {}
    page_content = get_url_content(url_tmp)
    bs_info = bs(page_content, 'html.parser')
    # 名称
    for tags in bs_info.find_all('div', attrs={'id': 'content'}):
        for h1 in tags.find_all('h1', ):
            name = h1.find_all('span', )[0].get_text()
            print(name)

    content['电影名称'] = name
    # 评分
    rating_tag = bs_info.find('strong', attrs={'class': 'll rating_num'})
    print(rating_tag)
    rating_num = rating_tag.get_text()
    print(rating_num)

    content['评分'] = rating_num
    # 评论数
    comments_head = bs_info.find('div', attrs={'id': 'comments-section'})
    # print(comments_head)
    comments_head_span = comments_head.find('span', attrs={'class': 'pl'})
    print(comments_head_span)
    comments_count_tag = comments_head_span.find('a')
    print(comments_count_tag)
    comment_count_text = comments_count_tag.get_text()
    print(comment_count_text)
    comment_count = comment_count_text.split(' ')[1]
    print(comment_count)

    content['短评数'] = comment_count
    # 前五短评 hot-comments
    comments_head_span = comments_head.find_all(
        'span', attrs={'class': 'short'})
    i = 1
    for hot_comment_tag in comments_head_span:
        hot_comment = hot_comment_tag.get_text()
        print(hot_comment)
        content['热门短评' + str(i)] = hot_comment
        i += 1
    print(content)
    return content


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

# top250 movie介绍页，每页25条，共10页，range(10)为10页
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(1))
## 推导式功能, 相当于
## for page in range(10)：
##     astring = 'https://movie.douban.com/top250?start={ page * 25}'
##     urls = tuple(astring)

# top250 movie详情页url
movie_url_list = []

## 单独执行 python 文件的一般入口
if __name__ == '__main__':
    for url in urls:
        get_movie_detail(url)
        sleep(5)
    print(movie_url_list)

    with open('movie-top250-comments.csv', 'w') as csv_file:
        fieldnames = ['电影名称', '评分', '短评数', '热门短评1',
                      '热门短评2', '热门短评3', '热门短评4', '热门短评5']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for movie_url in movie_url_list:
            print(movie_url)
            content_out = resolve_movie_info(movie_url)
            writer.writerow(content_out)
            sleep(5)
