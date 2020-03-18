import requests
import lxml.etree
import time
import pandas

#电影集合
movieObjList = []
movieCsvList = []

url = 'https://movie.douban.com/top250'
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

resp = requests.get(url, headers = header)
selector = lxml.etree.HTML(resp.text)

movieNames = selector.xpath('//span[@class="title"][1]/text()')
ratintNums = selector.xpath('//span[@class="rating_num"][1]/text()')
links = selector.xpath('//div[@class="item"]//a/@href')
ratingPersonNums = selector.xpath('//div[@class="star"]/span[4]/text()')
ratingPersonNums = [each[0:len(each)-3] for each in ratingPersonNums]

#总条数
count = selector.xpath('//div[@class="paginator"]//span[@class="count"]/text()')
count = count[0][2:len(count[0])-2]

#页数和每页数量
pageSize = len(movieNames)
pageNum = int((int(count)/pageSize))

i = 1
while pageSize > 0 and i < pageNum:
    url = 'https://movie.douban.com/top250?start='+str(pageSize*i)
    resp = requests.get(url, headers = header)
    selector = lxml.etree.HTML(resp.text)

    movieNames = selector.xpath('//span[@class="title"][1]/text()')
    ratintNums = selector.xpath('//span[@class="rating_num"][1]/text()')
    links = selector.xpath('//div[@class="item"]//a/@href')
    ratingPersonNums = selector.xpath('//div[@class="star"]/span[4]/text()')
    ratingPersonNums = [each[0:len(each)-3] for each in ratingPersonNums]

    for i in range(pageSize):
        movieObj = {}
        movieObj["movieName"] = movieNames[i]
        movieObj["ratingNum"] = ratintNums[i]
        movieObj["ratingPersonNum"] = ratingPersonNums[i]
        resp = requests.get(links[i], headers = header)
        selector = lxml.etree.HTML(resp.text)
        comment = selector.xpath('//div[@class="comment"]//span[@class="short"]/text()')
        movieObj["comment"] = comment
        movieObjList.append(movieObj)

        movieCsvList.append([movieObj["movieName"], movieObj["ratingNum"], movieObj["ratingPersonNum"], movieObj["comment"]])
        time.sleep(2)
    
movieFile = pandas.DataFrame(columns=['电影名称', '评分', '评分人数', '评价top5'], data = movieCsvList)
movieFile.to_csv('./movieFile.csv', encoding='utf-8')