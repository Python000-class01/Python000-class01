# 作业一：
# 使用 jieba 对豆瓣中任意一本书评或影评提前 top10 关键词，并绘制词云。

import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
import jieba.analyse
from os import path

dir = path.dirname(__file__)
text = open(path.join(dir, 'bwbj1.txt'),encoding='utf-8').read()
user_dict=r'dict.txt'
jieba.load_userdict(user_dict)

stop_words=r'stop.txt'
jieba.analyse.set_stop_words(stop_words)

tfidf = jieba.analyse.extract_tags(text,
topK=15,
withWeight=False)

print(tfidf)
file = open('bwbj.txt','w')
for i in range(len(tfidf)):
  s = str(tfidf[i]).replace('[','').replace(']','')
  s = s.replace("'",'').replace(',','') +'\n'
  file.write(s)
file.close()
print("保存关键词")


cizu = open(path.join(dir, 'bwbj.txt'),encoding='GBK').read()
background_Image = np.array(Image.open(path.join(dir, 'shaor.png')))
img_colors = ImageColorGenerator(background_Image)
wc = WordCloud(
  width = 600,      #默认宽度
  height = 200,     #默认高度
  margin = 2,       #边缘
  ranks_only = None,
  prefer_horizontal = 0.9,
  mask = background_Image,      #背景图形,如果想根据图片绘制，则需要设置
  color_func = None,
  max_words = 200,  #显示最多的词汇量
  stopwords = None, #停止词设置，修正词云图时需要设置
  random_state = None,
  background_color = '#ffffff',#背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
  font_step = 1,
  font_path='msyh.ttf',
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

wc.generate_from_text(cizu)
# 根据图片色设置背景色
wc.recolor(color_func = img_colors)
# 显示图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('love.png')
plt.show()
