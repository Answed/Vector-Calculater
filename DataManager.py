from VectorClasses import *
import re
import CalculatorMessages as CM

saved_2D_dic = {}
saved_3D_dic = {}
vector2_pattern = r"\(\s*\d+\s*\|\s*\d+\s*\)"
vector3_pattern = r"\(\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\)"
name_pattern = r"\b\w{2,}\b" #  Pattern to find a name in an Input

def FindOrCreate_3D_vectors(vectors):
    found_vectors = []
    for vector in vectors:
        if re.match(vector3_pattern, vector):
            found_vectors.append(create_vector3(vector))
        else : 
            try:
                found_vectors.append(saved_3D_dic[vector])
            except(KeyError): CM.WrongInput("This Vector doesn't exist")
    return found_vectors

def  create_vector2(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector2(float(vector_values[0]), float(vector_values[1]))

def create_straight2D(matches):
    tempVectors = []
    for match in matches:
        if re.match(vector2_pattern, match):
            tempVectors.append(create_vector2(match))
        else : 
            try:
                print(match)
                tempVectors.append(saved_2D_dic[match])
            except(KeyError): CM.WrongInput("This Vector doesn't exist")
    return Straight2D(tempVectors[0], tempVectors[1])

def create_vector3(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector3(vector_values[0], vector_values[1], vector_values[2])

def create_straight3D(matches):
    tempVectors = FindOrCreate_3D_vectors(matches)
    return Straight3D(tempVectors[0], tempVectors[1])
    
def create_area(matches):
    tempVectors = FindOrCreate_3D_vectors(matches)
    return Area(tempVectors[0], tempVectors[1], tempVectors[2])

def save_Vector2(name, value):
    if re.match(vector2_pattern, value):
        saved_2D_dic[name] = create_vector2(value)
    else: CM.WrongInput("keep in mind it has to be (number|number)")

def save_Straight2D(name, value):
    matches = re.findall(name_pattern + "|" + vector2_pattern, value)
    if (len(matches) == 2):
        saved_2D_dic[name] = create_straight2D(matches)
    else: CM.WrongInput("Check your Inputs again")    

def save_Vector3D(name, value):
    if re.match(vector3_pattern, value):
        saved_3D_dic[name] = create_vector3(value)
    else: CM.WrongInput("keep in mind it has to be (number|number|number)")

def save_Straight3D(name, value):
    matches = re.findall(name_pattern + "|" + vector3_pattern, value)
    if (len(matches) == 2):
        saved_3D_dic[name] = create_straight3D(matches)
    else: CM.WrongInput("Check your Inputs again")  

def save_Area(name, value):
    matches = re.findall(name_pattern + "|" + vector3_pattern)
    if (len(matches) == 3):
        saved_3D_dic[name] = create_area(value)
    else: CM.WrongInput("Check your Inputs again")  

def find_vector(kind_of_Vector, name_of_vector):
    try:
        match kind_of_Vector:
            case "Vector2":
               return saved_2D_dic[name_of_vector]
            case "Vector3":
               return saved_3D_dic[name_of_vector]
    except KeyError:
        CM.WrongInput("That Vector does not exist")
    finally:
        return 0