import numpy as np
import matplotlib.pyplot as plt

print ('o separador no caso era o :	: um espação vazio') 
data = np.genfromtxt('relevo.txt', delimiter='	')
print (data)

a=data[:, 0]
print (a)
b=data[:,1]
print (b)
sigy=data[:,2]
print (sigy)

x=data[0,:]
print (x)
