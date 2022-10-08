from intmodules import logger, validate_data
from plotter import plotter
from parser import parse_request


def service(request):
    """Triggers the plotter engine for the given request"""

    logger.debug("Validating request in terms of format and JSON schema.")
    request = parse_request(request)

    logger.debug("Preprocessing input data.")
    data = validate_data(request["data"])

    logger.debug("Calling plotter engine for given data.")
    response = plotter(data, request["options"])

    logger.debug("Returning encoded json data.")
    return response
