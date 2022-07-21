from modules import logger
from modules import validate_request
from modules import preprocess_data
from fitter import fitter


def service(request):
    """Triggers the fitter engine for the given request"""

    logger.debug("Validating request in terms of format and JSON schema.")
    request = validate_request(request)

    logger.debug("Preprocessing data")
    data = preprocess_data(request["ContentB64"])

    fitter(data)

    return data.to_json().encode()
