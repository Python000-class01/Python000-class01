import sys
import os 
import path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting.setting import GlobalSetting
from datetime import timedelta


class Config(object):
    # MySQL Config
    MYSQL_HOST = GlobalSetting.mysql_host
    MYSQL_PORT = GlobalSetting.mysql_port
    MYSQL_USER = GlobalSetting.mysql_user
    MYSQL_PASSWD = GlobalSetting.mysql_password
    MYSQL_DB = GlobalSetting.mysql_database
    MYSQL_TABLE = GlobalSetting.mysql_cleaned_data_table
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8&connect_timeout=10'
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True

    SECRET_KEY = 'KEY'

    # session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
