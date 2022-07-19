import logging as log
import logging.config


log_path = "..\\logs\\"
logger = logging.getLogger()


def config_logger(filename: str = "log.log", filemode: chr = 'a', level: int = log.DEBUG,
                  logformat: str = "%(levelname)s [%(asctime)s] %(message)s", disable_existing: bool = True):
    """Configures the project logger for given inputs"""
    log.basicConfig(filename=log_path+filename, filemode=filemode, level=level, format=logformat)
    config_existing_logger(disable_existing)


def config_existing_logger(disable):
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': disable,
    })
