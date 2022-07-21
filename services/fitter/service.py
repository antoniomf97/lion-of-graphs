from ext_modules import logger
from ext_modules import validate_request
from ext_modules import preprocess_data
from fitter import fitter


def service(request):
    """Triggers the fitter engine for the given request"""

    logger.debug("Validating request in terms of format and JSON schema.")
    request = validate_request(request)

    logger.debug("Preprocessing data")
    data = preprocess_data(request["ContentB64"])

    fitter(data)

    return data.to_json().encode()
