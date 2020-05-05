import jieba
from jieba import analyse as ae

with open('E:\\PycharmProjects\\myjieba\\pj.txt', encoding='utf-8') as f:
    pj = f.read()

stopwords = "E:\\PycharmProjects\\myjieba\\stop.txt"
ae.set_stop_words(stopwords)
textrank = ae.extract_tags(pj,topK=10,withWeight=False)


