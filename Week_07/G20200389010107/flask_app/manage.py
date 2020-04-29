# manage 启动脚本
# app    入口
#   __init__.py
#   models.py   数据模型
#   static      静态文件
#   home        前台
#       __init__.py 
#       views.py    前台视图
#       forms.py    表单

#   templates       
#       home        前台模版
#       admin       后台模版

from app import app
from flask import Flask
from flask_script import Manager
from flask_apscheduler import APScheduler

import time
import sys
import os 
import path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../news_comment_spider')))
#from runspider import RunSpider
from scrapy import cmdline

manager = Manager(app)
scheduler = APScheduler(app=app)

@app.before_first_request
@scheduler.task(trigger='interval', id='run_spider', seconds=100)
def run_spider():
    cwd = os.getcwd()
    print(f"current working dir {cwd}")
    print(f'running spider @ {time.asctime(time.localtime(time.time()))}')
    spider_workding_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '../news_comment_spider')))
    print(f"change dir {spider_workding_dir}")
    os.chdir(spider_workding_dir)
    os.system("scrapy crawl sina_news_comment")
    os.chdir(cwd)
    print(f"reset dir: {os.getcwd()}")


    
    

@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch("**/*.*")
    live_server.serve(open_url=True)

if __name__ == "__main__":
    scheduler.start()
    manager.run()
