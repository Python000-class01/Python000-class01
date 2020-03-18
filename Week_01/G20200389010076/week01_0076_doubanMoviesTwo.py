from requests_html import HTMLSession
import re
import pandas as pd

#获取session
class Tool():
    session = None
    @classmethod
    def get_session(cls):
        if cls.session==None:
            cls.session=HTMLSession()
        return cls.session


#获取每页的电影详细页地址，返回50条地址
def getMoviesUrls(page):
    #HTMLSession
    url = 'https://movie.douban.com/top250'
    start=str(page*25)
    data={'start':start}
    response=Tool.get_session().get(url,params=data)
    movies_urls=response.html.xpath('//ol[@class="grid_view"]/li/div/div[1]/a/@href')
    return movies_urls

#爬所需要的数据，返回爬取到的数据
def crawlDatas(movies_url):
    movies_names,movies_evalutes,short_comment_counts,hot_short_comments = [],[],[],[]

    movies_response = Tool.get_session().get(movies_url)
    movies_html = movies_response.html

    # 爬取名称
    movies_name = movies_html.xpath('//div[@id="content"]/h1/span[1]/text()')[0]
    # 爬取评分
    movies_evalute = movies_html.xpath('//div[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
    # 爬取短评数量
    short_comment_count = movies_html.xpath('//div[@id="comments-section"]/div/h2/span/a/text()')[0]
    regex = re.compile(r'\d+')
    short_comment_count = regex.search(short_comment_count).group()
    # 爬取热门短评
    hot_short_comment = movies_html.xpath('//div[@id="hot-comments"]/div/div/p/span/text()')

    movies_names.append(movies_name)
    movies_evalutes.append(movies_evalute)
    short_comment_counts.append(short_comment_count)
    hot_short_comments.append(hot_short_comment)

    return movies_names,movies_evalutes,short_comment_counts,hot_short_comments

#处理爬取到的数据
def dealDatas(data_list):
    datas = {'moviesName': data_list[0], 'moivesEvalute': data_list[1], 'moviesCommentCout': data_list[2],
             'moviesHotComment': data_list[3]}
    movies = pd.DataFrame(data=datas)
    movies.to_csv('./moviesTwo.csv', encoding='utf-8', mode='a', header=False, index=False)

#对50条地址进行处理
def deal_urls(movies_urls):
    for movies_url in movies_urls:
        #爬取数据
        data_list=crawlDatas(movies_url)
        #将爬取的数据进行处理
        dealDatas(data_list)
    print('爬虫结束了')


if __name__ == '__main__':
    columns = ['moviesName', 'moivesEvalute', 'moviesCommentCout', 'moviesHotComment']
    movies = pd.DataFrame(columns=columns)
    movies.to_csv('./moviesTwo.csv', encoding='utf-8', index=False)
    pages = 2
    for page in range(pages):
        movies_urls=getMoviesUrls(page)
        deal_urls(movies_urls)
