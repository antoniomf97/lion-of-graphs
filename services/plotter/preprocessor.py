from reader import *

"""
input:
X,Y
1,2
2,4
3,8
4,16
"""

def plotter(b64_data):
    print(base64_to_dataframe(b64_data))


if __name__ == '__main__':
    plotter("WCxZCjEsMgoyLDQKMyw4CjQsMTY=")

