import numpy as np

a = [1000,0.2,-150,4,300000]
m = np.mean(a)
print (m, 'media')

aa = a-m
print (aa, 'xi - xm')

a2 = aa**2
print (a2, '(xi-xm)²')

S = np.sum(a2)
print (S, 'somatoria')

V = S/4
print (V, 'variance')



