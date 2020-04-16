import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '3c3s3h'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@127.0.0.1/geektime'
    SQLALCHEMY_TRACK_MODIFICATIONS = False