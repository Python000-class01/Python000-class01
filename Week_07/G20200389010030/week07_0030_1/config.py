from datetime import timedelta
import time

class Config(object):
    # MySQL Config
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWD = 'root'
    MYSQL_DB = 'sina_news'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=UTF8MB4&connect_timeout=10'
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True

    SECRET_KEY = f'shop_helper{int(time.time())}'

    # session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)