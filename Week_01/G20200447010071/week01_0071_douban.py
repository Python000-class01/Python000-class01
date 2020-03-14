import requests
from bs4 import BeautifulSoup


class Douban():

    def __init__(self):
        self.urls = ["https://movie.douban.com/top250?start=" + str(start * 25) for start in range(10)]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36 "
        }


    # 初始化CSV文件
    def initCSVFile(self):
        print("初始化CSV文件")
        with open('douban.csv', 'w', encoding='utf-8-sig') as f:
            f.write('电影名称,评分,评论数量,前五个评分')


    # 获取数据
    def getData(self, url):
        try:
            res = requests.get(url, headers=self.headers)
            self.parseData(res.text)
        except Exception as e:
            print(e)

    # 解析数据
    def parseData(self, data):
        parse_data = BeautifulSoup(data, 'html.parser')
        items = parse_data.find_all('div', attrs={"class": "item"})
        for item in items:
            titles = item.find_all('span', attrs={"class": "title"})
            if len(titles) > 1:
                sub_title = titles[1].text.replace(" / ", "")
                title = "{}({})".format(titles[0].text, sub_title)
            else:
                title = titles[0].text
            score = item.find('span', attrs={"class": "rating_num"}).text
            url = item.find('a').get('href')
            comment = self.getComment(url)
            with open('douban.csv', 'a', encoding='utf-8-sig') as f:
                f.write("\r\n")
                f.write("{},{},{},{}".format(title, score, comment["total"], ','.join([content.replace(',', '，').replace('\r', '').replace('\n', '') for content in comment["hot_comments"]])))
            print(title, score, comment["total"], [content for content in comment["hot_comments"]])

    # 获取评论
    def getComment(self, url):
        try:
            data = requests.get(url, headers=self.headers).text
            parse_data = BeautifulSoup(data, "html.parser")
            comment = parse_data.find("div", attrs={"id": "comments-section"})
            comment_total = comment.find("div", attrs={"class": "mod-hd"}).find_all("a")[1].text[3:-2]
            comment_contents = comment.find_all("span", attrs={"class": "short"})
            comment_contents = map(lambda comment_content: comment_content.text, comment_contents)
            if comment_total == 0:
                return self.getComment(url)
            return {
                "total": comment_total,
                "hot_comments": comment_contents
            }
        except Exception as e:
            print(e)

    def run(self):
        self.initCSVFile()
        for url in self.urls:
            self.getData(url)


if __name__ == "__main__":
    douban = Douban()
    douban.run()
