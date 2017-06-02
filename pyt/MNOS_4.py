#----------------------------------------------------#
#ALUNO: MARIO MARTINS RAMOS

#MODELAGEM NUMERICA DE ONDAS SISMICAS

#EXERCICIO 3 - SOLUCAO EXPLICITA 2D
#----------------------------------------------------#

import numpy as np
import matplotlib.pyplot as plt
import math

a = 7
b = 5



# i = linha
# j = coluna
ME = [100]*b
MD = [50]*b

MET = [[100]]*b
MDT = [[50]]*b

M = [[0]*a]*b
MF = MET + M + MDT
MK = np.array(MF)

MG = MK.T
print MK
print MG


MG = [MG[i,j]+1] for i in range(a) for j in range (b)
