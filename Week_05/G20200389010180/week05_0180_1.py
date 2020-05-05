#-*- coding:utf-8 -*-

import requests
import jieba.analyse
import lxml.etree
from time import sleep
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
#import random


def crawl(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    try:
        response = requests.get(url, headers=header, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f'抓取出错：{url}  原因：{e}')

    selector = lxml.etree.HTML(response.text)
    review_urls = selector.xpath('//div[@class="main-bd"]/h2/a/@href')

    reviews_text = []
    for sub_url in review_urls:
        try:
            response = requests.get(sub_url, headers=header, timeout=5)
            response.raise_for_status()
        except Exception as e:
             print(f'抓取出错：{sub_url}  原因：{e}')

        selector = lxml.etree.HTML(response.text)
        text = selector.xpath('//div[@class="review-content clearfix"]//text()')
        reviews_text.append(''.join(text))
        sleep(3)
    
    #print(reviews_text)
    return reviews_text


def get_keyword(text):
    dir = path.dirname(__file__)
    stop_words= path.join(dir,'stop_words.txt')
    jieba.analyse.set_stop_words(stop_words)
    tfidf = jieba.analyse.extract_tags(text,
    topK=50,
    withWeight=False)
    textrank = jieba.analyse.textrank(text,
    topK=50,
    withWeight=False)
    import pprint
    pprint.pprint(tfidf)
    pprint.pprint(textrank)
    return tfidf


def gen_wordcloud(text):
    dir = path.dirname(__file__)
    background_Image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))
    img_colors = ImageColorGenerator(background_Image)

    wc = WordCloud(
    width = 1024,     
    height = 768,    
    margin = 2,      
    ranks_only = None, 
    prefer_horizontal = 0.9,
    mask = background_Image,        
    color_func = None,
    max_words = 200, 
    stopwords = None, 
    random_state = None,
    background_color = '#ffffff',
    font_step = 1,
    mode = 'RGB',
    regexp = None,
    collocations = True,
    normalize_plurals = True,
    contour_width = 0,
    colormap = 'viridis',
    contour_color = 'Blues',
    repeat = False,
    scale = 2,
    min_font_size = 10,
    max_font_size = 200)

    wc.generate_from_text('\n'.join(text)) 
    wc.recolor(color_func = img_colors)
    plt.imshow(wc, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout()
    wc.to_file(path.join(dir,'book_wc.png'))
    plt.show()
    return
    

if __name__=="__main__":
    #<<显微镜下的大明>>
    url = 'https://book.douban.com/subject/30414743/'
    book_reviews = crawl(url)
    keyword = get_keyword('\n'.join(book_reviews))
    gen_wordcloud(keyword)
