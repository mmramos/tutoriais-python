import numpy as np

def explicita(N,TempoFinal):
    Nt = int(TempoFinal/dt) # Numero de passos
    x = np.arange(0,N*2,dx) 
    T = np.zeros(N)
    T[0] = T0
    T[-1] = Tf
    for l in range(0,Nt):
        for i in range(1,N-1):
            T[i] = T[i]+(Lambda*(T[i+1]-(2*T[i])+T[i-1]))
        
    return T,x
print T
