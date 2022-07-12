from reader import *
from plotter import *

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
    plot(response)
    return response
