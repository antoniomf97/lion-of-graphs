from reader import *
from fitter import fitter

"""
input:
  X,Y
0 1,2
1 2,4
2 3,8
3 4,16
"""

def plotter(b64_data):
    response = base64_to_dataframe(b64_data)
    fitter(response)
    return response
