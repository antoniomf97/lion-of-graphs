from pandas import DataFrame

from .plotter import build_plot
from .._models.options import Options
from .._utils.preprocessor import validate_dataframe, validate_latex
from .._utils.log import logger


def service(data: DataFrame, options: Options, func: str) -> bytes:
    """Triggers the plotter engine for the given request"""

    logger.debug("Preprocessing input data.")
    data = validate_dataframe(data)

    logger.debug("Validating provided function.")
    func = validate_latex(func)

    # TODO: validate latex function
    # TODO: convert latex to lambda code

    logger.debug("Building plot for given inputs.")
    plot = build_plot(data, options, func)

    return plot
