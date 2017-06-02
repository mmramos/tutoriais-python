"""Simple matshow() example."""
from matplotlib.pylab import *


def samplemat(dims):
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    aa = zeros(dims)
    for i in range(min(dims)):
        aa[i, i] = i
    return aa



# Display 2 matrices of different sizes
dimlist = [(100, 100), (100, 100)]
for d in dimlist:
    matshow(samplemat(d))

print dimlist
show()
