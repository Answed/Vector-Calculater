from VectorClasses import*
import math as mt
import matplotlib.pyplot as plt
import numpy as np

def generate_straight2d(straight: Straight2D):
    x = []
    y = []
    for i in range(100): # Will be changeable later in development
        new_point = straight.point_on_straight(i)
        x.append(new_point.x)
        y.append(new_point.y)
    return [x, y]

def generate_straight3d(straight: Straight3D):
    x = []
    y = []
    z = []
    for i in range(100): # Will be changeable later in development
        new_point = straight.point_on_straight(i)
        x.append(new_point.x)
        y.append(new_point.y)
        z.append(new_point.z)
    return [x, y, z]