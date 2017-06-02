"""
Seismic: 2D finite difference simulation of elastic SH wave propagation in a
medium with a discontinuity (i.e., Moho), generating Love waves.
"""
import numpy as np
from matplotlib import animation
from fatiando import gridder
from fatiando.seismic import wavefd
from fatiando.vis import mpl



# Set the parameters of the finite difference grid

density = np.genfromtxt('d.txt')
svel = np.genfromtxt('v.txt')
shape = svel.shape
area = [0, 80000, 0, 10000]

# Make a density and S wave velocity model

mu = wavefd.lame_mu(svel, density)

# Make a wave source from a mexican hat wavelet
sources = [wavefd.MexHatSource(1000, 1000, area, shape, 80000, 0.8, delay=2)]

# Get the iterator. This part only generates an iterator object. The actual
# computations take place at each iteration in the for loop below
dt = wavefd.maxdt(area, shape, svel.max())
duration = 35
maxit = int(duration/dt)
stations = [[10000, 0], [70000, 0]]
snapshots = int(1./dt)
simulation = wavefd.elastic_sh(mu, density, area, dt, maxit, sources, stations,
                               snapshots, padding=70, taper=0.005)

# This part makes an animation using matplotlibs animation API
background = svel*5*10**-7
fig = mpl.figure(figsize=(10, 8))
mpl.subplots_adjust(right=0.98, left=0.11, hspace=0.3, top=0.93)
mpl.subplot(3, 1, 1)
mpl.title('Seismogram 1')
seismogram1, = mpl.plot([],[],'-k')
mpl.xlim(0, duration)
mpl.ylim(-0.1, 0.1)
mpl.ylabel('Amplitude')
mpl.subplot(3, 1, 2)
mpl.title('Seismogram 2')
seismogram2, = mpl.plot([],[],'-k')
mpl.xlim(0, duration)
mpl.ylim(-0.1, 0.1)
mpl.ylabel('Amplitude')
ax = mpl.subplot(3, 1, 3)
mpl.title('time: 0.0 s')
wavefield = mpl.imshow(background, extent=area, cmap=mpl.cm.gray_r,
                       vmin=-0.005, vmax=0.005)
mpl.points(stations, '^b', size=8)
#mpl.text(7500, 2000, 'Crust')
#mpl.text(7400, 10000, 'Mantle')
fig.text(0.82, 0.33, 'Seismometer 2')
fig.text(0.16, 0.33, 'Seismometer 1')
mpl.ylim(area[2:][::-1])
mpl.xlabel('x (km)')
mpl.ylabel('z (km)')
mpl.m2km()
times = np.linspace(0, dt*maxit, maxit)
# This function updates the plot every few timesteps
def animate(i):
    t, u, seismogram = simulation.next()
    mpl.title('time: %0.1f s' % (times[t]))
    wavefield.set_array((background + u)[::-1])
    seismogram1.set_data(times[:t+1], seismogram[0][:t+1])
    seismogram2.set_data(times[:t+1], seismogram[1][:t+1])
    return wavefield, seismogram1, seismogram2
anim = animation.FuncAnimation(fig, animate, frames=maxit/snapshots, interval=1)
mpl.show()
