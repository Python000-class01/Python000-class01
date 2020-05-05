import requests
import time
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from bs4 import BeautifulSoup as bs


def get_content_html(doban_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {'user-agent': user_agent}
    response = requests.get(
        doban_url,
        headers=header
    )
    html_contents = bs(response.text, 'html.parser')
    return html_contents


def get_book_comment(url):
    comments_top10 = []
    detail_content = get_content_html(url)

    for comments in detail_content.find_all('li', attrs={'class': 'comment-item'}):
        items = comments.find_all('span', attrs={'class': 'short'})
        i = 0
        for comment in items:
            if i < 10:
                comments_top10.append(comment.getText())
            else:
                break
            i += 1
    return comments_top10


def create_wordcloud(comment_list):
    wordlist = jieba.lcut(''.join(comment_list))
    text = ' - '.join(wordlist)
    print(text)
    wordcloud = WordCloud(
        font_path="C:/Windows/Fonts/simkai.ttf",  # 字体需下载到本地，不引入会出现乱码，色彩图块等异常，可替换其他中文字体库
        background_color="white",
        max_font_size=80,
        stopwords=STOPWORDS,
        width=800,
        height=660,
        margin=2, ).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    book_url = 'https://book.douban.com/subject/4913064/comments/'
    start_time = time.time()
    comments = get_book_comment(book_url)
    print(comments)
    create_wordcloud(comments)
    end_time = time.time()
    print("程序耗时 %f 秒!" % (end_time - start_time))
