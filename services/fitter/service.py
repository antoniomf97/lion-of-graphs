from services.modules import config_logger, logger
from services.modules import validate_request
from services.modules import preprocess_data
from fitter import fitter


def service(request):
    """Triggers the fitter engine for the given request"""
    filename, level = "test.log", 10
    config_logger(filename=filename)
    logger.debug("Initialized logging process at {} with level {}".format(filename, level))

    logger.debug("Validating request in terms of format and JSON schema.")
    request = validate_request(request)

    logger.debug("Preprocessing data")
    data = preprocess_data(request["ContentB64"])

    fitter(data)

    return data.to_json().encode()
