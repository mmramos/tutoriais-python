#----------------------------------------------------#
#ALUNO: MARIO MARTINS RAMOS

#MODELAGEM NUMERICA DE ONDAS SISMICAS

#EXERCICIO 1 - SOLUCAO EXPLICITA
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

l = 500 #numero de intervalos de tempo



T1 = 100 #temperatura no lado esquerdo da barra
T2 = 50 #temperatura no lado direito da barra
T3 = 0 #temperatura inicial da barra

M1 = [T1]
M2 = [T3]*(p-2)
M3 = [T2]

M = np.array(M1+M2+M3)


N = []
tt = []
for j in range (l):
    
    M = M1+[M[i+1]+la*(M[i+2]-2*M[i+1]+M[i]) for i in range(p-2)]+M3
    N.append(M)
    tt.append(j*t)
    
    
print tt,"tempo"
print N, 'N'

P = []
for u in range (p):
    P.append(u)

print P

G0 = N[0]
G1 = N[l/4]
G2 = N[l/2]
G3 = N[3*(l/4)]
G4 = N[l-1]

plt.plot(P,G0,'-b')
plt.plot(P,G1,'-g')
plt.plot(P,G2,'-y')
plt.plot(P,G3,'-m')
plt.plot(P,G4,'-r')
plt.title('Distribuicao de Temperatura em uma Barra de Aluminio')
plt.xlabel('pontos da barra')
plt.ylabel('Temperatura')
plt.show()
