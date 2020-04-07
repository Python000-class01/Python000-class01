#  from xxx import  xxx   从xx 包  导入 xx 库
import jieba.analyse
import pprint
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from os import path

# 当前文件所在目录
dir = path.dirname(__file__)

# 获取文本text, 已经生成好的关键词
# text = open(path.join(dir, 'shopping.txt'), encoding='utf-8').read()

with open('./contents.text', 'r') as f:
    stop_words = r'stop_words.txt'
    jieba.analyse.set_stop_words(stop_words)
    jieba.suggest_freq('孟晚舟', True)
    #  基于FT-IDF算法进行关键词抽取
    # topK  权重最大的topk 个关键词
    # withweigth 返回每个关键词的权重
    text_list = jieba.analyse.extract_tags(f.read(), topK=10, withWeight=False)

text_string = ','.join(text_list)

# 读取背景图片
background_Image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))
# 提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)


# 中文乱码

font = "/Library/Fonts/Songti.ttc"
# FONT_PATH = os.environ.get('FONT_PATH', path.join(FILE, 'PingFang.ttc'))

# 生成词云
wc = WordCloud(
    width=600,  # 默认宽度
    height=200,  # 默认高度
    margin=2,  # 边缘
    ranks_only=None,
    prefer_horizontal=0.9,
    mask=background_Image,  # 背景图形,如果想根据图片绘制，则需要设置 如果想根据图片绘制，则需要设置
    color_func=None,
    max_words=30,  # 最多显示多少词 显示最多的词汇量
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
    font_path=font)

wc.generate_from_text(text_string)
# 根据图片色设置背景色
wc.recolor(color_func=img_colors)

# 显示图像
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('book.png')

plt.show()
