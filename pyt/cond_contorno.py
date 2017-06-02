import numpy as np
import matplotlib.pyplot as plt

t1 = 0
t2 = 75
t3 = 100
t4 = 50

A = [[4,-1,0,-1,0,0,0,0,0],[-1,4,-1,0,-1,0,0,0,0],[0,-1,4,0,0,-1,0,0,0],[-1,0,0,4,-1,0,-1,0,0],[0,-1,0,-1,4,-1,0,-1,0],[0,0,-1,0,-1,4,0,0,-1],[0,0,0,-1,0,0,4,-1,0],[0,0,0,0,-1,0,-1,4,-1],[0,0,0,0,0,-1,0,-1,4]]

MA = np.array(A)
print MA

B = [t2,t1,t4,t2,t1,t4,t2+t3,t3,t3+t4]
MB = np.array(B)

print MB, 'B'

IA = np.linalg.inv(MA)

T = np.dot(MB,IA)
print T, 'T nos pontos centrais'
