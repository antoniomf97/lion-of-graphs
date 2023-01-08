from io import BytesIO
from uuid import uuid4

from services.models.options import Options
from matplotlib.pyplot import figure
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from pandas import DataFrame


def plotter(data: DataFrame, configs: Options) -> bytes:
    uid = uuid4()
    fig: Figure = figure(uid)
    axes: Axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    axes.plot(data.index.values, data[data.keys()[0]].values, color=configs.color)
    set_configurations(axes, configs)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    return buf.getvalue()


def set_configurations(axes: Axes, configs: Options) -> None:
    axes.set_title(
        label=configs.title.label,
        color=configs.title.color,
        fontsize=configs.title.fontsize,
    )
    axes.set_xlabel(xlabel=configs.xlabel)
    axes.set_ylabel(ylabel=configs.ylabel)
