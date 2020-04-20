from flask import render_template
from week06_homework.showmes.models import Comment
from . import spbp



@spbp.route('/')
def index():
    comments=Comment.query.all()
    return render_template('showpage/comment.html',comments=comments)
