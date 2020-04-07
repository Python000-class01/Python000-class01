import pandas as pd
import jieba.analyse
import pprint
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
plt.switch_backend('qt5agg')
from wordcloud import WordCloud
# from matplotlib.pyplot import imread
# import random


data = pd.read_csv("./comments.csv")
text = ""
for s in data['short']:
    text += s

text_rank = jieba.analyse.extract_tags(text, topK=10, withWeight=False)
pprint.pprint((text_rank))
text_string = ','.join(text_rank)


font = r'/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
wc = WordCloud(
  width = 600,      #默认宽度
  height = 200,     #默认高度
  margin = 2,       #边缘
  ranks_only = None,
  prefer_horizontal = 0.9,
  mask = None,      #背景图形,如果想根据图片绘制，则需要设置
  color_func = None,
  max_words = 20,  #显示最多的词汇量
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
  max_font_size = 200,
  font_path=font)

wc.generate_from_text(text_string)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout()
wc.to_file("comments.png")
plt.show()