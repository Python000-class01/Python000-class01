import jieba.analyse
import pprint
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path
from matplotlib import pyplot as plt

cinecism = '菜刀老头代表的是利己的现实主义者、保守派。后来变成男主脑中的声音，多代表人性自私的一面。' \
           '宠物女代表的是利他的浪漫主义者、但不是自由派，更接近改良派。变成男主脑中的声音后，更多的代表的是理性的发声。' \
           '亚裔女，含义很复杂，既暗喻了宗教上的圣母，主动下沉底层“牺牲自我利益”去寻找“孩子”，算是血腥版玛利亚。另一方面，又代表了激进的革命先锋，并不被保守派、改进派所认同，甚至认为她的“孩子”不存在是个纯粹搅乱制度的疯子。另外她也代表了命运与变数——即便你知足的呆在你的那个阶层，依然有外来事件和力量让你失去本就不富足的生活。' \
           '绳子黑人队友，代表理想主义者，很像各个历史事件里的“学生”，简单、真诚、觉得凭借一己之力可以改变世界，但也容易被骗被煽动。其次，也是跨越阶级的人，但面对上层阶级关闭上升通道后，选择推翻这个游戏规则。 ' \
           '轮椅老头，扮演的智者的角色，一眼看过去仿若甘地再世，其建议也非常具有“非暴力，不合作”的几分神采。而提出“信息”这个建议则是对应的男主他们应该有自己的政治诉求，虽然变革本身掺杂着暴力，但与纯粹恐怖主义的暴力宣泄不同之处，就在于暴力和混乱是阶段性手段而不是目的。' \
           '每个进入监狱坑的人带的东西，代表了他的为人、社会属性、职业或阶层。' \
           '综上所述，男主开始代表的是知识分子理论派，偏自由派，对应现实差不多就是中产或知识中产，受过良好教育有一定社会地位但不是顶层分配者。被现实鞭打了几回合后上升到了6层变为决策层，成为了真正的舍身取义的革命家和社会实践家。' \
           '升到第六层然后下沉的过程中：' \
           '拉屎的第五层代表了占据资源却耽于声色道德沦丧的权贵阶级，可对标故宫大G女。' \
           '前50层，男主只是要求他们放弃一顿却被各种拒绝的人，代表了在变革中不愿出让权益的既得利益阶层与团体。（实例太多说了要被封号）' \
           '50层之后，就是韭菜大赏，有遵守男主新制度的拥簇者（只吃自己份量）；有沉湎于娱乐麻痹自己的人（泡在游泳池里等别人扔西瓜才去吃）；也有借机讨要更多的投机者（与男主一伙言论争抢）；还有想窃取gm果实的强盗（与男主他们大打出手）；甚至更多在男主他们出现之前就已经进行了自我消灭的人。' \
           '而愈往下愈悲惨，说明制度的不合理造成的悲剧，不是个人的善恶选择或道德的约束就可以避免的。' \
           '最后出的小女孩，那个亚裔女本不该存在的“孩子”，对应的是先锋者不被当下所理解的追求。而男主所要传达的信息，是舍身取义的“义”。' \
           '这个“义”是什么，各花入各眼，每个人都会有自己的见解。我的理解是人性所存的最后一丝善意，剥去财富、阶级、种族、外貌这一切之后，生为生命平等活着的权利。' \
           '男主走下餐台，意味着享受革命果实的，是未来是下一代。变革的漫长往往需要一代人的牺牲。也对应耶稣为众人牺牲自我的宗教寓意。'

words = jieba.analyse.extract_tags(cinecism, topK=10, withWeight=False)
print(words)
pprint.pprint(words)

# 当前文件所在目录
dir = path.dirname(__file__)
print(dir)

# 读取背景图片
background_Image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))

# 提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)

# 生成词云
wc = WordCloud(
    width=600,  # 默认宽度
    height=200,  # 默认高度
    margin=2,  # 边缘
    ranks_only=None,
    prefer_horizontal=0.9,
    mask=background_Image,  # 背景图形,如果想根据图片绘制，则需要设置
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

text = ','.join(words)
print(text)

wc.generate_from_text(text)

# 根据图片色设置背景色
wc.recolor(color_func = img_colors)

# 显示图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('love.png')

plt.show()
