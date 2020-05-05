from flask import render_template,Blueprint,g,make_response,jsonify,request
from app.models import *
from app import db
import time
import subprocess

import json
special = Blueprint('special', __name__)


# 一个函数，用来做定时任务的任务。
def cronspider(a,b):
    rs = HzSpecialUrl.query.order_by(HzSpecialUrl.id.desc()).all()
    for i in rs:
        runspider(project="news",spider=i.spider_name,url_id=str(i.id))

def runspider(project="news",spider="netease",url_id="1"):

    clss = f'spider.sh {project} {spider} {url_id}'
    #print(clss.split(" "))
    subprocess.check_output(clss.split(" "))

@special.route("/", methods=["GET"])
@special.route("/index", methods=["GET"])
def _index():
    rs = HzSpecial.query.filter( HzSpecial.status==1).order_by(HzSpecial.id.desc()).limit(10).all()

    return render_template('/home/special/index.html',rs=rs)
@special.route("/spider", methods=["GET"])
def spider():
    # 创建一个CrawlerProcess对象
    # settings = get_project_settings()
    # process = CrawlerProcess(settings=settings)  # 括号中可以添加参数
    #
    # process.crawl(BookSpider, sub_id=1116367)
    # # process.crawl(BookSpider,sub_id=5243775)
    # process.start()
    # spider_name = "book"
    # spider_path=r"H: cd python\college\flasks\layui\spider\douban\ "
    # clss=spider_path+'scrapy crawl '+spider_name+" -a sub_id=1116367"
    # print(clss.split(" "))
    # subprocess.check_output(clss.split(" "))
    #subprocess.check_output(['scrapy', 'crawl', spider_name])
    id = int(request.args.get("id"))
    rs = HzSpecialUrl.query.filter( HzSpecialUrl.id==id).first()
    if (rs is None):
        response = make_response(jsonify({'status':0, 'info': "链接不存在", 'data': {"refer":1}}))
        return response
    runspider(project="news",spider=rs['spider_name'],url_id=str(id))

    response = make_response(jsonify({'status': 1, 'info': "已启动", 'data': {"refer":1}}))
    return response
@special.route("/urls", methods=["GET"])
def urls():
    id = int(request.args.get("id"))
    rs = HzSpecialUrl.query.filter( HzSpecialUrl.special_id==id).order_by(HzSpecialUrl.id.desc()).limit(10).all()
    return render_template('/home/special/urls.html',rs=rs)
@special.route("/comment", methods=["GET"])
def comment():
    id = request.args.get("id",type=int,default=0)
    q = request.args.get("q",type=str,default="")
    p = request.args.get("p",type=int,default=1)
    pager=50
    offset=(p-1) * pager
    if q is not "":
        rs = HzSpecialComment.query.filter( HzSpecialComment.special_id==id,HzSpecialComment.comment.like("%" + q + "%")).order_by(HzSpecialComment.id.desc()).limit(pager).offset(offset).all()
    else:
        rs = HzSpecialComment.query.filter( HzSpecialComment.special_id==id).order_by(HzSpecialComment.id.desc()).limit(pager).offset(offset).all()

    aa = HzSpecialComment.query.filter( HzSpecialComment.special_id==id, HzSpecialComment.score1 >= 0.7).count()  
    bb = HzSpecialComment.query.filter( HzSpecialComment.special_id==id, HzSpecialComment.score1 < 0.7).count()  
    daily_count = HzSpecialComment.daily_count()
    xAxis=daily_count['xAxis']
    series=daily_count['series']


    return render_template('/home/special/comment.html',rs=rs,aa=aa,bb=bb,xAxis=xAxis,series=series,q=q,id=id)
@special.route("/report", methods=["GET"])
def report():

    id = int(request.args.get("id"))
    aa = HzSpecialComment.query.filter( HzSpecialComment.special_id==id, HzSpecialComment.score1 >= 0.5).count()  
    bb = HzSpecialComment.query.filter( HzSpecialComment.special_id==id, HzSpecialComment.score1 < 0.5).count()  
    daily_count = HzSpecialComment.daily_count()
    xAxis=daily_count['xAxis']
    series=daily_count['series']
    print(series)  
    return render_template('/home/special/report.html',aa=aa,bb=bb,xAxis=xAxis,series=series) 


