import matplotlib.pyplot as plt
from ext_modules import logger


def plotter(df):
    logger.debug('outras cenas')
    plt.figure()
    plt.plot(df)

