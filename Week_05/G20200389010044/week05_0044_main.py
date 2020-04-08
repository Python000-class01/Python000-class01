from GetComments import getcomments, setup_io
from GenerateKeywords import generateKeywords
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import random
from os import path

# 1. 获取数据集

setup_io()
# url为指定图书的短评首页 - getcomment()将抓取全部短评数目然后生成urls列表抓取所有短评作为结果返回
url = "https://book.douban.com/subject/10554308/comments/"
comments = getcomments(url)

# 2. 数据预处理
# 数据集只有一列且十分规整，不需要进行预处理部分

# 3. 分词 & 提取关键词
text = "。".join(comments)
keywordsNum = 50
keywords = generateKeywords(text, keywordsNum)
# print(keywords)

# 4. 生成词云

text_string = ','.join(keywords)
# 当前文件所在目录
dir = path.dirname(__file__)
# 读取背景图片
background_Image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))
# 提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)
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

# 根据图片色设置背景色
wc.recolor(color_func = img_colors)


# 显示图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('book.png')

plt.show()