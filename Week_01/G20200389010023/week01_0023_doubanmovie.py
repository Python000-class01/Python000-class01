import requests
from bs4 import BeautifulSoup
import time
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

def get_detailulrs(url):
    resp = requests.get(url,headers=headers).text
    soup = BeautifulSoup(resp,'lxml')
    lis = soup.find('ol',class_='grid_view').find_all('li')
    detail_urls = []
    for li in lis:
        detail_url = li.find('a')['href']
        detail_urls.append(detail_url)
    return detail_urls

def get_detailcontents(url):
    resp = requests.get(url, headers=headers).text
    soup = BeautifulSoup(resp, 'lxml')
    hot_comments = ""
    contents_list = []
    film_name = soup.find('span',property="v:itemreviewed").text
    film_score = soup.find('strong',property="v:average").text
    len_comments = soup.find('div',class_="mod-hd").h2.span.a.text
    comments = soup.find_all('div',class_="comment")
    for comment in comments:
        hot_comments += comment.find('span',class_="short").text + "\n"
    contents_list.append([film_name,film_score,len_comments,hot_comments])
    return contents_list

def write_to_csv(content_list,f):
    columns = ['film_name','film_score','len_comments','hot_comments']
    data = content_list
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(data)

def main():
    base_url = "https://movie.douban.com/top250?start={}&filter="
    with open("movie_top250.csv","w",encoding="utf-8") as f:
        for i in range(0,226,25):
            url = base_url.format(i)
            detail_urls = get_detailulrs(url)
            for detail_url in detail_urls:
                contents_list = get_detailcontents(detail_url)
                time.sleep(5)
                write_to_csv(contents_list,f)

if __name__ == "__main__":
    main()
