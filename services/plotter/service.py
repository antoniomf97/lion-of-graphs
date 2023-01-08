from pandas import DataFrame
from services.models.options import Options

from plotter import plotter

from services.utils.log import logger
from services.utils.preprocessor import validate_dataframe


def service(data: DataFrame, options: Options) -> bytes:
    """Triggers the plotter engine for the given request"""

    logger.debug("Preprocessing input data.")
    data = validate_dataframe(data)

    logger.debug("Calling plotter engine for given data.")
    response = plotter(data, options)

    logger.debug("Returning image as bytes.")
    return response
