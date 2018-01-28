# Ví dụ 4: Tách log thành các file log theo kích thước
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter

formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('RotatingFileHandler')
handler = RotatingFileHandler('log_filename.txt', maxBytes=2, backupCount=10)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

for index in range(1000):
    logger.debug('This is a debug log message.')
    logger.info('This is a info log message.')
    logger.warning('This is a warning log message.')
    logger.error('This is a error log message.')
    logger.critical('This is a critical log message.')
