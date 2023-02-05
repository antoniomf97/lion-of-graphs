from .fitter import fitter

from pandas import DataFrame

from .._models.options import Options
from .._utils.log import logger
from .._utils.preprocessor import validate_dataframe, validate_latex
from ..plotter.service import build_plot


def service(data: DataFrame, options: Options, func: str):
    """Triggers the fitter engine for the given request"""

    logger.debug("Preprocessing input data.")
    data: DataFrame = validate_dataframe(data)

    logger.debug("Validating provided function.")
    func = validate_latex(func)

    # TODO: validate latex function
    # TODO: convert latex to lambda code

    logger.debug("Calling fitter engine for given data.")
    fit_data: DataFrame = fitter(data)

    logger.debug("Building plot for given inputs.")
    plot = build_plot(data, options, func, fit_data)

    logger.debug("Returning image as bytes.")
    return plot
