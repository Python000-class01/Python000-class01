import functools
from flask import Blueprint
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
from flask import g
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from blog_dbo import UserDBO
from blog_models import BlogUser
from blog_models import BlogPost



bp = Blueprint("auth", __name__, url_prefix='/auth')
userDBO = UserDBO()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth/login'))
        return view(**kwargs)
    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = (userDBO.get_byid(user_id))

@bp.route("/register", methods=("GET", "POST"))
def register():
    """register a new user
    validates than the username is not already exist.
    encrypt the password
    """
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        password = generate_password_hash(password)
        user = BlogUser(username=username, password=password)
        userDBO.save_user(user)
    return render_template("auth/register.html")

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # password = generate_password_hash(password)
        user = userDBO.get_byname(username)
        
        errinfo = None

        
        if user is None or not check_password_hash(user.password, password):
            errinfo = "username or password is incorrect!"
        

        if errinfo is None:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for('index'))
        flash(errinfo)

    return render_template("auth/login.html")
@bp.route('/logout')
def logout():
    """ clear the current session, include the stored user id """
    session.clear()
    return redirect(url_for('index'))
        


