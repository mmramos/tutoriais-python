import numpy as np

pvel  = np.genfromtxt('camvp.txt')
shape = pvel.shape
shape0 = shape[0]
shape1 = shape[1]

R = np.zeros(shape)
S = np.zeros(shape)

for j in range (shape1-1):
    for i in range (shape0-1):
        if pvel[i,j] != pvel[i-1,j]:
            R[i,j] = 1
        if pvel[i,j] != pvel[i,j-1]:
            R[i,j] = 2

print R
