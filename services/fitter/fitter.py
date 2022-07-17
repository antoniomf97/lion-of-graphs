import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def fitter(request, keys='Y'):
    """Fitter engine"""
    xdata, ydata = np.asarray(request.index.values), np.asarray(request[keys[0]])
    parameters, covariance = curve_fit(LinearRegression, xdata, ydata)

    test_plot(xdata, ydata, parameters)


def LinearRegression(x, m, c):
    """Computes the linear regression at point x, for given parameteres"""
    return m * x + c


def test_plot(xdata, ydata, parameters):
    """Testing plot"""
    fit1 = parameters[0]
    fit2 = parameters[1]
<<<<<<< HEAD
=======

    fit_y = LinearRegression(xdata, fit1, fit2)
    plt.plot(xdata, ydata, 'o', label='data')
    plt.plot(xdata, fit_y, '-', label='fit')
    plt.legend()
    plt.show()
>>>>>>> 7b27599 (Refactored fitter engine)

    fit_y = LinearRegression(xdata, fit1, fit2)

