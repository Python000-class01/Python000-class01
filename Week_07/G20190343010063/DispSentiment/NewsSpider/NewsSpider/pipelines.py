# -*- coding: utf-8 -*-

import pandas as pd

from common.DbUtil import ConnDB, newsCommentDbInfo, pickCntDbInfo


class Hour24HotmovierrysPipeline(object):

    def open_spider(self, spider):
        self.df = pd.DataFrame(columns=['user_name', 'time_stamp', 'comment_content'])

    # 对新闻评论数据进行存库
    def save_db(self):
        print(f'spider saving data to {newsCommentDbInfo["table"]}')

        commands = []
        commands.append(f'create table if not exists {newsCommentDbInfo["table"]} (content varchar(3000) character set utf8, user_name varchar(200) character set utf8, time_stamp varchar(100), primary key(user_name, time_stamp)) default charset=utf8')

        for i in range(self.df.shape[0]):
            line = self.df.iloc[i]
            #print(line.user_name, line.time_stamp, line.comment_content)
            commands.append(f'insert ignore into {newsCommentDbInfo["table"]} (content, user_name, time_stamp) values ("{line.comment_content}", "{line.user_name}", {line.time_stamp})')
        db = ConnDB(newsCommentDbInfo, commands)

        # 将采集的数据量进行存库
        commands = []
        commands.append(
            f'create table if not exists {pickCntDbInfo["table"]} (id int not null auto_increment, pick_cnt int, primary key(id)) default charset=utf8'
        )

        commands.append(
            f'select pick_cnt from {pickCntDbInfo["table"]}'
        )
        print(commands)

        db = ConnDB(pickCntDbInfo, commands)
        cnts = []

        print(f'result is {db.result}')
        for cnt in db.result[1]:
            cnts.append(cnt[0])

        if len(cnts) < 6:
            cnts.append(self.df.shape[0])
        else:
            cnts = cnts[1:]
            cnts.append(self.df.shape[0])

        commands = []
        commands.append(
            f'truncate table {pickCntDbInfo["table"]}'
        )

        for cnt in cnts:
            commands.append(
                f'insert into {pickCntDbInfo["table"]} (pick_cnt) values ({cnt})'
            )
        print(commands)

        db = ConnDB(pickCntDbInfo, commands)


        print(f'saving db over, threre are totally {self.df.shape[0]} records')

    # 对新闻评论数据进行简单清洗
    def clean_data(self):
        # 同一个用户同一时间发布的重复评论只保留一条
        self.df.drop_duplicates(['user_name', 'time_stamp'])

        self.df.user_name.fillna('unknown', inplace=True)
        self.df.dropna(subset=['comment_content'], inplace=True)
        self.df.time_stamp.fillna(0, inplace=True)

    def close_spider(self, spider):
        self.clean_data()
        self.save_db()

        #print(self.df)

    def process_item(self, item, spider):
        #print('process_item', item['user_name'], item['comment_content'], item['time_stamp'])

        self.df.loc[self.df.shape[0]] = {'user_name': item['user_name'],
                                         'time_stamp': item['time_stamp'],
                                         'comment_content': item['comment_content']}
        return item
