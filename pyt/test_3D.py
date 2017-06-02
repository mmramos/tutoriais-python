from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.array([0,1,2,3,4],float)
Y = X**2
Z = np.array([1,1,1,1,1],float)

ax.plot_wireframe(X,Y,Z)

plt.show()
