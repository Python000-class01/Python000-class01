# -*- coding: utf-8 -*-

import csv
import jieba
import jieba.analyse
from wordcloud import WordCloud
import os


def extract_keywords(sentence):
    # print(sentence)
    keywords = jieba.analyse.extract_tags(
        sentence, topK=50, withWeight=True, allowPOS=('n',))
    #print("Keywords: ", keywords)
    kw_dict = dict(keywords)
    print(kw_dict)
    return kw_dict


def generate_wordcloud(word_dict):
    wordcloud = WordCloud(background_color="white",
                          font_path=r"/System/Library/fonts/PingFang.ttc",
                          width=1000, height=860, margin=2).generate_from_frequencies(word_dict)
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    file_path = os.path.dirname(
        os.path.realpath(__file__)) + "/review_text.csv"
    sen = []
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for line in csv_reader:
            sen.append(line[0])

    keywords = extract_keywords("".join(sen))
    generate_wordcloud(keywords)
