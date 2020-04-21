import hashlib
from datetime import datetime


class Helper:

    @staticmethod
    def md5(data):
        return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()

    @staticmethod
    def parse_comment_time(datetime_str):
        try:
            datetime_str = datetime_str.replace(" ", "")
            return datetime.strptime(datetime_str, "%Y-%m-%d")
        except:
            return datetime.now()
