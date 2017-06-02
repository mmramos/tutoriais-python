import numpy as np
import scipy as sp
from scipy import misc
import matplotlib.pyplot as plt

# nota: shape deve ter 60(cima) x 300(lado) 


m = misc.imread('cam.png') #IMPORTANTE usar o scipy para importar uma
# imagem na forma de matriz onde as cores são numeros


g = m.shape
d1 = g[0]
d2 = g[1]

print m
print "                                                              "
print "                                                              "
print "                                                              "
print "                                                              "
print "                                                              "


vp = np.array(m, float)

for j in range (d2):
    for i in range (d1):
        if vp[i,j] == 1:
            vp[i,j] = 800
        if vp[i,j] == 2:
            vp[i,j] = 1700
        if vp[i,j] == 3:
            vp[i,j] = 1700
        if vp[i,j] == 4:
            vp[i,j] = 2300
        if vp[i,j] == 5:
            vp[i,j] = 4500
        if vp[i,j] == 6:
            vp[i,j] = 4900
print vp
np.savetxt('camvp.txt', vp, fmt='%.4f') #salva como txt
#np.save('camv',v) # salva como binario
#np.ndarray.tofile('camv', sep=" ", format="%8f")

vs = np.array(m, float)

for j in range (d2):
    for i in range (d1):
        if vs[i,j] == 1:
            vs[i,j] = 300
        if vs[i,j] == 2:
            vs[i,j] = 500
        if vs[i,j] == 3:
            vs[i,j] = 400
        if vs[i,j] == 4:
            vs[i,j] = 700
        if vs[i,j] == 5:
            vs[i,j] = 2500
        if vs[i,j] == 6:
            vs[i,j] = 3000
print vs
np.savetxt('camvs.txt', vs, fmt='%.4f')


d = np.array(m, int)

for j in range (d2):
    for i in range (d1):
        if d[i,j] == 1:
            d[i,j] = 1600.0
        if d[i,j] == 2:
            d[i,j] = 2000.0
        if d[i,j] == 3:
            d[i,j] = 2100.0
        if d[i,j] == 4:
            d[i,j] = 2300.0
        if d[i,j] == 5:
            d[i,j] = 2500.0
        if d[i,j] == 6:
            d[i,j] = 2600.0

print d
np.savetxt('camd.txt', d, fmt='%.4f')

