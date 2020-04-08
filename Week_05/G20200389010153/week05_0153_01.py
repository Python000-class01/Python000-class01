import jieba.analyse
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import os

comment = [
    '感觉像是《斯通纳》的翻版，只是没想到这样的知识分子生活能以漫画的形式呈现出来。主角和斯通纳不无相似之处：对他们而言，只有一个世界是不够的，都需要alternative生活；无时无刻的自我质疑、自我审视倾向，但某些信念又坚定到顽固的地步；与现实生活格格不入，无法过那种不假思索的日子。不过有所不同的是，他比斯通纳幸福，遇到了另一个异类，并最终通过她反思了自己，对这类人来说，这差不多就是救赎。当然，即便在美国，能过这样日子的可能也是纽约、加州之类“象牙塔飞地”中的少数，但这种生活至少是可欲也可能的。 ',
    '一本关于人生的书。关于人生的荒谬、虚无、痛苦、幸福都可以在本书中找到。叙事结构精妙，变成小说应该也是杰作，但是漫画的形式最能成全这个故事。画面和用色极具设计感，作者在书中埋下了无数细节和隐喻等着读者去发现。最喜欢的角色是神神叨叨的乌尔苏拉，其实她看穿了所有世间的荒谬，但仍然能和当下相处泰然。',
    '这是一个带有实验性的作品，不论是用色，还是情节，而且可能一些小朋友未必有兴趣，因为这个故事说的是一个中年男人的事情，可以说作者很到位的描述了人到中年，对某些事情的眷恋，对很多事物的厌倦，最好玩的是，它不是常规的漫画故事，它几乎是图像的小说，这点当你看到结尾的时候，你就能发现作者不是漫画家而是小说家。他给出的结尾真的是让人又好气又好笑，带着戏谑和讽刺，像极了生活和爱情。',
    '一个伍迪·艾伦式的爱情故事，中间夹杂了很多哲学、艺术、历史、希腊神话的桥段或细节。而主人公是一个没有任何建筑作品的建筑师，常常陷入身份认同危机（他有一个出生时便夭折的双胞胎兄弟），这些设定本身就很有意味……国外的图像小说都已经写成了“书之书”，真是令人唏嘘啊。']

hotwords = jieba.analyse.extract_tags(
    ' '.join(comment), topK=10, withWeight=False)
print(hotwords)

text_string = ','.join(hotwords)

FILE = os.path.dirname(__file__)
print(FILE)
FONT_PATH = os.environ.get('FONT_PATH', os.path.join(FILE, 'PingFang.ttc'))
print(FONT_PATH)
wc = WordCloud(
    font_path=FONT_PATH,
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

wc.generate_from_text(text_string)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('book.png')

plt.show()
