import numpy
from fatiando.gui.simple import Lasagne

# http://fatiando.readthedocs.org/en/releases/cookbook/seismic_profile_vertical_interactive.html

thickness = [20]*10
zp = numpy.arange(0.5, sum(thickness), 0.5)
print thickness
print zp
vmin, vmax = 500, 10000
app = Lasagne(thickness, zp, vmin, vmax)
app.run()
