import jieba.analyse
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread

file_nm = 'book_comment.txt'
text = open(file_nm,"r",encoding="utf-8").read()

# # 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(text,
topK=5,                   # 权重最大的topK个关键词
withWeight=False)         # 返回每个关键字的权重值

# import pprint             # pprint 模块提供了打印出任何Python数据结构的类和方法
# pprint.pprint(tfidf)


text_string = ','.join(tfidf)

# 生成词云
wc = WordCloud(
  width = 600,      #默认宽度
  height = 200,     #默认高度
  margin = 2,       #边缘
  ranks_only = None, 
  prefer_horizontal = 0.9,
  mask = None,      #背景图形,如果想根据图片绘制，则需要设置    
  color_func = None,
  max_words = 200,  #显示最多的词汇量
  stopwords = None, #停止词设置，修正词云图时需要设置
  random_state = None,
  background_color = '#ffffff',#背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
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

wc.generate_from_text(text_string)


# 显示图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('book.png')

plt.show()
