from VectorClasses import *
import re
import CalculatorMessages as CM

saved_objects_dic = {}
vector2_pattern = r"\(\s*\d+\s*\|\s*\d+\s*\)"
vector3_pattern = r"\(\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\)"
name_pattern = r"\b\w{2,}\b" #  Pattern to find a name in an Input

# Check if all inputs are of the same type
def varify_Vectors(vectors):
    sameType = False
    for i in range(len(vectors) - 1):  # -2 Because we dont want to go through the last object of the list
        if(type(vectors[i]) == type(vectors[i+1])): sameType = True
        else: sameType = False
    return sameType

def FindOrCreate_2D_vectors(vectors):
    found_vectors = []
    for vector in vectors:
        if re.match(vector2_pattern, vector):
            found_vectors.append(create_vector2(vector))
        else : 
            try:
                found_vectors.append(saved_objects_dic[vector])
            except(KeyError): CM.WrongInput("This Vector doesn't exist")
    return found_vectors

def FindOrCreate_3D_vectors(vectors):
    found_vectors = []
    for vector in vectors:
        if re.match(vector3_pattern, vector):
            found_vectors.append(create_vector3(vector))
        else : 
            try:
                if (type(saved_objects_dic[vector]) == Straight3D):
                    found_vectors.append(saved_objects_dic[vector].base_point)
                    found_vectors.append(saved_objects_dic[vector].direction)
                else: found_vectors.append(saved_objects_dic[vector])
            except(KeyError): CM.WrongInput("This Vector doesn't exist")
    return found_vectors

def FindVectorsInInput(input):
    matches = re.findall(name_pattern + "|" + vector3_pattern + "|" + vector2_pattern, input)
    found_vectors = []
    if (len(matches) < 2):
        CM.WrongInput("Check your Inputs again")
    else: 
        for vector in matches:
            if re.match(vector2_pattern, vector):
                found_vectors.append(create_vector2(vector))
            elif re.match(vector3_pattern, vector):
                found_vectors.append(create_vector3(vector))
            else: 
                try:
                    found_vectors.append(saved_objects_dic[vector])
                except(KeyError): print("One of the options is not available")
        return found_vectors

def  create_vector2(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector2(float(vector_values[0]), float(vector_values[1]))

def create_straight2D(matches):
    tempVectors = FindOrCreate_2D_vectors(matches)
    return Straight2D(tempVectors[0], tempVectors[1])

def create_vector3(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector3(float(vector_values[0]), float(vector_values[1]), float(vector_values[2]))

def create_straight3D(matches):
    tempVectors = FindOrCreate_3D_vectors(matches)
    return Straight3D(tempVectors[0], tempVectors[1])
    
def create_area(matches):
    tempVectors = FindOrCreate_3D_vectors(matches)
    return Area(tempVectors[0], tempVectors[1], tempVectors[2])

def save_Vector2(name, value):
    if re.match(vector2_pattern, value):
        saved_objects_dic[name] = create_vector2(value)
    else: CM.WrongInput("keep in mind it has to be (number|number)")

def save_Straight2D(name, value):
    matches = re.findall(name_pattern + "|" + vector2_pattern, value)
    if (len(matches) == 2):
        saved_objects_dic[name] = create_straight2D(matches)
    else: CM.WrongInput("Check your Inputs again")    

def save_Vector3D(name, value):
    if re.match(vector3_pattern, value):
        saved_objects_dic[name] = create_vector3(value)
    else: CM.WrongInput("keep in mind it has to be (number|number|number)")

def save_Straight3D(name, value):
    matches = re.findall(name_pattern + "|" + vector3_pattern, value)
    if (len(matches) == 2):
        saved_objects_dic[name] = create_straight3D(matches)
    else: CM.WrongInput("Check your Inputs again")  

def save_Area(name, value):
    matches = re.findall(name_pattern + "|" + vector3_pattern, value)
    if (len(matches) == 3 or len(matches) == 2):
        saved_objects_dic[name] = create_area(matches)
    else: CM.WrongInput("Check your Inputs again")  
