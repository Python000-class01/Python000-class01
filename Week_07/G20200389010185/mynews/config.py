from datetime import timedelta

class Config(object):
    # MySQL Config
    MYSQL_HOST = '14.14.14.20'
    MYSQL_PORT = 3306
    MYSQL_USER = 'python'
    MYSQL_PASSWD = '123456'
    MYSQL_DB = 'python'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8&connect_timeout=10'
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True

    SECRET_KEY =  '14-w9Wl:xSXG-w,;s2F22S#0.N9%^Mm2K%Nekpn2'

    # session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)