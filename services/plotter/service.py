from pandas import DataFrame

from .._models.options import Options
from .._utils.preprocessor import validate_dataframe, validate_latex
from .._utils.log import logger
from .._utils.mpb_wrap import set_func, set_plots, set_configurations


def service(data: DataFrame, options: Options, func: str) -> bytes:
    """Triggers the plotter engine for the given request"""

    logger.debug("Preprocessing input data.")
    data = validate_dataframe(data)

    logger.debug("Validating provided function.")
    func = validate_latex(func)

    # TODO: validate latex function
    # TODO: convert latex to lambda code

    logger.debug("Building plot for given inputs.")
    
    uid = uuid4()
    fig: Figure = figure(uid)
    axes: Axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    set_func(axes, func)
    set_plots(axes, data, options.plots)
    set_configurations(axes, options.figure)

    buf = BytesIO()
    fig.savefig(buf, format="png")

    return buf.getvalue()
