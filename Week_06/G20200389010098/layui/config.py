class Config(object):
    # MySQL Config
    MYSQL_HOST = 'swortect.mysql.rds.aliyuncs.com'
    MYSQL_PORT = 3306
    MYSQL_USER = 'swortect'
    MYSQL_PASSWD = '1q2w3e4r'
    MYSQL_DB = 'wordcloud'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8mb4&connect_timeout=10'
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True