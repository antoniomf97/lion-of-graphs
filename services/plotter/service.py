import json
from preprocessor import plotter
from services.modules import config_logger, logger


def validate_json(request):
    pass


def service(request):
    config_logger(filename='log.log', disable_existing_loggers=True)

    validate_json(request)
    parsed = json.loads(request)
    response = plotter(parsed["ContentB64"]).to_json().encode()
    logger.debug('cenas')

    return response

