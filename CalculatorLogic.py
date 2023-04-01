from VectorClasses import*
import math as mt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import DataManager as DM


def generate_vector2D(vector: Vector2):
    lenght = vector.length()
    x = []
    y = []
    for i in range(int(lenght)):
        new_point = vector * i
        x.append(new_point.x)
        y.append(new_point.y)
    return[x, y]

def generate_straight2d(straight: Straight2D):
    x = []
    y = []
    for i in range(100): # Will be changeable later in development
        new_point = straight.point_on_straight(i)
        x.append(new_point.x)
        y.append(new_point.y)
    return [x, y]

def generate_vector3D(vector: Vector3):
    lenght = vector.length()
    x = []
    y = []
    z = []
    for i in range(int(lenght)):
        new_point = vector * i
        x.append(new_point.x)
        y.append(new_point.y)
        z.append(new_point.z)
    return[x, y, z]

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
        for multi in range(100): # Generates for everypoint from the span_striaght1 a new clone of span_striaght2
            new_point = span_striaght2.point_on_straight(multi) +  temp_start_point
            x.append(new_point.x)
            y.append(new_point.y)
            z.append(new_point.z)
    return [x, y, z]

# Used to plot all of the specifics made in the ui and display them at the same time.
def plot_vector2D(*vectors: Vector2):
    for vector in vectors:
        x, y = generate_vector2D(vector)
        plt.plot(x, y)

def plot_straight2D(*straights: Straight2D):
    for straight in straights:
        x, y = generate_straight2d(straight)
        plt.plot(x, y)

def plot_vector3D(*vectors: Vector3):
    fig = plt.figure()
    ax = plt.axes(projection = "3d")
    for vector in vectors:
        x, y, z = generate_vector2D(vector)
        plt.plot(x, y, z)

def plot_straight3D(*straights: Straight3D):
    fig = plt.figure()
    ax = plt.axes(projection = "3d")
    for straight in straights:
        x, y, z = generate_straight3d(straight)
        ax.plot3D(x, y, z)

def plot_area(*areas: Area):
    fig = plt.figure()
    ax = plt.axes(projection = "3d")
    for area in areas:
        x, y, z = generate_area(area)
        ax.plot3D(x, y, z)

def show2D(args):
    for arg in args:
        value = DM.saved_vector2_dic[arg]
        if (type(value) == Vector2):
            plot_vector2D(value)
        if(type(value) == Straight2D):
            plot_straight2D(value)
    plt.show()

def show3D(args):
    for arg in args:
        value = DM.saved_vector3_dic[arg]
        if(type(value) == Vector3):
            plot_vector3D(value)
        if(type(value) == Straight3D):
            plot_straight3D
        if(type(value) == Area):
            plot_area(value)
    plt.show()