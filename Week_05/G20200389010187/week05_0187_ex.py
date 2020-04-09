import requests
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from bs4 import BeautifulSoup as bs


# 获取html内容
def get_content_html(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    html_contents = bs(response.text, 'html.parser')
    return html_contents


# 获取豆瓣书籍详情评论前10条
def get_comments(url):

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


def create_wordcloud(comment_list, font_path):

    wordlist = jieba.lcut(''.join(comment_list))
    text = ' - '.join(wordlist)

    #print(text)
    wc = WordCloud(
        font_path=fontpath,
        background_color="white",
        max_font_size=80,
        stopwords=STOPWORDS,
        width=800,
        height=660,
        margin=2, ).generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    #wc.to_file('wordcloud.png')


if __name__ == '__main__':

    url = 'https://book.douban.com/subject/34911027/comments/'
    fontpath="/System/Library/fonts/PingFang.ttc"

    comments = get_comments(url)

    create_wordcloud(comments, fontpath)