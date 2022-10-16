from parser import parse_request

from fitter import fitter

from utils.log import logger
from utils.preprocessor import validate_data


def service(request):
    """Triggers the fitter engine for the given request"""

    logger.debug("Validating request in terms of format and JSON schema.")
    request = parse_request(request)

    logger.debug("Preprocessing input data.")
    data = validate_data(request["data"])

    logger.debug("Calling fitter engine for given data.")
    response = fitter(data)

    logger.debug("Returning image as BytesIO.")
    return response
