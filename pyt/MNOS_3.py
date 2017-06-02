#----------------------------------------------------#
#ALUNO: MARIO MARTINS RAMOS

#MODELAGEM NUMERICA DE ONDAS SISMICAS

#EXERCICIO 3 - SOLUCAO EXPLICITA 2D
#----------------------------------------------------#

import numpy as np
import matplotlib.pyplot as plt
import math

p=6 #numero de secoes da barra

t = 0.1 #intervalo de tempo utilizado
d = 2 #espessura das secoes da barra
k = 0.49/(2.7*0.2174)
print k,"k"

la = (k*t)/(d*2) #lambda
print la,"LAMBDA"

M = np.array([[100,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,50]])
print M

M1 = []
for i in range (1,4):
    for j in range (1,4):
        M1.append(M[i,j])
       

#print M1
print M1

m = np.array(M1).reshape(3,3)
print m
