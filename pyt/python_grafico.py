import numpy as np
import matplotlib.pyplot as plt

a=[1, 2, 4, 7, 10, 15, 25]
b=[1, 2, 3, 4, 5, 6, 7]
c=[1, 7, 15, 7, 1, 7, 15] 

print (a)
print (b)


plt.title('TITULO DO GRAFICO AQUI')
plt.xlabel('O QUE VC VAI ESCREVER NO EIXO X')
plt.ylabel('O QUE VC VAI ESCREVER NO EIXO Y')

plt.plot(b, a,'-r') # posta linha( - ) vermelha
# r = vermelho
plt.plot(b, c,'*b') # posta "estrelinha"azul
# b = azul
plt.show()
