import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from lxml import etree

def get_info(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    html = etree.HTML(response.text)
    ul = html.xpath("//ol[@class='grid_view']")[0]
    lis = ul.xpath("./li")
    for li in lis:
        movie_detail = li.xpath(".//a")[0].attrib['href']
        movie_name = li.xpath(".//span")[0].text
        movie_score = li.xpath(".//span[@class='rating_num']")[0].text
        movie_comment_num = li.xpath(".//span")[len(li.xpath(".//span")) - 2].text.replace('人评价','')
        print(f" movie_detail: {movie_detail} \n movie_name: {movie_name} \n movie_score: {movie_score} \n movie_comment_num: {movie_comment_num}")
        print('###############################################################################################')

urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))

if __name__ == '__main__':
    for url in urls:
        get_info(url)
        sleep(3)