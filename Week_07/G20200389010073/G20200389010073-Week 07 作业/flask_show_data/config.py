from datetime import timedelta

class Config(object):
    # MySQL Config
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWD = 'root'
    MYSQL_DB = 'douban_reviews'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector:' \
                              f'//{MYSQL_USER}' \
                              f':{MYSQL_PASSWD}' \
                              f'@{MYSQL_HOST}' \
                              f':{MYSQL_PORT}' \
                              f'/{MYSQL_DB}' \
                              f'?charset=utf8&connect_timeout=10'
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True

    SECRET_KEY ='KEY'

    # session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)