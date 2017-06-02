import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------#

l = 10
t = 15

B = np.array([0]*l,float)

B[0] = 100
B[l-1] = 50

print B

Nj = []
for j in range (t):
    Ni = []
    for i in range (l):
        if i == 0:
            M = 100
        if 0 < i < l-1:
            M = (B[i-1,j]+B[i+1,j])*0.5
        if i == l-1:
            M = 50
        Ni.append(M)


    B = Ni
    
    Nj.append(B)

print Nj

#------------------------------------------------------------------#

L = []
for u in range (l):
    L.append(u)

print L

G0 = Nj[0]
G1 = Nj[t/4]
G2 = Nj[t/2]
G3 = Nj[3*(t/4)]
G4 = Nj[t-1]

plt.plot(L,G0,'-b')
plt.plot(L,G1,'-g')
plt.plot(L,G2,'-y')
plt.plot(L,G3,'-m')
plt.plot(L,G4,'-r')
plt.title('Teste barra condicao de contorno')
plt.xlabel('pontos da barra')
plt.ylabel('Temperatura')
plt.show()
