import requests
import lxml.etree
import os
from os import path
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import random
import jieba.analyse

# 爬取页面详细信息

# 图书详细页面
url = 'https://movie.douban.com/subject/34805219/comments?status=P'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent': user_agent}

response = requests.get(url, headers=header)

# xml化处理
selector = lxml.etree.HTML(response.text)
#jieba.enable_paddle()
f = open('douban_move.txt', 'a+', encoding='utf-8')

for i in range(1, 10):
    context = selector.xpath(
        f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()')
    # print(context[0])
    text = jieba.analyse.extract_tags(context[0],topK=5,withWeight=False)
    print(text)
    output = f'{text}\t\n\n'
    f.write(output)
    
f.close()

# 当前文件所在目录
dir = path.dirname(__file__)
# 获取文本text
text = open(path.join(dir, 'douban_move.txt'), encoding='utf-8').read()

# 读取背景图片
background_Image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))

# 提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)

# 生成词云
wc = WordCloud(
    width=600,  # 默认宽度
    height=200,  # 默认高度
    margin=2,  # 边缘
    ranks_only=None,
    prefer_horizontal=0.9,
    mask=background_Image,  # 背景图形,如果想根据图片绘制，则需要设置
    color_func=None,
    max_words=200,  # 显示最多的词汇量
    stopwords=None,  # 停止词设置，修正词云图时需要设置
    random_state=None,
    background_color='#ffffff',  # 背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
    font_step=1,
    mode='RGB',
    regexp=None,
    collocations=True,
    normalize_plurals=True,
    contour_width=0,
    colormap='viridis',  # matplotlib色图，可以更改名称进而更改整体风格
    contour_color='Blues',
    repeat=False,
    scale=2,
    min_font_size=10,
    max_font_size=200,
    font_path="C:\\Windows\\Fonts\\simfang.ttf")

wc.generate_from_text(text)

# 根据图片色设置背景色
wc.recolor(color_func=img_colors)

# 显示图像
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('love.png')

plt.show()

