import os
from datetime import timedelta


db_file = os.path.join(os.path.dirname(__file__), 'instance', 'news.sqlite')

class Config(object):
    # # MySQL Config
    # MYSQL_HOST = '127.0.0.1'
    # MYSQL_PORT = 3306
    # MYSQL_USER = 'root'
    # MYSQL_PASSWD = 'rootroot'
    # MYSQL_DB = 'db1'
    # SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8&connect_timeout=10'

    SQLALCHEMY_DATABASE_URI = f'sqlite:////{db_file}?check_same_thread=False'

    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY =  'KEY'

    # session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    DEBUG = True