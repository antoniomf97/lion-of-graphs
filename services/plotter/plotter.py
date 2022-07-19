import matplotlib.pyplot as plt
from services.modules import logger


def plot(df):
    logger.debug('outras cenas')
    plt.figure()
    plt.plot(df)
