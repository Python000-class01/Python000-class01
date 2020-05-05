import requests
from lxml import etree
import pandas as pd
import jieba.analyse
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import pprint


header={}
header['user-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"

#获取任意一本书的若干页书评
def book_comments(bookid,n):
    comments=[]
    for i in range(1,n):
        url=f'https://book.douban.com/subject/{bookid}/comments/hot?p={i}'
        response=requests.get(url,headers=header)
        html=etree.HTML(response.text)
        comments_per_page=html.xpath('//span[@class="short"]/text()')
        comments.extend(comments_per_page)
        re_links=html.xpath('//a[@class="page-btn"]/text()')
        if '后一页' not in re_links:
            break
    return comments

# 存成csv文件作为备用
def csv_save(alist):
    df=pd.DataFrame(alist)
    df.to_csv('comments.csv',index=False, header=False)

#获取前10关键字
def top_10(comments):
    content=''.join(comments)
    #设置屏蔽词
    stop_words=r'stop_words.txt'
    jieba.analyse.set_stop_words(stop_words)
    # 基于TF-IDF算法进行关键词抽取
    tfidf=jieba.analyse.extract_tags(content,topK=10,withWeight=True)
    return tfidf

#制作词云图
def bookcomments_wordcloud(tfidf):
    keywords=dict()
    for i in tfidf:
        keywords[i[0]]=i[1]

    
    # 读取背景图片
    background_Image = np.array(Image.open(r'bc_background.jpg'))

    # 提取背景图片颜色
    img_colors = ImageColorGenerator(background_Image)

    # 生成词云
    wc = WordCloud(
        width = 400,      #默认宽度
        height = 400,     #默认高度
        margin = 2,       #边缘
        font_path ='C:\Windows\Fonts\simhei.ttf',
        ranks_only = None, 
        prefer_horizontal = 0.9,
        mask = background_Image,      #背景图形,如果想根据图片绘制，则需要设置    
        color_func = None,
        max_words = 200,  #显示最多的词汇量
        # stopwords = None, #停止词设置，修正词云图时需要设置
        random_state = None,
        background_color = 'white',#背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
        font_step = 1,
        mode = 'RGB',
        regexp = None,
        collocations = True,
        normalize_plurals = True,
        contour_width = 0,
        colormap = 'viridis',#matplotlib色图，可以更改名称进而更改整体风格
        contour_color = 'Blues',
        repeat = False,
        scale = 2,
        min_font_size = 10,
        max_font_size = 200)

    #根据词频生成词云
    wc.generate_from_frequencies(keywords)

    #根据原图生成词云颜色
    wc.recolor(color_func=img_colors)

    # 显示图像
    plt.imshow(wc, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout()
    # 存储图像
    wc.to_file('cute.png')

    plt.show()

if __name__=='__main__':
    comments=book_comments(1858513,50)
    csv_save(comments)
    tfidf=top_10(comments)
    pprint.pprint(tfidf)
    bookcomments_wordcloud(tfidf)


















