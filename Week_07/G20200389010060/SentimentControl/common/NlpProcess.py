from common.DbUtil import ConnDB, newsCommentDbInfo, nlpCommentDbInfo
from snownlp import SnowNLP
import jieba.analyse

stop_words=r'./stop_words.txt'
jieba.analyse.set_stop_words(stop_words)

class NewsCommentNlpProcess:
    # 单个文本进行情感分析
    def get_sentiments(self, text):
        s = SnowNLP(text)
        return s.sentiments

    # 数据库所有内容进行nlp处理
    def nlp_all_db_data(self):
        cmd = f'select user_name, content, time_stamp from {newsCommentDbInfo["table"]}'
        db = ConnDB(newsCommentDbInfo, [cmd])

        cmds = [f'create table if not exists {nlpCommentDbInfo["table"]} (content varchar(3000) character set utf8, user_name varchar(200) character set utf8, time_stamp varchar(100), score double, positive bool, keywords varchar(3000), primary key(user_name, time_stamp)) default charset=utf8']
        print(db.result)
        for user_name, content, time_stamp in db.result[0]:
            score = self.get_sentiments(content)
            print(f'nlp process result: {user_name} {time_stamp} {score}')
            is_positive = score >= 0.8

            tfidf = jieba.analyse.extract_tags(content,
                                               topK=300,  # 权重最大的topK个关键词
                                               withWeight=True)  # 返回每个关键字的权重值
            print(tfidf)

            keywords = ','.join([w[0] for w in tfidf])
            cmds.append(f'replace into {nlpCommentDbInfo["table"]} (user_name, content, time_stamp, score, positive, keywords) values ("{user_name}", "{content}", {time_stamp}, {score}, {"true" if is_positive else "false"}, "{keywords}")')

        # 建表并插入数据
        print(f'inserting nlp data to {nlpCommentDbInfo["table"]}')
        db = ConnDB(newsCommentDbInfo, cmds)
        print('inserting nlp data over')


if __name__ == '__main__':
    nlp = NewsCommentNlpProcess()
    nlp.nlp_all_db_data()