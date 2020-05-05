from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, AnyOf

class SearchForm(FlaskForm):
    name = StringField(u'输入名称', render_kw={'placeholder': u'输入名称'},validators=[DataRequired()])
    category = StringField(u'书或电影', render_kw={'placeholder': u'书或电影'}, validators=[DataRequired()])
    submit = SubmitField(u'搜索')
