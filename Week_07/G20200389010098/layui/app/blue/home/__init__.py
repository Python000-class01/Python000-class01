from flask import Blueprint,request,redirect,url_for,g
from helper import NestableBlueprint
import xxtea


# 一级蓝图
home = NestableBlueprint('home', __name__)
# 二级蓝图
from app.blue.home.index import index as index
home.register_blueprint(index, url_prefix="/index")
from app.blue.home.login import login as login
home.register_blueprint(login, url_prefix="/login")
from app.blue.home.special import special as special
home.register_blueprint(special, url_prefix="/special")




def checkCookie(auth,saltkey):
    if((auth is not None) & (saltkey is not None)):
        try:
            dec = xxtea.decrypt_hex(str.encode(auth), str.encode(saltkey))
            mannageInfo=bytes.decode(dec)
            mannageList=mannageInfo.split("\t")
            print(mannageList)
        except (Exception) as e:
            print(e)
            return False 
        if(len(mannageList) != 2):
            return False
        else:
            g.appname = "swortect"
            return True
    else:
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


@home.app_context_processor
def appinfo():
    return dict(appname="test")
@home.route("/")
def index():
    return redirect(url_for('index._index'))



