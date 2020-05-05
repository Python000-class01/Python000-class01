# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

from app.models import User

from app.models import User

class LoginForm(FlaskForm):

    username = StringField(
        label=u"用户名",
        validators=[DataRequired(u"请输入用户名！")],
        description=u"用户名",
        render_kw={
            "class": "form-control form-control-user",
            "id": "exampleInputEmail",
            "placeholder": u"用户名...",
            "required": u"required"
            }
        )
    password = PasswordField(
        label=u'密码',
        validators=[DataRequired()],
        description=u"密码",
        render_kw={
            "class": "form-control form-control-user",
            "id": "exampleInputPassword",
            "placeholder": u"密码...",
            "required": u"required"
            }
        )
    submit = SubmitField(
        label=u'登录',
        description=u"登录",
        render_kw={"class": "btn btn-primary btn-user btn-block"}
        )
    remeberme = BooleanField(label='remeberme')


class RegisterForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[
            DataRequired(), Length(1, 20),
            Regexp('^[a-zA-Z0-9]*$', message='The username should contain only a-z, A-Z and 0-9.')
            ]
        )
    password = PasswordField(
        label='Password',
        validators=[DataRequired(), Length(8, 128), EqualTo('reppassword')]
        )
    reppassword = PasswordField(label='Confirm password', validators=[DataRequired()])
    submit = SubmitField(label=u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('The email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('The username is already in use.')