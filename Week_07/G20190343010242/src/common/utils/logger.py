import logging
import os


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


def get_logger(name):
    log_level = os.getenv("LOG_LEVEL", "info")
    log_format = os.getenv("LOG_FORMAT", "%(asctime)-15s - %(name)s - %(levelname)s  %(message)s")
    logging.basicConfig(level=LOG_LEVELS[log_level.upper()], format=log_format)
    return logging.getLogger(name)

# To-do add more logging handlers, like file
