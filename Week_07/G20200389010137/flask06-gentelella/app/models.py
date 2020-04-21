# coding: utf-8
from sqlalchemy import Column, Integer, Table, Text
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import json


from . import login_manager
# 类似Django认证用户模型
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



from flask_login import UserMixin
class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)

    @property
    def password(self):
        return None

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """
        用户是不是被禁用
        """
        return True


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Text, unique=True)
    desc = db.Column(db.Text)
    event_time = db.Column(db.Text)
    event_date = db.Column(db.Text)
    collect_time = db.Column(db.Text)

class Sentiments(db.Model):
    __tablename__ = 'sentiments'

    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Text, unique=True)
    sentiment = db.Column(db.Text)
