import logging
import datetime


def get_logger(name):
    level = logging.INFO

    log_file = "logs/" + name + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
