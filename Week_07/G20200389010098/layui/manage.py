# manage 启动脚本
# app    入口
#   __init__.py
#   models.py   数据模型
#   static      静态文件
#   home        前台
#       __init__.py 
#       views.py    前台视图
#       forms.py    表单
#   admin
#       __init__.py
#       views.py    管理视图
#       forms.py    管理表单
#   templates       
#       home        前台模版
#       admin       后台模版

from flask_apscheduler import APScheduler
from app import app

if __name__ == "__main__":
    scheduler=APScheduler()  # 实例化APScheduler
    scheduler.init_app(app)  # 把任务列表放进flask
    scheduler.start() # 启动任务列表
    app.run(host='0.0.0.0',port=5000,debug=True)
