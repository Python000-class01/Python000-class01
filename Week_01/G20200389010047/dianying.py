# coding = utf-8
import requests
from bs4 import BeautifulSoup as bs
import re, csv
from time import sleep



def writeCsv(file, line,write_type):
    out = open(file, write_type, encoding = 'utf-8')
    csv_write = csv.writer(out, dialect = 'excel')
    csv_write.writerow(line)
 
# Python 使用 def 定义函数，myurl 是函数的参数
def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
 
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')
 
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        movie_url = tags.find('a',).get('href')

        movie_name = tags.find('a',).find('span', attrs={'class': 'title'}).text
      
        movie_score = tags.find('span', attrs={'class':'rating_num','property':'v:average'}).text

        movie_score_num = list(map(int, re.findall('\d+',tags.find('div', attrs={'class': 'star'}).find_all('span')[3].text)))[0] 
        response_movie_url = requests.get(movie_url, headers=header)
        bs_info_movie_url = bs(response_movie_url.text, 'html.parser')

        # 取出热评数量
        commeents_num = list(map(int, re.findall('\d+', bs_info_movie_url.find('div', attrs={'class': 'mod-hd'}).  find('span', attrs={'class':'pl'}).text)))[0]
        # 找到热门短评的标签
        hot_commeents = bs_info_movie_url.find('div', attrs={'id':'hot-comments','class':'tab'})

        # 获取热评
        movie_commeents = []
        print(type(movie_commeents))
        for hot_commeents_item in hot_commeents.find_all('span', attrs={'class':'short'}):
            movie_commeents.append(hot_commeents_item.text)

        movie_info = [movie_name,movie_score,commeents_num, movie_commeents[0],movie_commeents[1],movie_commeents[2],movie_commeents[3],movie_commeents[4]]
        writeCsv(csv_file, movie_info,'a')


csv_file= './top250movie.csv'
csv_header = ['电影名称','电影得分','短评数量','热评1', '热评2', '热评3', '热评4', '热评5']
writeCsv(csv_file, csv_header, 'w')


urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

 
 
## 单独执行 python 文件的一般入口
if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(10)
    
