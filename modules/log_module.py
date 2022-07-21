import os
import logging as log
import logging.config


log_path = "../services/logs\\"
logger = logging.getLogger()


def config_existing_logger(disable):
    """Disable all existing loggers"""
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': disable,
    })


def clean_all_logs():
    """Clean all existing logs"""
    for f in os.listdir(path=log_path):
        os.remove(os.path.join(log_path, f))


def config_logger(filename: str = "log.log", filemode: chr = 'a', level: int = log.DEBUG, clean_logs: bool = True,
                  log_format: str = "%(levelname)s [%(asctime)s] %(message)s", disable_existing_loggers: bool = True):
    """Configures the project logger for given inputs"""
    if clean_logs:
        clean_all_logs()
    log.basicConfig(filename=log_path+filename, filemode=filemode, level=level, format=log_format)
    config_existing_logger(disable_existing_loggers)
