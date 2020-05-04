from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SForm(FlaskForm):
    s_word = StringField(label='关键词', validators=[DataRequired()])
    submit = SubmitField(label='搜索')
