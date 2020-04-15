class Config(object):
    # MySQL Config
    MYSQL_HOST = '192.168.6.128'
    MYSQL_PORT = 3306
    MYSQL_USER = 'loujg'
    MYSQL_PASSWD = 'Ljg2019!'
    MYSQL_DB = 'demo'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8&connect_timeout=10'
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True