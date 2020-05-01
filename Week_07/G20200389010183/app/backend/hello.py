from flask import Flask, render_template, redirect, url_for, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import sched
import time
import os
from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from newsCrawl.spiders.hw5_2 import ExampleSpider

# from homework7.backend import app
Base = declarative_base()
# flask 服务
app = Flask(__name__)
# 定时任务
s = sched.scheduler(time.time, time.sleep)


# 1. 完成从数据库读取数据 ok
# 2. 正确返回前台ok
# 3. 前段网页展示
# 4. 重构
#
class CommentDO(Base):
    # 表名
    __tablename__ = "news_comment"
    # 字段，属性
    id = Column(Integer, primary_key=True)
    atti = Column(Integer)
    time = Column(DateTime)
    user_name = Column(String(255))
    score = Column(Integer)
    comment = Column(String(2000))


def spider_task():
    proc = CrawlerProcess(get_project_settings())
    proc.crawl(ExampleSpider)
    proc.start()


def crawl_sched(time_loop_seconds):
    print('开始定时任务爬取数据')
    s.enter(time_loop_seconds, 2, spider_task)
    s.enter(time_loop_seconds, 1, crawl_sched, argument=(time_loop_seconds,))  # time_loop_seconds每隔秒执行一次perform1
    s.run()
    print('定时任务结束')


@app.route('/post', methods=['post'])
def post():
    page_size = request.form['pageSize']
    keyword = request.form['keyword']
    print(keyword)
    return redirect(f"{url_for('query')}?pageSize={page_size}&keyword={keyword}")


@app.route('/')
def query():
    star_to_number = {
        '5': '力荐',
        '4': '推荐',
        '3': '还行',
        '2': '较差',
        '1': '很差',
        '0': '很差'
    }
    page_size = 10
    keyword = None
    if request.args.lists():
        page_size = request.args.to_dict().get('pageSize', 10)
        keyword = request.args.to_dict().get('keyword', None)
        print('+' * 20)
        print(page_size)
        print(keyword)
    if not page_size:
        page_size = 10
    engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8", echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    print('+' * 20)
    print(page_size)
    # new_data = CommentDO(id=item['id'], rank=item['rank'], comment=item['comment'], sentiments=sent)
    if keyword is None:
        res = session.query(CommentDO).order_by(CommentDO.time.desc()).limit(page_size)
    else:
        print('keyword' + str(keyword))
        res = session.query(CommentDO).filter(CommentDO.comment.like(f'%{keyword}%')).order_by(
            CommentDO.time.desc()).limit(page_size)
    print('res' + str(res))
    lists = []
    pos = 0
    neg = 0
    day_count = {}
    for do in res:
        # com = do.comment
        # if keyword:
        #     if not com.__contains__(keyword):
        #         continue
        time = do.time
        atti = do.atti
        print(f'atti:{atti}')
        if atti == 0:
            pos += 1
        else:
            neg += 1
        # print(time)
        day = str(time)[0:10]
        if day_count.__contains__(f'{day}'):
            day_count[f'{day}'] = day_count[f'{day}'] + 1
        else:
            day_count[f'{day}'] = 1
        comment = {}
        comment["id"] = do.id
        comment["comment"] = do.comment
        comment["score"] = do.score
        comment["atti"] = do.atti
        comment["time"] = do.time
        comment["user_name"] = do.user_name
        print(do.atti)
        # comment["sentiments"] = star_to_number[str(int(do.sentiments * 5))]
        lists.append(comment)
    print(f'P:{pos} N:{neg}')
    # session.commit()
    # print(lists)
    labels = []
    values = []
    print(day_count)
    for k, v in day_count.items():
        labels.append(k)
        values.append(v)
    count = {}
    count['labels'] = labels
    count['values'] = values
    statistic = json.dumps(count)
    print(statistic)
    return render_template('index.html', item_name='饥饿站台', results=lists, statistic=statistic, positive=pos,
                           negative=neg, search_keyword=keyword)


def flask_task():
    print('#' * 50)
    print(f'flask app running, pid is {os.getpid()}, ppid is {os.getppid()}')
    print('#' * 50)
    # app.secret_key = 'key'
    app.run(port=8080)


if __name__ == '__main__':
    spider = Process(target=crawl_sched, args=(60,))#传入爬虫执行的时间，这里测试设置为1分钟，一般设置为 3600*24 一天
    spider.start()
    flask_app = Process(target=flask_task)
    flask_app.start()

    spider.join()
    flask_app.join()
