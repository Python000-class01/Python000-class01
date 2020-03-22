# -*- coding: utf-8 -*-
import logging

# 设置日志输出格式
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)-15s] [%(levelname)8s] [%(name)10s ] - %(message)s (%(filename)s:%(lineno)s)',
                    datefmt='%Y-%m-%d %T'
                    )
logger = logging.getLogger(__name__)

# Truncate header and tailer blanks
def strip(data):
    if data is not None:
        return data.strip()
    return data