import os
from flask  import Flask
from blog_dbo import DBConfig
import auth 
import post


# app enter point
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # config db ,then can get db from Dbconfig
    dbconfig = DBConfig(app)


# url function
    count = 1
    # @app.route('/')
    # def index():
    #     return "this is index page!"

    @app.route('/hello')
    def hello_world():
        return "hello, world!"

    @app.route('/user/<username>')
    def show_user_profile(username):
        return "User %s"%username

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        return "Post %d  %d"%(post_id,count)

    @app.route('/path/<path:subpath>')
    def show_subpath(subpath):
        return "Subpath %s" % (subpath)

    app.register_blueprint(auth.bp)
    app.register_blueprint(post.bp)
    app.add_url_rule('/',endpoint='index')
    return app

