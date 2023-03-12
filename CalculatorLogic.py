from VectorClasses import *
import math as mt


g = Straight3D(Vector3(2, 1, 3), Vector3(1, 2, 3))
h = Straight3D(Vector3(1, 3, 4), Vector3(3, 1, 2))

print(g.distance_between_straights(h))

