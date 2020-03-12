import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import lxml.etree as etree
from io import StringIO
import time
import re
import pandas as pd
#
P_HEADLESS = '--headless'
P_USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
P_BASEURL = 'https://movie.douban.com/top250'
P_PAGEQUERYSTR = 'start'
P_PAGESIZE = 25
#
P_XAPTH_TITLE = '//div[@class="item"]/div[@class="info"]/div[@class="hd"]//span[@class="title" and position() = 1]'
P_XPATH_RATING = '//div[@class="item"]/div[@class="info"]//span[@class="rating_num"]'
P_XPATH_COMMENTCNT = '//div[@class="item"]/div[@class="info"]//span[contains(text(),"人评价")]'
P_XPATH_LINK = '//div[@class="item"]/div[@class="info"]/div[@class="hd"]/a[contains(@href,"subject")]'
#
P_XPATH_COMMENT = '//div[@class="comment"]//span[@class="short"]'
P_XPATH_COMMENTTIME = '//div[@class="comment"]//span[@class="comment-time "]'
P_XPATH_COMMENTUSER = '//div[@class="comment"]//span[@class="comment-info"]/a[contains(@href,"people")]'
P_XPATH_COMMENTVOTES = '//div[@class="comment"]//span[@class="votes"]'
#re
P_RE_SUBJECTID = r'https://movie.douban.com/subject/([0-9]*)/'

headers = {'user-agent': P_USERAGENT}
#movie cols
colSubjectId = []
colTitle =[]
colRatingNum = []
colCommentCount = []
colLink = []
#comment cols
colCommentSubjectId = []
colCommentShort = []
colCommentTime = []
colCommentUser = []
colCommentVotes = []

#获取影片数据
def getMovieTop250(pageCount):
    movieCount = 0
    browser = getBrowser()
    try:
        browser.get(P_BASEURL)
        time.sleep(5)
        page = 0
        for page in range(pageCount):
            print(f'begin fetch movies of page {page+1}')
            pageUrl = f'{P_BASEURL}{ "" if page == 0 else f"?{P_PAGEQUERYSTR}={page * P_PAGESIZE}" }'
            fetchMovieList(getResponse(url=pageUrl, cookies=browser.get_cookies()).text)
            time.sleep(2)
        #保存列表
        saveMovieList()
        index = 0
        for link in colLink:
            print(f'begin fetch comment of {index} {colTitle[index]} {link} ')
            fetchMovieComment(colSubjectId[index], getResponse(url=link, cookies=browser.get_cookies()).text)
            index = index + 1
            time.sleep(2)
        #保存评论
        saveMovieComment()
    finally:
        browser.quit()
    return movieCount

# 获取影片列表
def fetchMovieList(pageSource):
    parser = etree.HTMLParser()
    html = etree.parse(StringIO(pageSource), parser)
    colTitle.extend([ el.text for el in html.xpath(P_XAPTH_TITLE)])
    colRatingNum.extend([ el.text for el in html.xpath(P_XPATH_RATING)])
    colCommentCount.extend([ el.text.replace('人评价','') for el in html.xpath(P_XPATH_COMMENTCNT)])
    colLink.extend(links := [ el.attrib['href'] for el in html.xpath(P_XPATH_LINK)])
    colSubjectId.extend([ re.search(P_RE_SUBJECTID, link, re.M|re.I).group(1)  for link in links])
    return

#获取影片热评
def fetchMovieComment(subjectId, pageSource):
    parser = etree.HTMLParser()
    html = etree.parse(StringIO(pageSource), parser)
    shortEls = html.xpath(P_XPATH_COMMENT)
    colCommentShort.extend([el.text.strip().replace('\r','').replace('\n','').replace(',','，') for el in shortEls])
    colCommentSubjectId.extend([subjectId for el in shortEls])
    colCommentTime.extend([el.text.strip() for el in html.xpath(P_XPATH_COMMENTTIME)])
    colCommentUser.extend([el.text.strip() for el in html.xpath(P_XPATH_COMMENTUSER)])
    colCommentVotes.extend([el.text for el in html.xpath(P_XPATH_COMMENTVOTES)])
    return

#保存影片CSV
def saveMovieList():
    df = pd.DataFrame({'subject_id':colSubjectId,
        'title':colTitle,
        'rating_num':colRatingNum,
        'comment_cnt':colCommentCount,
        'link':colLink
    })
    df.to_csv(f'./movie.douban.com_top250.csv')
    return

#保存评论CSV
def saveMovieComment():
    df = pd.DataFrame({'subject_id':colCommentSubjectId,
        'short':colCommentShort,
        'comment_time':colCommentTime,
        'comment_user':colCommentUser,
        'vote':colCommentVotes
    })
    df.to_csv(f'./movie.douban.com_top250_comment.csv')
    return

# 获取response
def getResponse(url, cookies):
    cookieJar = requests.cookies.RequestsCookieJar()
    for item in cookies:
        cookieJar.set(name=item['name'], value=item['value'], secure=item['secure'], 
        rest={'domain':item['domain'], 'path':item['path'], 'httpOnly':item['httpOnly']})
    response = requests.get(url, headers=headers, cookies=cookieJar)
    return  response

#获取浏览器对象
def getBrowser():
    options = Options()
    #options.add_argument(P_HEADLESS)
    browser = webdriver.Firefox(options=options)
    return browser

getMovieTop250(10)
