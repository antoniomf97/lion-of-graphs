from io import BytesIO
from uuid import uuid4

from matplotlib.pyplot import figure
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from pandas import DataFrame


def plotter(data: DataFrame, configs: dict) -> BytesIO:
    uid = uuid4()
    fig: Figure = figure(uid)
    axes: Axes = fig.add_axes([.1, .1, .8, .8])

    axes.plot(data.index.values, data[data.keys()[0]].values, color=configs["color"])
    set_configurations(axes, configs)

    buf = BytesIO()
    fig.savefig(buf, format='png')
    return buf


def set_configurations(axes: Axes, configs: dict) -> None:
    axes.set_title(label=configs["title"]["label"], color=configs["title"]["color"], fontsize=configs["title"]["fontsize"])
    axes.set_xlabel(xlabel=configs["xlabel"]["xlabel"], loc=configs["xlabel"]["loc"])
    axes.set_ylabel(ylabel=configs["ylabel"]["ylabel"], loc=configs["ylabel"]["loc"])
    axes.grid(visible=configs["grid"]["visible"], axis=configs["grid"]["axis"])


# This should not exist as a function - fix it later
# def plotter_for_fitter(data_x, data_y, function):
#     increment = (max(data_x) - min(data_x)) / 100
#     x = np.arange(min(data_x), max(data_x) + increment, increment)
#
#     logger.debug("Building plot for given data.")
#     plt.plot(data_x, data_y, 'o', label='data')
#     plt.plot(x, function(x), '-', label='fit')
#     plt.legend()
#
#     logger.debug("Show resulting plot.")
#
#     buf = BytesIO()
#     plt.savefig(buf, format='png')
#     return buf
