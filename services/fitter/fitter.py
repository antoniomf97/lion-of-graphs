# from intmodules import logger
import numpy as np
from scipy.optimize import curve_fit
from pandas import DataFrame


def fitter(data: DataFrame) -> tuple:
    """Fitter engine"""
    xdata, ydata = np.asarray(data.index.values), np.asarray(data[data.keys()[0]])

    # logger.debug("Computing quadratic regression for given data.")
    parameters_q, covariance_q = curve_fit(LinearRegression, xdata, ydata)

    increment = (max(xdata) - min(xdata)) / 100  # resolution

    x = np.arange(min(xdata), max(xdata) + increment, increment)

    fit_y = LinearRegression(x, parameters_q[0], parameters_q[1])

    return DataFrame(fit_y, index=x)


def LinearRegression(x: float, m: float, c: float) -> float:
    """Computes the linear regression at point x, for given parameteres"""
    return m * x + c


def QuadraticRegression(x: float, a: float, b: float, c: float) -> float:
    """Computes the linear regression at point x, for given parameteres"""
    return a * x * x + b * x + c


# keep for later usage

# def test_plot_linear(xdata, ydata, parameters):
#     """Testing plot"""
#     increment = (max(xdata) - min(xdata)) / 100
#     x = np.arange(min(xdata), max(xdata) + increment, increment)

#     fit_y = LinearRegression(x, parameters[0], parameters[1])
#     plt.plot(xdata, ydata, "o", label="data")
#     plt.plot(x, fit_y, "-", label="fit")
#     plt.legend()


# def test_plot_quadratic(xdata, ydata, parameters):
#     """Testing plot"""
#     increment = (max(xdata) - min(xdata)) / 100
#     x = np.arange(min(xdata), max(xdata) + increment, increment)

#     fit_y = QuadraticRegression(x, parameters[0], parameters[1], parameters[2])
#     plt.plot(xdata, ydata, "o", label="data")
#     plt.plot(x, fit_y, "-", label="fit")
#     plt.legend()
