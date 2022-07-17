import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def fitter(request):
    xdata = np.asarray(request['X'])
    ydata = np.asarray(request['Y'])
    parameters, covariance = curve_fit(LinearRegression, xdata, ydata)
    fit_A = parameters[0]
    fit_B = parameters[1]

    # plotting fits
    fit_y = LinearRegression(xdata, fit_A, fit_B)
    plt.plot(xdata, ydata, 'o', label='data')
    plt.plot(xdata, fit_y, '-', label='fit')
    plt.legend()
    plt.show()


class Function:
    def fit(self, x, y):
        pass


class LinearRegression(Function):
    def fit(self, x, y):
        pass

    def LinearRegression(x, A, B):
        y = A*x + B
        return y


