from flask import render_template,Blueprint,request, session, make_response,jsonify,redirect,url_for
from app.models import *
from app import db
from helper import getRandStr
import xxtea

login = Blueprint('login', __name__)
@login.route("/", methods=["GET"])
@login.route("/index", methods=["GET"])
def _index():
    return render_template('/home/login/index.html')

@login.route("/ajax_login", methods=["POST"])
def ajax_login():
    response = None
    rs = Manage.query.filter(Manage.user_name == request.form['username']).one_or_none()
    if(rs is None):
        return jsonify({'status': 0, 'info': "对不起，用户不存在", 'data': ""})
    if (rs.psd != Manage.md5_password(request.form['password'])):
        return jsonify({'status': 0, 'info': "对不起，密码错误", 'data': ""})
    refer=url_for('index._index')

    response = make_response(jsonify({'status': 1, 'info': "登陆成功", 'data': {"refer":refer}}))
    saltkey = "".join(getRandStr(16))
    print(saltkey)

    mannageInfo = str(rs.id)+"\t"+str(rs.status)
    auth = xxtea.encrypt_hex(mannageInfo, saltkey)
    print(auth)
    response.set_cookie('ms_home_auth', auth)
    response.set_cookie('ms_home_saltkey', saltkey)
    return response
@login.route("/logout", methods=["GET"])
def logout():
    response = make_response(redirect(url_for('login._index')))
    response.delete_cookie('ms_home_auth')
    response.delete_cookie('ms_home_saltkey')
    return response


    