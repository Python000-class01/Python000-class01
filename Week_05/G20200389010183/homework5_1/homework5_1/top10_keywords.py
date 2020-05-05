import jieba.analyse
import pprint
from wordcloud import WordCloud
from os import path


def gene_word_cloud(_text):
    font = "/System/Library/fonts/PingFang.ttc"
    wc = WordCloud(
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
        font_path=font,
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

    wc.generate_from_text(_text)

    # 存储图像
    wc.to_file('饥饿站台top10关键词textrank.png')


if __name__ == '__main__':
    dir = path.dirname(__file__)
    # 获取文本text
    # text = open(path.join(dir, 'shopping.txt'), encoding='utf-8').read()
    file_path = path.join(dir, 'comments/comments.txt')
    with open(file_path, 'r') as f:
        text = f.read()
        stop_word_path = path.join(dir, 'jieba_config/stop_words.txt')
        jieba.analyse.set_stop_words(stop_word_path)
        # 基于TF-IDF算法进行关键词抽取
        # topN = jieba.analyse.extract_tags(text,
        #                                    topK=10,  # 权重最大的topK个关键词
        #                                    withWeight=False)
        topN = jieba.analyse.textrank(text,
                                          topK=10,  # 权重最大的topK个关键词
                                          withWeight=False)
        pprint.pprint(topN)
        gene_word_cloud(','.join(topN))
