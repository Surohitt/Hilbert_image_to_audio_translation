from hilbertcurve.hilbertcurve import HilbertCurve
from matplotlib.pyplot import *
p = 8
N = 2
hill_curve = HilbertCurve(p,N)

num_coords = 256*4
y_coords = []
x_coords = []
coords = []

for i in range(num_coords):
   hil_coords = hill_curve.coordinates_from_distance(i)
   coords.append(hil_coords)
   x_coords.append(hil_coords[0])
   y_coords.append(hil_coords[1])
plot(x_coords, y_coords)
show()
print(coords)
