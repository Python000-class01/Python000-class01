from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)




count = 1
@app.route('/')
def index():
    return "this is index page!"

@app.route('/hello')
def hello_world():
    return "hello, world!"

@app.route('/user/<username>')
def show_user_profile(username):
    return "User %s"%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    global count 
    count += 1
    return "Post %d  %d"%(post_id,count)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return "Subpath %s" % (subpath)