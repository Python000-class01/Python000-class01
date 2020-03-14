import requests
import lxml.etree
from pandas import DataFrame
from time import sleep


# 獲取每部電影的名字(movie_nm)、分數(rating)、短評數(cmt_cnt)和前五熱門短評(cmt_tp5)
def get_movie_info(url):
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    movie_nm = selector.xpath('//h1/span[1]/text()')
    rating = selector.xpath("//strong[@class='ll rating_num']/text()")
    cmt_cnt = [selector.xpath('//header/h2/span/a/text()')[0].split(' ')[1]]
    cmt_tp5 = [selector.xpath('//*[@id="hot-comments"]/div//p/span/text()')]
    movie_info = movie_nm + rating + cmt_cnt + cmt_tp5
    return movie_info


# 獲取每部電影的專頁網址(movie_url)
def get_movie_url(url):
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    movie_url = selector.xpath('//li//div[2]/div[1]/a/@href')
    movie_info_lst = [get_movie_info(i) for i in movie_url]
    return movie_info_lst


# user agent
header = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


if __name__ == '__main__':    
    movie_info_lst = []
    # initial page number
    page_num = 0
    while page_num <= 225:
        page = (f'https://movie.douban.com/top250?start={page_num}&filter=')
        page_num += 25
        movie_info_lst += get_movie_url(page)
        sleep(2)
    # list轉為DF再存成csv
    movie_info_df = DataFrame(movie_info_lst, columns=['movie_nm', 'rating', 'cmt_cnt', 'cmt_tp5'])
    movie_info_df.to_csv('C:/Users/10802118/Desktop/ForTest/Result_final.csv', encoding='utf-8')