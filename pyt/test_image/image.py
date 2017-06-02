import numpy as np
import scipy as sp
from scipy import misc
import matplotlib.pyplot as plt

# nota: shape deve ter 60(cima) x 300(lado) 

m = misc.imread('601x301.png')
g = m.shape
d1 = g[0]
d2 = g[1]

print m


v = np.array(m, float)

for j in range (d2):
    for i in range (d1):
        if v[i,j] == 1:
            v[i,j] = 2400.0
        if v[i,j] == 2:
            v[i,j] = 2600.0
        if v[i,j] == 3:
            v[i,j] = 2800.0
        if v[i,j] == 4:
            v[i,j] = 3500.0
print v
np.savetxt('v.txt', v)

print m

d = np.array(m, float)

for j in range (d2):
    for i in range (d1):
        if d[i,j] == 1:
            d[i,j] = 3400.0
        if d[i,j] == 2:
            d[i,j] = 3600.0
        if d[i,j] == 3:
            d[i,j] = 3800.0
        if d[i,j] == 4:
            d[i,j] = 4500.0

print d
np.savetxt('d.txt', d)
