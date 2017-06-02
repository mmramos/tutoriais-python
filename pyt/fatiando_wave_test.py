import numpy as np
from matplotlib import animation
from fatiando import gridder
from fatiando.seismic import wavefd
from fatiando.vis import mpl

shape = (150, 900)
area = [0, 540000, 0, 90000]

w = wavefd.MexHatSource(10000, 10000, area, shape, 100000, 0.5, delay=2)
print w
