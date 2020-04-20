from flask import Blueprint,request,redirect,url_for
from helper import NestableBlueprint



# 一级蓝图
home = NestableBlueprint('home', __name__)
# 二级蓝图
from app.blue.home.index import index as index
home.register_blueprint(index, url_prefix="/index")
from app.blue.home.login import login as login
home.register_blueprint(login, url_prefix="/login")


def checkCookie(auth,saltkey):
    if((auth is None) | (saltkey is None)):
        return False

@home.before_app_request
def before_request():
    #过滤静态资源
    if (request.blueprint is not None):
        auth = request.cookies.get('ms_home_auth')
        saltkey = request.cookies.get('ms_home_saltkey')
        print(auth)
        print(saltkey)
        if (request.path[0:6] !='/login'):
            if(checkCookie(auth,saltkey) == False):
                return redirect(url_for('login._index'))
        else:
            if(checkCookie(auth,saltkey) == True):
                return redirect(url_for('index._index'))

@home.route("/")
def index():
    return '2asdddddd'



