import jieba.analyse


with open('./wenben.text', 'r') as f:
    #  基于FT-IDF算法进行关键词抽取
    # topK  权重最大的topk 个关键词
    # withweigth 返回每个关键词的权重
    tfidf = jieba.analyse.extract_tags(f.read(),
                                       topK=5,  # 权重最大的topK个关键词
                                       withWeight=False)  # 返回每个关键字的权重值

    # 基于TextRank算法进行关键词进行抽取
    # 权重最大的topK个关键词
    # 返回每个关键字的权重值
    textrank = jieba.analyse.textrank(f.read(),
                                      topK=5,  # 权重最大的topK个关键词
                                      withWeight=False)  # 返回每个关键字的权重值

# pprint 模块提供了打印出任何Python数据结构的类和方法
import pprint

pprint.pprint(tfidf)
pprint.pprint(textrank)
