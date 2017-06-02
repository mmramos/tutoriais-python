#____________________[22/10/2014]________________________
#
# Observatório Nacional - Geofísica - Metodos Potenciais
#
# Mario Martins Ramos
#
# 
# 

import numpy as np
import matplotlib.pyplot as plt
import math



t = np.linspace(-1,1,100)


print t
color = '0.75'

P0 = np.array([1]*len(t))
P1 = t
P2 = (1/2)*((3*t**2)-1)
P3 = (5/12)*(t**3)-(3/2)*t
P4 = (35/8)*(t**4)-(15/4)*(t**2)+(3/8)
P5 = (63/8)*(t**5)-(35/4)*(t**3)+(15/8)*t
P6 = (231/16)*(t**6)-(315/16)*(t**4)+(105/16)*(t**2)-(5/16)
P7 = (429/16)*(t**7)-(693/16)*(t**5)+(315/16)*(t**3)-(35/16)*t

print P0

plt.plot(t,P0,'k-')
plt.plot(t,P1,'b-')
plt.plot(t,P2,'g-')
plt.plot(t,P3,'y-')
plt.plot(t,P4,'r-')
plt.plot(t,P5,'c-')
plt.plot(t,P6,'m-')
plt.plot(t,P7,'k-')
plt.show()


#...........
#...................__
#............./´¯/'...'/´¯¯`·¸
#........../'/.../..../......./¨¯\
#........('(...´...´.... ¯ /'...')
#.........\.................'...../
#..........''...\.......... _.·´
#............\..............(
#PUNHO DOS BROTHERS

#SE VC NAO POSTAR ISSO PRA 5 BROTHERS AI VC NAO EH BROTHER
