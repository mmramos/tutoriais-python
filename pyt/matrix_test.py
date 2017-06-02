import numpy as np
import matplotlib.pyplot as plt
from numpy import matrix
from numpy import linalg

a = [[1,2,3],[4,5,5],[7,8,9]]
print a
c = linalg.inv(a)
print c
b = np.array(a)
print b
print b.T
