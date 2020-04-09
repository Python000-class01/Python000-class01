#coding=utf-8
import jieba.analyse
import pprint
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import numpy as np
from PIL import Image
from os import path

# comment = '太好看！曹雪芹好叛逆。本以为会很闷，没想到读起来这么顺畅轻松。如果没有续书，元妃薨逝后的情节实在是压抑阴暗的让人绝望。最喜欢探春惜春，一个伶俐果断，一个能舍能断不牵三挂四。喜欢王熙凤，聪明利落，也挺善良。读完之后觉得金玉良缘不是个好词，象征着妥协草率、委屈不甘、凑合将就、平庸苦闷。宝玉从没爱过薛宝钗，也决不会爱上她，宝钗也没真爱过贾宝玉，不过是逆来顺受嫁到哪算哪，嫁到谁家她都会像如今这样持家有方周到圆滑的。金玉良缘，我真不羡慕。我一定会选林黛玉。她是真懂宝玉的，跟宝玉一样都是那种心无挂碍一门心思堂堂正正的想着谈恋爱的，不被俗事功名缠扰。跟黛玉在一起，生活不会无聊。红楼梦当中的真爱，那些纯粹干净的暧昧几乎都是同性之间的。我自己觉得宝姐姐可能是喜欢林黛玉的，那份周到体贴。贾宝玉真是难得的极品。'
comment = '盛衰之理，本为天命。然而人心就是如此。眼见得他起高楼，于是便不忍心见他楼塌了。见过他鼎盛的时候，再看他的衰败就无比心酸。而更加可悲的是，目睹这场哗变的你，本就是这戏中之人。'

jieba.add_word('戏中之人')

# 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(comment, topK=10, withWeight=False)
pprint.pprint(tfidf)

top_word = ','.join(tfidf)
#print(top_word)

# 获取背景图片
dir = path.dirname(__file__)
background_image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))
image_colors = ImageColorGenerator(background_image)

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

wc.generate_from_text(top_word)

# 根据图片设置背景色
wc.recolor(color_func=image_colors)

# 显示图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('comment_wordcloud.png')

plt.show()

  
