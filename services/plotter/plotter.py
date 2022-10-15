from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np

from services.utils import logger


def plotter(data, configs):
    # logger.debug("Building plot for given data.")
    plt.figure()

    plt.plot(data.index.values, data[data.keys()[0]].values, color=configs["color"])

    set_configurations(configs)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    return buf


def set_configurations(configs):
    plt.title(label=configs["title"]["label"], color=configs["title"]["color"], fontsize=configs["title"]["fontsize"])
    plt.xlabel(xlabel=configs["xlabel"]["xlabel"], loc=configs["xlabel"]["loc"])
    plt.ylabel(ylabel=configs["ylabel"]["ylabel"], loc=configs["ylabel"]["loc"])
    plt.grid(visible=configs["grid"]["visible"], axis=configs["grid"]["axis"])


def plotter_for_fitter(data_x, data_y, function):
    increment = (max(data_x) - min(data_x)) / 100
    x = np.arange(min(data_x), max(data_x) + increment, increment)

    logger.debug("Building plot for given data.")
    plt.plot(data_x, data_y, 'o', label='data')
    plt.plot(x, function(x), '-', label='fit')
    plt.legend()

    logger.debug("Show resulting plot.")

    buf = BytesIO()
    plt.savefig(buf, format='png')
    return buf
