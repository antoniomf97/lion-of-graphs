from plotter import plotter

from utils.log import logger
from utils.preprocessor import validate_data


def service(data, options) -> bytes:
    """Triggers the plotter engine for the given request"""

    logger.debug("Preprocessing input data.")
    data = validate_data(data)

    logger.debug("Calling plotter engine for given data.")
    response = plotter(data, options)

    logger.debug("Returning image as bytes.")
    return response
