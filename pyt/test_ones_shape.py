import numpy as np

# Set the parameters of the finite difference grid
shape = (10, 10)
area = [0, 800000, 0, 160000]

# Make a density and S wave velocity model
density = 2400*np.ones(shape)
svel = 3500*np.ones(shape)
moho = 5
density[moho:] = 2800
svel[moho:] = 4500

print density
print svel
