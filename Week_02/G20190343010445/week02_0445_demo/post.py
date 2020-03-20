import functools
from datetime import datetime
from flask import Blueprint
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
from flask import abort
from flask import g
from blog_dbo import PostDBO
from auth import login_required
from blog_models import BlogPost

bp = Blueprint("post", __name__)
postDBO = PostDBO()

@bp.route('/')
def index():
    posts = postDBO.get_all()
    return render_template("post/index.html", posts = posts)

@bp.route("/create", methods=("POST", "GET"))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        errinfo = None

        if not title:
            errinfo = 'title is required'
        
        if errinfo is not None:
            flash(errinfo)
        else:
            post = BlogPost(created=datetime.now(), author_id=g.user.id, title = title, body = body)
            postDBO.save_post(post)
    return render_template('post/create.html')

@bp.route('/<int:id>/update', methods = ("GET", "POST"))
@login_required
def update(id):
    post = postDBO.get_byid(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        errinfo = None

        if post.title is None:
            errinfo = "blog title is required"
        
        if errinfo is not None:
            flash(errinfo)
        else:
            postDBO.save_post(post)
            return redirect(url_for('post.index'))
    return render_template('post/update.html', post=post)

@bp.route('/<int:id>/delete', methods = ('POST',))
@login_required
def delete(id):
    """ delete a post.
    ensure than the post exists and that the logged in user is the author of the post
    """
    post = postDBO.validate_post_author(userid=g.user.id,postid=id)
    if post is not None:
        postDBO.delete_post(post)
        return redirect(url_for('post.index'))
    abort(404, "delete post failed!")
