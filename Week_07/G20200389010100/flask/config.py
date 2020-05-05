from datetime import timedelta


class Config(object):
    # MYSQL
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'mysql'
    MYSQL_PASSWORD = 'Pwd_2020'
    MYSQL_DB = 'testdb'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    MY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True

    SECRET_KEY = 'KEY'

    # session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
