import requests
from bs4 import BeautifulSoup as bs
import re
import lxml.etree
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
##这里如果不去定义 header 为字典直接使用是否会报错？
header['user-agent'] = user_agent

#电影名称、评分、短评数量、前5条热门短评
titleList = []
ratingList = []
ratingNumList = []
commentList = []

# Python 使用 def 定义函数，myurl 是函数的参数
def get_url_name(myurl):

    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')

    # Python 中使用 for in 形式的循环,Python 使用缩进来做语句块分隔
    ## 混合使用模块和 for 的功能，因为 tags atag 对象既能支持 find_all 又拥有迭代功能
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        span = tags.a.find_all('span')
        title = span[0].text
        titleList.append(title)
        href = tags.a.get('href')        
        commentList.append(get_hot_comments(href))

        
    for star in bs_info.find_all('div', attrs={'class':'star'}):
        span = star.find_all('span')
        rating = span[1].text
        rating_num = int(re.findall('\d+', span[3].text)[0])
        ratingList.append(rating)
        ratingNumList.append(rating_num)

    # return titleList.append(ratingList).append(ratingNumList).append(commentList)


def get_hot_comments(url):
    res = requests.get(url, headers=header)
    sleep(1)

    # comments = lxml.etree.HTML(res.text)
    # comment1 = comments.xpath('//*[@id="hot-comments"]/div[1]/div/p/span/text()')
    # comment2 = comments.xpath('//*[@id="hot-comments"]/div[2]/div/p/span[1]/text()')
    # comment3 = comments.xpath('//*[@id="hot-comments"]/div[3]/div/p/span')
    # print(comment1, comment2, comment3)
    
    bs_comment = bs(res.text, 'html.parser')

    comment_list = []
    i = 0
    for comments in bs_comment.find_all('div', class_="comment"):
        comment = comments.p.find_all('span')         
        comment_list.append(comment[0].text)
        i += 1
        if (i == 5):
            break
    
    return '\n'.join(comment_list)

urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}&filter='for page in range(10))

## 推导式功能, 相当于
## for page in range(10)：
##     astring = 'https://book.douban.com/top250?start={ page * 25}'
##     urls = tuple(astring)


from time import sleep
## autopep8 或者其他 IDE 会自动调整 import from 到文件最开头，
## 但是有的时候我们希望在某些对象实例化以后再去进行导入，
## 所以自动移动代码位置不一定每次都是正确的


## 单独执行 python 文件的一般入口
if __name__ == '__main__':
    for url in urls:
        # print(url)
        get_url_name(url)
        sleep(5)

    # print(titleList)
    # print(ratingList)
    # print(ratingNumList)
    # print(commentList)
    columns_name = ['电影名称','评分','短评数量','热门短评']
    data = {
        '电影名称':titleList,
        '评分':ratingList,
        '短评数量':ratingNumList,
        '热门短评':commentList
    }
    # data = {
    #     '电影名称':['电影1','电影2','电影3','电影4'],
    #     '评分':['1','2','3','4'],
    #     '短评数量':['10','20','30','40'],
    #     '热门短评':['啊啊啊','哈哈哈','嘿嘿嘿','呜呜呜']
    # }
    df = pd.DataFrame(data, columns = columns_name)
    df.to_csv('./movie.csv', encoding='utf-8')

