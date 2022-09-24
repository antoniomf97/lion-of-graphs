from intmodules import logger, validate_request, preprocess_data
from plotter import plotter


def service(request):
    """Triggers the plotter engine for the given request"""

    logger.debug("Validating request in terms of format and JSON schema.")
    request = validate_request(request)

    logger.debug("Preprocessing input data.")
    data = preprocess_data(request["ContentB64"])

    logger.debug("Calling plotter engine for given data.")
    plotter(data, request["Configurations"])

    logger.debug("Returning encoded json data.")
    return data.to_json().encode()


