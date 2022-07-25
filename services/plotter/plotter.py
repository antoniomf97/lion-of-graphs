from ext_modules import logger
import matplotlib.pyplot as plt


def plotter(data):
    logger.debug("Building plot for given data.")
    plt.figure()
    plt.plot(data)

    logger.debug("Show resulting plot.")
    plt.show()
