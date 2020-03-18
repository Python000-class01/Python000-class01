import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import pandas as pd

urls = ["https://movie.douban.com/top250?start={}".format(i*25) for i in range(10)]

headers = {
    'Connection': 'keep-alive',
    'Host': 'movie.douban.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Cookie': 'll="108090"; bid=gDcumZR8Uss; __yadk_uid=ZEgncmiHPGvYS42M0i7eBPGvu47FUiQ5; __gads=ID=e51b3e101c4e42fd:T=1582686852:S=ALNI_MZtI4NnGWGRLc4GwF9XueHs1vjRuQ; _vwo_uuid_v2=DA37F5F285EAD822DFCC2ED5C115893F3|bb45ada0267ee37116ecdab389eddfb5; viewed="27125805"; gr_user_id=55257b48-d709-479f-abbc-0dd24705ca32; __utmc=30149280; __utmz=30149280.1583741336.4.3.utmcsr=u.geekbang.org|utmccn=(referral)|utmcmd=referral|utmcct=/lesson/8; __utmc=223695111; __utma=30149280.651851016.1582686852.1583741336.1583810356.5; __utmt=1; __utmb=30149280.1.10.1583810356; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1583810356%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.618831049.1582686852.1583741336.1583810356.4; __utmb=223695111.0.10.1583810356; __utmz=223695111.1583810356.4.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; _pk_id.100001.4cf6=7f8d31c9a12b461c.1582686852.4.1583810401.1583745040.'
}

def get_all_urls():
    random.shuffle(urls)
    with open('movie_urls.txt', 'a+') as fp:
        for url in urls:
            print("Parse {}!".format(url))
            retry = 10
            while retry>0:
                response = requests.get(url, headers=headers)
                if response.status_code != 200:
                    retry -= 1
                    sleep(35)
                    continue
                soup = BeautifulSoup(response.text, 'lxml')
                urls_list = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a')
                print("Get total {} conents.".format(len(urls_list)))
                for movie_url in urls_list:
                    fp.write(movie_url.get('href')+'\n')
                sleep(60)
                retry = 0


def get_movie_info(url):
    retry = 10
    while retry>0:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                retry -= 1
                sleep(30)
                if retry==0:
                    return None
                continue
            soup = BeautifulSoup(response.content, 'lxml')
            title = soup.select_one('#content > h1 > span').get_text()
            print(title)
            rate =  soup.select_one("#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong").get_text()
            hot_short_comments = " "
            for comment in soup.select("#hot-comments > div > div > p > span"):
                hot_short_comments += comment.get_text() + " "
            return (title, rate, hot_short_comments)
        except requests.exceptions.TooManyRedirects as e:
            print("Error: ", e)
            return None
        except requests.exceptions.ProxyError as e:
            print("Error: ", e)
            return None
        except requests.exceptions.ConnectionError as e:
            print("Error: ", e)
            return None


if __name__ == "__main__":
    urls_fp = open('movie_urls.txt', 'r', encoding='utf-8')
    all_urls = set(url.strip() for url in urls_fp)
    if len(all_urls)<250:
        get_all_urls()

    crawled_fp = open('crawled_urls.txt', 'r', encoding='utf-8')
    crawled_urls = set(url.strip() for url in crawled_fp)
    movie_info_fp = open('movie_info.txt', 'a+', encoding='utf-8')
    crawled_fp_w = open('crawled_urls.txt', 'a+', encoding='utf-8')
    urls = all_urls - crawled_urls
    for url in urls:
        movie_info = get_movie_info(url.strip())
        if movie_info is not None:
            title, rate, hot_comments = movie_info
            movie_info_fp.write('[start]' + str(title)+'[m]' +str(rate) + '[m]' + str(hot_comments) + '[end]\n')
            crawled_fp_w.write(url+'\n')
        sleep(30)
    movie_info_fp.close()
    crawled_fp.close()
    crawled_fp_w.close()
    urls_fp.close()

    if len(crawled_urls) == 250:
        movie_df = pd.DataFrame(columns=['Title', 'Rate', 'Hot short comment'])
        tmp_str = ""
        with open("movie_info.txt", "r", encoding="utf-8") as fp:
            for line in fp:
                if line.strip():
                    tmp_str += line
                if '[end]' in line.strip():
                    tmp_str = tmp_str.split("[start]")[1].split("[end]")[0]
                    title, rate, comments = tmp_str.split('[m]')
                    movie_df = movie_df.append(pd.DataFrame([[title, rate, comments]], columns=['Title', 'Rate', 'Hot short comment']))
                    tmp_str = ""
        movie_df.to_csv("douban_top250_movie.csv", encoding='utf_8_sig', index=False)