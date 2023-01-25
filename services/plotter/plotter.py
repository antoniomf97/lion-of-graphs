from io import BytesIO
from uuid import uuid4

from numpy import arange
from pandas import DataFrame
from matplotlib.pyplot import figure
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from .._models.options import Options, Plot, Figure


def build_plot(data: DataFrame, options: Options, func: str):
    uid = uuid4()
    fig: Figure = figure(uid)
    axes: Axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    set_func(axes, func)
    set_plots(axes, data, options.plots)
    set_configurations(axes, options.figure)

    buf = BytesIO()
    fig.savefig(buf, format="png")

    return buf.getvalue()


def quadratic(x):
    return -(x - 4)**2 + 50


def set_func(axes: Axes, func: str):
    x = arange(1, 8, 8 / 100)
    y = quadratic(x)

    axes.plot(x, y, color="red")


def set_plots(axes: Axes, data: DataFrame, plots: Plot) -> None:
    xdata = data.index.values

    for plot in plots:
        ydata = data[plot.index].values
        if plot.showLines:
            axes.plot(xdata, ydata, color=plot.linesColor)
        if plot.showPoints:
            axes.scatter(xdata, ydata, color=plot.pointsColor)


def set_configurations(axes: Axes, figure: Figure) -> None:
    axes.set_title(
        label=figure.title.label,
        color=figure.title.color,
        fontsize=figure.title.fontsize,
    )
    axes.set_xlabel(xlabel=figure.xlabel)
    axes.set_ylabel(ylabel=figure.ylabel)
