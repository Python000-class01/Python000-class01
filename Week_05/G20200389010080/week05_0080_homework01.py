import jieba.analyse
from wordcloud import WordCloud
from matplotlib import pyplot as plt


comment = [
    '不努力工作会变成猪'
    ,
    '你忘了吗? 往下飞的时候眼泪是往上流的.'
    ,
    '十年后重看只想大哭，其实我们都明白这个结局。'
    ,
    '一个寻找自我或者自我复苏的过程'
    ,
    '欲望无限，就会让你失去自己，进而痛失所爱；在残酷的环境下，只有努力去适应并寻求改变，才能有突破的可能；成功路人，伯乐很重要，一定要记得感恩；奋斗途中，会有妖魔鬼怪，也有可爱温暖的无脸男和小白。节制欲望、不断进阶、知世故而不世故、做个善良有温度的人。千寻，你是最棒的！']

qyqx = jieba.analyse.extract_tags(' '.join(comment), topK=10, withWeight=False)
print(qyqx)

text_string = ','.join(qyqx)


wc = WordCloud(
    # font_path='/System/Library/fonts/PingFang.ttc',
    width=600,  # 默认宽度
    height=200,  # 默认高度
    margin=2,  # 边缘
    ranks_only=None,
    prefer_horizontal=0.9,
    mask=None,  # 背景图形,如果想根据图片绘制，则需要设置
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
    max_font_size=200)

dx = wc.generate_from_text(text_string)


plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('movie.png')

print(plt.show())