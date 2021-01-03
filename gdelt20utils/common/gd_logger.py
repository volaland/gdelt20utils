import sys
import logging

from gdelt20utils.common.constants import APPLICATION_NAME


class Logger():
    def __init__(self):
        self.logger = None
        self.is_initialized = False

    def init_loger(self, filename, level=logging.INFO, name=APPLICATION_NAME):
        logging.basicConfig(
            level=level,
            format='%(asctime)s|%(pathname)s:%(lineno)s|%(levelname)s| %(message)s',
            handlers=(
                logging.StreamHandler(sys.stdout),
                logging.FileHandler(filename, mode='a+', encoding='utf8')
            )
        )

        self.logger = logging.getLogger(name)
        self.is_initialized = True

        self.logger.info("Logger {} is initialized".format(name))

logger_obj = Logger()

