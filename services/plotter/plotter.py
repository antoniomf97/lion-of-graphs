from ext_modules import logger
import matplotlib.pyplot as plt
import numpy as np


def plotter(data):
    logger.debug("Building plot for given data.")
    plt.figure()
    plt.plot(data)

    logger.debug("Show resulting plot.")
    plt.show()


def plotter_for_fitter(data_x, data_y, function):
    increment = (max(data_x) - min(data_x)) / 100
    x = np.arange(min(data_x), max(data_x) + increment, increment)

    logger.debug("Building plot for given data.")
    plt.plot(data_x, data_y, 'o', label='data')
    plt.plot(x, function(x), '-', label='fit')
    plt.legend()

    logger.debug("Show resulting plot.")
    # plt.show()
