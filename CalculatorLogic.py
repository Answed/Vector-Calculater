from VectorClasses import*
import math as mt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import DataManager as DM
import CalculatorMessages as CM

# This file hanldes all the calculations, needed for displaying objects or calculating user inputs.

def generate_vector2D(vector: Vector2):
    lenght = vector.length()
    x = []
    y = []
    for i in range(int(lenght)):
        new_point = vector * i
        x.append(new_point.x)
        y.append(new_point.y)
    return[x, y]

def generate_straight2d(straight: Straight2D, length: int):
    x = []
    y = []
    for i in range(length):
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

def generate_straight3d(straight: Straight3D, length: int):
    x = []
    y = []
    z = []
    for i in range(length):
        new_point = straight.point_on_straight(i)
        x.append(new_point.x)
        y.append(new_point.y)
        z.append(new_point.z)
    return [x, y, z]

def generate_area(area: Area, length: int):
    x = []
    y = []
    z = []
    span_striaght1 = Straight3D(area.base_point, area.span_vector1) 
    span_striaght2 = Straight3D(area.base_point, area.span_vector2)
    for i in range(length):
        temp_start_point = span_striaght1.point_on_straight(i)
        for multi in range(length): # Generates for everypoint from the span_striaght1 a new clone of span_striaght2
            new_point = span_striaght2.point_on_straight(multi) +  temp_start_point
            x.append(new_point.x)
            y.append(new_point.y)
            z.append(new_point.z)
    return [x, y, z]

# Used to plot all of the specifics made in the ui and display them at the same time.
def plot_vector2D(vector: Vector2):
    x, y = generate_vector2D(vector)
    plt.plot(x, y)

def plot_straight2D(straight: Straight2D):
    x, y = generate_straight2d(straight, 100)
    plt.plot(x, y)

def plot_vector3D(vector: Vector3):
    fig = plt.figure()
    ax = plt.axes(projection = "3d")
    x, y, z = generate_vector3D(vector)
    plt.plot(x, y, z)

def plot_straight3D(straight: Straight3D):
    fig = plt.figure()
    ax = plt.axes(projection = "3d")
    x, y, z = generate_straight3d(straight, 100)
    ax.plot3D(x, y, z)

def plot_area(area: Area):
    fig = plt.figure()
    ax = plt.axes(projection = "3d")
    x, y, z = generate_area(area, 100)
    ax.plot3D(x, y, z)

def show2D(args):
    for arg in args:
        value = DM.saved_objects_dic[arg]
        if (type(value) == Vector2):
            plot_vector2D(value)
        if(type(value) == Straight2D):
            plot_straight2D(value)
    plt.show()

def show3D(args):
    for arg in args:
        value = DM.saved_objects_dic[arg]
        if(type(value) == Vector3):
            plot_vector3D(value)
        if(type(value) == Straight3D):
            plot_straight3D(value)
        if(type(value) == Area):
            plot_area(value)
    plt.show()

def calculate_angel(vectors):
    vectors = DM.FindVectorsInInput(vectors)
    if (DM.varify_Vectors(vectors)):
        CM.Result("The angle between the vector {} and {}\n is {}".format(vectors[0], vectors[1], vectors[0].angle_between_vectors(vectors[1])))

def calculate_sum(vectors):
    vectors = DM.FindVectorsInInput(vectors)
    if(DM.varify_Vectors(vectors)):
        for i in range(1, len(vectors)):
            vectors[0] += vectors[i]
        CM.Result("The sum of the vectors is {}".format(vectors[0]))

def calculate_distance(vectors):
    vectors = DM.FindVectorsInInput(vectors)
    if(DM.varify_Vectors(vectors)):
        CM.Result("The distance between the straight {} and {}\n is {}".format(vectors[0], vectors[1], vectors[0].distance_between_straights(vectors[1])))

def check_area(vectors):
    if(vectors[0].point_is_on_area(vectors[1])):
        CM.Result("The Point {} is on the Area {}".format(vectors[1], vectors[0]))
    else: CM.Result("The Point {} is not on the Area {}".format(vectors[1], vectors[2]))

def check_straight(vectors):
    if(vectors[0].point_is_on_straight(vectors[1])):
        CM.Result("The Point {} is on the Straight {}".format(vectors[1], vectors[0]))
    else: CM.Result("The Point {} is not on the Straight {}".format(vectors[1], vectors[2]))

def check_point(input):
    vectors = DM.FindVectorsInInput(input)
    if(type(vectors[0])== Area):
        check_area(vectors)
    elif(type(vectors[0]) == Straight2D or type(vectors[0]) == Straight3D):
        check_straight(vectors)
        