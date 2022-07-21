import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def fitter(data):
    """Fitter engine"""
    xdata, ydata = np.asarray(data.index.values), np.asarray(data[data.keys()[0]])

    parameters_l, covariance_l = curve_fit(LinearRegression, xdata, ydata)
    parameters_q, covariance_q = curve_fit(QuadraticRegression, xdata, ydata)

    test_plot_linear(xdata, ydata, parameters_l)
    test_plot_quadratic(xdata, ydata, parameters_q)
    plt.show()


def LinearRegression(x, m, c):
    """Computes the linear regression at point x, for given parameteres"""
    return m * x + c


def QuadraticRegression(x, a, b, c):
    """Computes the linear regression at point x, for given parameteres"""
    return a * x * x + b * x + c


def test_plot_linear(xdata, ydata, parameters):
    """Testing plot"""
    increment = (max(xdata)-min(xdata))/100
    x = np.arange(min(xdata), max(xdata)+increment, increment)

    fit_y = LinearRegression(x, parameters[0], parameters[1])
    plt.plot(xdata, ydata, 'o', label='data')
    plt.plot(x, fit_y, '-', label='fit')
    plt.legend()


def test_plot_quadratic(xdata, ydata, parameters):
    """Testing plot"""
    increment = (max(xdata) - min(xdata)) / 100
    x = np.arange(min(xdata), max(xdata) + increment, increment)

    fit_y = QuadraticRegression(x, parameters[0], parameters[1], parameters[2])
    plt.plot(xdata, ydata, 'o', label='data')
    plt.plot(x, fit_y, '-', label='fit')
    plt.legend()
