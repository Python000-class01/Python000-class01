import requests
import re
from bs4  import BeautifulSoup as bs
from movie import Movie


def get_comment_url(url):
    return url+"comments?start=0&limit=20&sort=new_score&status=P&percent_type=h"

def get_reponse_BSinfo_by_url(url):
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    header = {}
    header['user-agent']=user_agent
    response = requests.get(url,headers=header)
    bs_info = bs(response.text,"html.parser")
    return bs_info

def get_comment_num(bs_info):
    inner_info =bs_info.find_all('div',attrs={'id':'comments-section'})
    # short_info =inner_info[0].find_all('span',attrs={'class':'short'})
    comment_num = inner_info[0].find('span',attrs={'class':'pl'}).find('a').string
    num=re.search(r'\d+', comment_num).group()
    return num

def get_comment_top5(bs_info):
    comment_details=[]
    # 获取所有短评的div
    inner_info =bs_info.find_all('div',attrs={'class':'comment'})
    # 获取每个div对应短评的点赞数量
    for i in range(5):
        # short_nums =inner_info[i].find('span',attrs={'class':'votes'}).string
        sorted_info=sorted(inner_info, key=lambda info: int(info.find('span',attrs={'class':'votes'}).string), reverse=True) 
        #按照评论热度排序
        comment_detail=sorted_info[i].find('span',attrs={'class':'short'}).string
        comment_details.append(comment_detail)
    return comment_details
   

def get_movie_data_by_url(url): 
    movie_collection = []
    bs_info=get_reponse_BSinfo_by_url(url) 
    infos = bs_info.find_all('div', attrs={'class': 'info'})
    for info in infos:
        movie_title = info.find('a').find('span',attrs={'class': 'title'}).string
        rating_num = info.find('span',attrs={'class':'rating_num'}).string
        inner_url = info.find('a').get('href')
        inner_bs_info=get_reponse_BSinfo_by_url(inner_url)
        comment_num=get_comment_num(inner_bs_info)
        comment_url =get_comment_url(inner_url)
        comment_bs_info = get_reponse_BSinfo_by_url(comment_url)
        comment_details= get_comment_top5(comment_bs_info)
        movie_current  = Movie(movie_title,rating_num,comment_num,comment_details)
        movie_collection.append(movie_current)
    return movie_collection
        
