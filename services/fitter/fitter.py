import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitter(response):
    pass

xdata = [1, 2, 3, 4, 5, 6]
ydata = [1.2, 2.5, 2.9, 4.0, 5.1, 5.9]

# Recast xdata and ydata into numpy arrays so we can use their handy features
xdata = np.asarray(xdata)
ydata = np.asarray(ydata)
plt.plot(xdata, ydata, 'o')

# Define the Gaussian function
def Gauss(x, A, B):
    y = A*x + B
    return y

parameters, covariance = curve_fit(Gauss, xdata, ydata)

fit_A = parameters[0]
fit_B = parameters[1]
print(fit_A)
print(fit_B)

fit_y = Gauss(xdata, fit_A, fit_B)
plt.plot(xdata, ydata, 'o', label='data')
plt.plot(xdata, fit_y, '-', label='fit')
plt.legend()
plt.show()
