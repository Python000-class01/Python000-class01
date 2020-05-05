
import jieba.analyse
import pprint
import os
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import random


dir = path.dirname(__file__)

text = open(path.join(dir, 'moon.txt'),encoding='utf-8').read()


jieba.del_word('之口')
jieba.del_word('但在')

textrank = jieba.analyse.textrank(text,
topK=10,
withWeight=True)
pprint.pprint(textrank)

# 读取背景图片
background_Image = np.array(Image.open(path.join(dir, 'background.jpg')))

# 提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)

# 生成词云
wc = WordCloud(
  width = 600,      #默认宽度
  height = 200,     #默认高度
  margin = 2,       #边缘
  ranks_only = None,
  prefer_horizontal = 0.9,
  mask = background_Image,
  color_func = None,
  max_words = 200,
  stopwords = None, #
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

wc.generate_from_text(text)
# 根据图片色设置背景色
wc.recolor(color_func = img_colors)
# 显示图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('123.png')
plt.show()