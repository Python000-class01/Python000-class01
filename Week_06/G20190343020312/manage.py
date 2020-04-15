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

from app import app
if __name__ == "__main__":
    app.run()
