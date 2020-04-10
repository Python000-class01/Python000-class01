import jieba
import jieba.analyse
import pprint             # pprint 模块提供了打印出任何Python数据结构的类和方法

def generateKeywords(text, keywordsNum):
    stop_words=r'stop_words.txt'
    # stop_words 的文件格式是文本文件，每行一个词语
    jieba.analyse.set_stop_words(stop_words)

    # 基于TF-IDF算法进行关键词抽取
    tfidf = jieba.analyse.extract_tags(text,
    topK=keywordsNum,         # 权重最大的topK个关键词
    withWeight=False)         # 返回每个关键字的权重值
    return tfidf

if __name__ == '__main__':
    text = '机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，如果从头到尾开始学，估计大部分人来不及，我建议先学习最基础的数学知识'
    keywordsNum = 5
    tfidf = generateKeyword(text, keywordsNum)
    pprint.pprint(tfidf)