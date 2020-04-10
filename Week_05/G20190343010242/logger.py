import logging
from configure import getConfig


LOG_LEVELS = {
    'CRITICAL': logging.CRITICAL,
    'FATAL': logging.FATAL,
    'ERROR': logging.ERROR,
    'WARN': logging.WARNING,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOTSET': logging.NOTSET,
}

def getLogger(name):
    log_level = getConfig()["configs"]["log_level"]
    log_format = getConfig()["configs"]["log_format"]
    logging.basicConfig(level=LOG_LEVELS[log_level.upper()], format=log_format)
    return logging.getLogger(name)

