from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    keyword = StringField(label='关键字', validators=[DataRequired()])
    submit = SubmitField(label='提交')