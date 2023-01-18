from .fitter import fitter

from pandas import DataFrame

from .._models.options import Options
from .._utils.log import logger
from .._utils.preprocessor import validate_dataframe
from ..plotter.service import build_plot


def service(data: DataFrame, options: Options, function: str):
    """Triggers the fitter engine for the given request"""

    logger.debug("Preprocessing input data.")
    data: DataFrame = validate_dataframe(data)

    logger.debug("Calling fitter engine for given data.")
    fit_data: DataFrame = fitter(data)

    plot = build_plot(fit_data, options)

    logger.debug("Returning image as bytes.")
    return plot
