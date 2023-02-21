# from io import BytesIO
# from uuid import uuid4
# from matplotlib.pyplot import figure
# from matplotlib.figure import Figure
# from matplotlib.axes import Axes
from fastapi import UploadFile

from .._models.payload import PayloadModel
from .._utils.preprocessor import validate_data
# from .._utils.log import logger
# from .._utils.wrapper import set_func, set_plots, set_configurations


def service(rawData: UploadFile, payload: PayloadModel) -> bytes:
    """Triggers the plotter engine for the given request"""

    validate_data(dataList=payload.data, rawData=rawData)

    # logger.debug("Building plot for given inputs.")

    # uid = uuid4()
    # fig: Figure = figure(uid)
    # axes: Axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    # set_func(axes, func)
    # set_plots(axes, data, payload.plots)
    # set_configurations(axes, payload.figure)

    # buf = BytesIO()
    # fig.savefig(buf, format="png")

    # return buf.getvalue()
