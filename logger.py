import datetime
import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


class Logger:

    _instance = None

    def __init__(self):
        pid = os.getpid()
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        log_name = 'sqlalchemy_db_' + str(pid) + '_' + today + '.log'
        f_handler = RotatingFileHandler('./log/' + log_name, encoding='utf-8', maxBytes=1048576, backupCount=10)
        f_handler.setLevel(logging.DEBUG)
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logging.getLogger('sqlalchemy').addHandler(f_handler)

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls):
        cls._instance = cls()
        cls.instance = cls._getInstance
        return cls._instance

    def get_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        pid = os.getpid()
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        log_name = 'stock_' + name + '_' + str(pid) + '_' + today + '.log'

        c_handler = logging.StreamHandler()
        f_handler = TimedRotatingFileHandler('./log/' + log_name, encoding='utf-8', when='midnight', backupCount=10)

        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        return logger