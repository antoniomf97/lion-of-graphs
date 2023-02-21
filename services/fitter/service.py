from io import BytesIO
from uuid import uuid4

from .fitter import fitter

from matplotlib.pyplot import figure
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from pandas import DataFrame

from .._models.options import Options
from .._utils.log import logger
from .._utils.preprocessor import validate_dataframe, validate_latex
from .._utils.wrapper import  set_func, set_plots, set_configurations


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

    uid = uuid4()
    fig: Figure = figure(uid)
    axes: Axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    set_func(axes, func)
    set_plots(axes, data, options.plots)
    set_plots(axes, fit_data, options.fitPlots)
    set_configurations(axes, options.figure)

    buf = BytesIO()
    fig.savefig(buf, format="png")

    return buf.getvalue()

