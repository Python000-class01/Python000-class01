from bs4 import BeautifulSoup as bs
from lxml import etree
import pandas as pd
import requests

	
movies_list_url = 'https://movie.douban.com/top250?start=%d'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

article_columns = ['title', 'href', 'cover', 'desc', 'rating_num', 'comments_num', 'quote']
comments_columns = ['article_href', 'author', 'content', 'comment_time', 'votes']


# 通过xpath获取电影列表
def xpath_crawl(url):
    response = send_request(url)
    selector = etree.HTML(response.text)
    items = selector.xpath('//div[@class="item"]')

    data = []
    for item in items:
        #  ? ? ?
        item = etree.tostring(item).decode()
        item = etree.HTML(item)

        cover = item.xpath('//div[@class="pic"]/a/img/@src')[0]
        title = item.xpath('//div[@class="info"]/div[1]/a/span/text()')
        href = item.xpath('//div[@class="info"]/div[1]/a/@href')[0]
        desc = item.xpath('//div[@class="item"]/div[2]/div[2]/p/text()')
        rating_num = item.xpath('//*[@class="item"]/div[2]/div[2]/div/span[2]/text()')[0]
        comments_num = item.xpath('//*[@class="item"]/div[2]/div[2]/div/span[4]/text()')[0]

        quote = item.xpath('//span[@class="inq"]/text()')
        if len(quote) > 0:
            quote = quote[0]

        # 处理空格 \n
        title = ''.join(title).replace(' ', '')
        desc = ''.join(desc).replace('\n', '').replace(' ', '')

        content = [title, href, cover, desc, rating_num, comments_num, quote]
        data.append(content)
    return data


# 通过bs4获取热评
def hot_comments(url):
    response = requests.get(url, headers=headers)
    html = response.text
    soup = bs(html, 'html.parser')
    comments = soup.find('div', id='hot-comments').find_all('div', class_='comment-item')
    data = []
    for item in comments:
        # content = item.find('span', class_='comment-info')
        author = item.find('span', class_='comment-info').find('a').get_text().replace(' ', '')
        comment_time = item.find('span', class_='comment-time ').get_text().replace(' ', '')
        content = item.find('span', class_='short').get_text().replace(' ', '')
        votes = item.find('span', class_='votes').get_text().replace(' ', '')
        comment_info = [url, author, comment_time, content, votes]
        data.append(comment_info)
    return data


# 发送get请求
def send_request(url):
    response = requests.get(url, headers=headers)
    return response


def main():
    data = []
    for page in range(10):
        url = movies_list_url % (page * 25)
        items = xpath_crawl(url)
        data += items
    write_csv('./moves.csv', data, article_columns)


# 写入csv
def write_csv(filename, data, columns=article_columns):
    # 数据导入到csv
    pd_handle = pd.DataFrame(data=data, columns=columns)
    pd_handle.to_csv(filename, mode='a')


if __name__ == '__main__':

    type = input('''
    1.抓取电影列表
    2.抓取电影热评
    ''')

    type = int(type)
    if type == 1:
        main()
    else:
        df = pd.read_csv('./moves.csv', skiprows=1, usecols=[1, 2])
        comments = []
        for move in df.itertuples(index=True, name="Pandas"):
            url = getattr(move, '_2')
            data = hot_comments(url)
            comments += data
        write_csv('./hot_comments.csv', comments, comments_columns)
