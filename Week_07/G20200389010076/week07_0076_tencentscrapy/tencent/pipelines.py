# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
from sqlalchemy import create_engine
import requests
import json
import time

class TencentPipeline(object):
    def open_spider(self,spider):
        self.pr_df=pd.DataFrame(columns=['cmtid','comment','time'])

    def process_item(self, item, spider):
        icr_df=pd.DataFrame({
            'cmtid':item['cmtid'],
            'comment':item['comment'],
            'time':item['time']
        })
        self.pr_df=self.pr_df.append(icr_df,ignore_index=True)
        return item

    def close_spider(self,spider):
        engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')
        self.pr_df.drop_duplicates(subset=['comment'], inplace=True)
        self.pr_df.drop(self.pr_df[self.pr_df.comment==''].index,inplace=True)
        self.pr_df.sort_values(by='time',inplace=True)
        comment_list = self.pr_df['comment'].tolist()

        #获取token
        ak = 'MhHHnaEblly9EjPT495j7bZR'
        sk = 'U2lKLPXN2ZgNxqMzUr1TzZQBreBaGUFG'
        url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}'
        resp = requests.post(url)
        dic = json.loads(resp.text)
        token = dic['access_token']

        # 情感分析，以及分词
        sentiment=[]
        sort_sentiment=[]
        div_comment=[]
        for text in comment_list:
            # 情感分析
            sen_url = f'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={token}'
            data = {'text': text}
            data = json.dumps(data)
            time.sleep(0.5)
            sen_resp = requests.post(sen_url, data=data)
            sen_resp = json.loads(sen_resp.text)
            sentiment.append(sen_resp['items'][0]['positive_prob'])
            sort_sentiment.append(sen_resp['items'][0]['sentiment'])
            #分词
            div_url = f'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token={token}'
            time.sleep(0.5)
            div_resp = requests.post(div_url, data=data)
            div_dic = json.loads(div_resp.text)
            s = []
            for i in range(len(div_dic['items'])):
                s.append(div_dic['items'][i]['item'])
                s.extend(div_dic['items'][i]['basic_words'])
            s = set(s)
            div_comment.append('|'.join(s))

        #存数据库
        self.pr_df['sentiment']=sentiment
        self.pr_df['sort_sentiment']=sort_sentiment
        self.pr_df['div_comment']=div_comment
        self.pr_df.to_sql('tencentcomm', engine, index=False,if_exists='append')

