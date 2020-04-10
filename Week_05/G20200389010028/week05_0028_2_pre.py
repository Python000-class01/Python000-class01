import pandas as pd

def get_comments():
    df = pd.read_csv(r'G:\python_advanced\homework\week5\book.csv')
    # 调整格式
    df.columns = ['star', 'comments']
    star_to_number = {
        '力荐' : 5,
        '推荐' : 4,
        '还行' : 3,
        '较差' : 2,
        '很差' : 1
    }
    df['new_star'] = df['star'].map(star_to_number)

    df2 = df[df['new_star'] == 4 ]
    # 取得评论内容  
    return df2['comments'].to_string()


import jieba.analyse
text = get_comments()
stop_words=r'G:\python_advanced\homework\week5\stop_words.txt'
# 过滤掉无用的符号
jieba.analyse.set_stop_words(stop_words)
# 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(text,
topK=10,                   # 权重最大的topK个关键词
withWeight=False) 
tfidf
# ['小霸王', '拉登', '救赎', '惊艳', '字里行间', '不管不顾', '透不过气', '晦涩', '耗时', '超群']