# Ví dụ 3: In ra màn hình + ghi vào file.
import logging
from logging import FileHandler
from logging import StreamHandler
from logging import Formatter

logger = logging.getLogger('mylog')

def config_log():
    formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # file handles
    file_handler = FileHandler('log_filename.txt')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # stream handles
    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.CRITICAL)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def write_log():
    logger.debug('This is a debug log message.')
    logger.info('This is a info log message.')
    logger.warning('This is a warning log message.')
    logger.error('This is a error log message.')
    logger.critical('This is a critical log message.')


if __name__ == '__main__':
    config_log()
    write_log()
