import requests
import lxml.etree
from time import sleep
import pandas as pd



def get_movieInfo(url):
    """
    安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，
    并以 UTF-8 字符集保存到 csv 格式的文件中
    """
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    infos = selector.xpath('//*[@class="info"]')
    for info in infos:
        movie_url = info.xpath('div/a/@href')[0]
        movie_name = info.xpath('div/a/span[1]/text()')[0]
        rating_num = info.xpath('div//*[@class="rating_num"]/text()')[0]
        response2 = requests.get(movie_url, headers=header)
        selector2 = lxml.etree.HTML(response2.text)
        comments = selector2.xpath('//*[@id="hot-comments"]//p/span/text()')
        comments_num = selector2.xpath('//*[@id="comments-section"]//h2//a/text()')[0]
        row = [movie_name, rating_num, comments_num]
        row.extend(comments)
        print(row)
        # columns = ['电影名称', '评分', '短评数', 'hot1', 'hot2', 'hot3', 'hot4', 'hot5']
        df = pd.DataFrame([row])
        df.to_csv('data.csv', encoding='utf-8', mode='a', header=False, index=0, sep=',')


if __name__ == '__main__':
    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))
    for url in urls:
        get_movieInfo(url)
        sleep(5)
