# Ví dụ 5: Tách log thành các file log theo thời gian
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('RotatingFileHandler')
# tách file hàng ngày vào 0h
handler = TimedRotatingFileHandler('time_log_file.txt', when="midnight", interval=1)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
