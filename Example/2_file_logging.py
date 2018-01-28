# Đặt log và đưa vào 1 file:
import logging
logging.basicConfig(filename='log_filename.txt', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.debug('This is a debug log message.')
logging.info('This is a info log message.')
logging.warning('This is a warning log message.')
logging.error('This is a error log message.')
logging.critical('This is a critical log message.')
