import numpy as np
import matplotlib.pyplot as plt



d1 = 500
v1 = 3000

d2 = 700
v2 = 3300
cr = 0.866

ti = 0.33

#x = np.array([0,150,300,450,600,750,900],float)

x = np.array([0,500,1000,1500,2000,2500,3000],float)



td = x/v1 #direta
#tr = (2*((d1**2)+((x)**2)/4)**(0.5)/v1) #refletida
tr = ((((2*d1)**2)+(x**2))**0.5)/v1

t0 = tr[0]

tdf = (4*(((d1+d2)**2)+(x**2)/4)**(0.5))/(v1+v2) #difratada


tm = (((2*t0)**2) + ((x/v1)**2))**(0.5) #multipla
trt = (((2*d1)*cr)/v1) + x/v2
#trt = ((2*d1)*cr)/v1 + (x-((2*d1)*cr)/v2) # reflexao total

print td
print tr
print tdf
print tm
print trt

plt.plot(x,td,'k')
plt.plot(x,tr,'b')
plt.plot(x,tdf,'c')
plt.plot(x,tm,'r')
plt.plot(x,trt,'g')
plt.show()
