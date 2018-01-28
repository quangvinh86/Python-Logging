import logging

# basic logging: Set log and print to console
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.debug('This is a debug log message.')
logging.info('This is a info log message.')
logging.warning('This is a warning log message.')
logging.error('This is a error log message.')
logging.critical('This is a critical log message.')

# Lần lượt thay level logging thành DEBUG - INFO, WARNING - ERROR - CRITICAL
