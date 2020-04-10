import requests
from bs4 import BeautifulSoup as bs
import time
import jieba
from wordcloud import WordCloud, STOPWORDS
from matplotlib import pyplot as plt


# 请求豆瓣
def request_douban(url):
    user_agent = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    header = {}
    header['user-agent'] = user_agent
    try:
        response = requests.get(url, headers=header)
        time.sleep(1)
    except Exception as e:
        raise

    return response


# 获取书评TOP10
def get_reviews_top10(url):
    response = request_douban(url)
    bs_info = bs(response.text, 'html.parser')
    movie_review_list = []
    for review in bs_info.find_all('div', attrs={'class': 'review-list'}):
        for bd in (review.find_all('div', attrs={'class': 'main-bd'})):
            review_url = (bd.find('h2').a['href'])
            resp_review = request_douban(url=review_url)
            bs_info = bs(resp_review.text, 'html.parser')
            for review_content in bs_info.find_all('div', attrs={'class': 'review-content clearfix'}):
                movie_review_list.append(review_content.text)

    return movie_review_list


# 通过Jiaba和WordCloud制作文字云图
def plot_word_cloud(review_content):
    word_list = jieba.lcut(''.join(review_content))
    text = ' - '.join(word_list)
    word_cloud = WordCloud(
        font_path="simkai.ttf",
        background_color="black",
        max_font_size=80,
        stopwords=STOPWORDS,
        width=800,
        height=660,
        margin=2, ).generate(text)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':  # 程序入口
    # 加缪-鼠疫
    requ_url = "https://book.douban.com/subject/24257229/"
    plot_word_cloud(get_reviews_top10(requ_url))
