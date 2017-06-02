#----------------------------------------------------#
#ALUNO: MARIO MARTINS RAMOS

#MODELAGEM NUMERICA DE ONDAS SISMICAS

#EXERCICIO 2 - SOLUCAO IMPLICITA
#----------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt
import math

t = 0.1 #intervalo de tempo utilizado
d = 2 #espessura das secoes da barra
k = 0.49/(2.7*0.2174)
print k,"k"

la = (k*t)/(d*2) #lambda
print la,"LAMBDA"

l = 500 #numero de intervalos de tempo

TE = 100
TD = 50

ME = [TE]
MD = [TD]

M = np.array([[(1+2*la),-la,0,0],[-la,(1+2*la),-la,0],[0,-la,(1+2*la),-la],[0,0,-la,(1+2*la)]])
print M


MI = np.linalg.inv(M)
print MI

T0 = np.array([TE*la,0,0,TD*la])


M0 = np.array([0,0,0,0])

N = []
for j in range (l):
    M0 = np.dot(M0+T0,MI)
    N.append(M0)


P = []
for u in range (4):
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
