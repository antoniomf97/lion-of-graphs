from parser import parse_request

from plotter import plotter

from utils.log import logger
from utils.preprocessor import validate_data


def service(request, options_schema):
    """Triggers the plotter engine for the given request"""

    logger.debug("Validating request in terms of format and JSON schema.")
    request = parse_request(request, options_schema)

    logger.debug("Preprocessing input data.")
    data = validate_data(request["data"])

    logger.debug("Calling plotter engine for given data.")
    response = plotter(data, request["options"])

    logger.debug("Returning image as BytesIO.")
    return response
