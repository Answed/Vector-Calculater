from VectorClasses import *
import math as mt

def angle_between_vectors(vec1, vec2):
    scalar_product = vec1.scalar_product(vec2)
    angle = mt.acos(scalar_product/(vec1.length() * vec2.length()))
    return mt.degrees(angle)
