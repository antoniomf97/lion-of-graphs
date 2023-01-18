from fitter import fitter

from pandas import DataFrame

from .._models.options import Options
from .._utils.log import logger
from .._utils.preprocessor import validate_dataframe


def service(data: DataFrame, options: Options, function: str):
    """Triggers the fitter engine for the given request"""

    logger.debug("Preprocessing input data.")
    data = validate_dataframe(data)

    logger.debug("Calling fitter engine for given data.")
    plot = fitter(data)

    logger.debug("Returning image as BytesIO.")
    return plot
