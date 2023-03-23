from VectorClasses import*
import math as mt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
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

def generate_area(area: Area):
    x = []
    y = []
    z = []
    for i in range(100): # Will be changeable later in development
        new_point = area.point_is_on_area()
        x.append(new_point.x)
        y.append(new_point.y)
        z.append(new_point.z)
    return [x, y, z]

def show_straight2D(*straights: Straight2D):
    for straight in straights:
        x, y = generate_straight2d(straight)
        plt.plot(x, y)
    plt.show()

def show_straight3D(*straights: Straight3D):
    fig = plt.figure()
    ax = plt.axes(projection = "3d")
    for straight in straights:
        x, y, z = generate_straight3d(straight)
        ax.plot3D(x, y, z)
    plt.show()
