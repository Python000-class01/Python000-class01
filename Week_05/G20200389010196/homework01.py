from os import path
import jieba.analyse
from matplotlib import pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
dir = path.dirname(__file__)
comments = open(path.join(dir, 'book_comment.txt'),encoding='utf-8').read()

tfidf = jieba.analyse.extract_tags(comments,
topK=10,                   # 权重最大的topK个关键词
withWeight=True)         # 返回每个关键字的权重值
text = ' '.join([w[0] for w in tfidf])
print(text)

background_Image = np.array(Image.open(path.join(dir, 'timg.jpg')))
img_colors = ImageColorGenerator(background_Image)

wc = WordCloud(
  font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",
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

wc.generate_from_text(text)
wc.recolor(color_func = img_colors)

# 显示并存储图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
wc.to_file('跑步谈些什么.png')

plt.show() 