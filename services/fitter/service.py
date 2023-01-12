from fitter import fitter

from .._utils.log import logger
from .._utils.preprocessor import validate_data


def service(request):
    """Triggers the fitter engine for the given request"""

    logger.debug("Preprocessing input data.")
    data = validate_data(request["data"])

    logger.debug("Calling fitter engine for given data.")
    response = fitter(data)

    logger.debug("Returning image as BytesIO.")
    return response
