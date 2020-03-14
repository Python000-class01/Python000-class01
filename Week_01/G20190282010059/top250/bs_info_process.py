from bs4 import BeautifulSoup as bs
from re import search
from top250.request_data import request_data
def bs_info_process(bs_info):
    list = []
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        title = tags.find_all('span', attrs={'class': 'title'})[0].contents[0]
        rating = tags.find('span', attrs={'class': 'rating_num'}).contents[0]
        subject_url = tags.find('a').get('href')
        subject = request_data(subject_url)
        subject_bs_info = bs(subject.text, 'html.parser')
        subject_tags = subject_bs_info.find('a', attrs={'href': f'{subject_url}comments?status=P'}).contents[0]
        comment_count = int(search(r'\d+', subject_tags).group())
        comment_top5 = ''
        for comment in subject_bs_info.select('.comment-item .short'):
            comment_top5 = comment_top5 + comment.contents[0] + ';'
        movie = {'title': title, 'rating': rating, 'comment_count': comment_count, 'comment_top5': comment_top5}
        list.append(movie)
    return list
