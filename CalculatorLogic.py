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
    span_striaght1 = Straight3D(area.base_point, area.span_vector1)
    span_striaght2 = Straight3D(area.base_point, area.span_vector2)
    for i in range(100): # Will be changeable later in development
        temp_start_point = span_striaght1.point_on_straight(i)
        for multi in range(100):
            new_point = span_striaght2.point_on_straight(multi) +  temp_start_point
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
