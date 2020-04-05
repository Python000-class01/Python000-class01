import pandas as pd
import jieba.analyse
from pprint import pprint
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt

df = pd.read_csv('../movei_comment_data/当幸福来敲门800影评.csv')
df = df.dropna()


# 把所有影评拼起来作为一篇文章提取关键词做词云
comments = ''
for c in df.comment_content.values:
    comments += c

# 没有营养的词汇先手动删掉
stop_words=r'./stop_words.txt'
jieba.analyse.set_stop_words(stop_words)


tfidf = jieba.analyse.extract_tags(comments,
topK=20,                   # 权重最大的topK个关键词
withWeight=True)         # 返回每个关键字的权重值
pprint(tfidf)

text = ' '.join([w[0] for w in tfidf])
print(text)

dir = path.dirname(__file__)
background_Image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))
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
wc.to_file('当幸福来敲门.png')

plt.show()