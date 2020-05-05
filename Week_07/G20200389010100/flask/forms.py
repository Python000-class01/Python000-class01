from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    keyword = StringField(label='关键词', validators=[DataRequired()])
    submit = SubmitField(label='搜索')
