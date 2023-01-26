from matplotlib.axes import Axes

from .._models.options import Options


def set_configurations(axes: Axes, configs: Options) -> None:
    axes.set_title(
        label=configs.title.label,
        color=configs.title.color,
        fontsize=configs.title.fontsize,
    )
    axes.set_xlabel(xlabel=configs.xlabel)
    axes.set_ylabel(ylabel=configs.ylabel)


def set_func(axes: Axes, func: str):
    x = arange(1, 8, 8 / 100)
    y = quadratic(x)

    axes.plot(x, y, color="red")


def set_plots(axes: Axes, data: DataFrame, plots: Plot or FitPlot) -> None:
    xdata = data.index.values

    for plot in plots:
        ydata = data[plot.index].values
        if plot.showLines:
            axes.plot(xdata, ydata, color=plot.linesColor)
        if plot.showPoints:
            axes.scatter(xdata, ydata, color=plot.pointsColor)

