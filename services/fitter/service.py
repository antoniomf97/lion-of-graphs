from intmodules import logger, parse_request, preprocess_data
from fitter import fitter


def service(request):
    """Triggers the fitter engine for the given request"""

    logger.debug("Validating request in terms of format and JSON schema.")
    request = parse_request(request)

    logger.debug("Preprocessing input data.")
    data = preprocess_data(request["data"])

    logger.debug("Calling fitter engine for given data.")
    fitter(data)

    logger.debug("Returning encoded json data.")
    return data.to_json().encode()
