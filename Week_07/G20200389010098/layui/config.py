class Config(object):
    # MySQL Config
    MYSQL_HOST = 'test.mysql.rds.aliyuncs.com'
    MYSQL_PORT = 3306
    MYSQL_USER = 'test'
    MYSQL_PASSWD = 'test'
    MYSQL_DB = 'wordcloud'
    MYSQL_PRE = 'hz_'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8mb4&connect_timeout=10'
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_POOL_SIZE=100
    SQLALCHEMY_MAX_OVERFLOW=20
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    JOBS=[
        {
            'id':'job1',
            'func':'app.blue.home.special:cronspider',
            'args':(1,2),
            'trigger':'cron',
            'hour':5,
            'minute':8
        }
    ]