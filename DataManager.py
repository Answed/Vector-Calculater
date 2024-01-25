from VectorClasses import *
import re
import CalculatorMessages as CM

# This file manages all of the saved objects and also creates new ones if neccessary/required.

saved_objects_dic = {}
vector2_pattern = r"\(\s*\d+\s*\|\s*\d+\s*\)"
vector3_pattern = r"\(\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\)"
operators = r"[-+*/]"
name_pattern = r"\b\w{2,}\b"  # Pattern to find a name in an Input


def varify_Vectors(vectors):
    tag_3D = 0
    tag_2D = 0
    for vector in vectors:
        if vector.tag == "3D":
            tag_3D += 1
        else:
            tag_2D += 1
    if tag_3D == len(vectors) or tag_2D == len(vectors):
        return True
    else:
        return False


def FindMathOperator(input):
    matches = re.findall(operators, input)
    if len(matches) == 0:
        CM.WrongInput("You forgot to actually say what to do with the vectors")
    else:
        return matches


def FindOrCreate_2D_vectors(vectors):
    found_vectors = []
    for vector in vectors:
        if re.match(vector2_pattern, vector):
            found_vectors.append(create_vector2(vector))
        else:
            try:
                found_vectors.append(saved_objects_dic[vector])
                found_vectors.append(saved_objects_dic[vector].tag)
            except KeyError:
                CM.WrongInput("This Vector doesn't exist")
    return found_vectors


def FindOrCreate_3D_vectors(vectors):
    found_vectors = []
    for vector in vectors:
        if re.match(vector3_pattern, vector):
            found_vectors.append(create_vector3(vector))
        else:
            try:
                if saved_objects_dic[vector] is Straight3D:
                    found_vectors.append(saved_objects_dic[vector].base_point)
                    found_vectors.append(saved_objects_dic[vector].direction)
                else:
                    found_vectors.append(saved_objects_dic[vector])
            except KeyError:
                CM.WrongInput("This Vector doesn't exist")
    return found_vectors


def FindVectorsInInput(input):
    matches = re.findall(name_pattern + "|" + vector3_pattern + "|" + vector2_pattern, input)
    found_vectors = []
    if len(matches) < 2:  # Matches has to be over 2 otherwise you cannot use it for calculations
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
                except KeyError:
                    print("This Object doesn't exist")
        return found_vectors


def create_vector2(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector2(float(vector_values[0]), float(vector_values[1]), tag="2D")


def create_straight2D(matches):
    tempVectors = FindOrCreate_2D_vectors(matches)
    return Straight2D(tempVectors[0], tempVectors[1], tag="2D")


def create_vector3(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector3(float(vector_values[0]), float(vector_values[1]), float(vector_values[2]), tag="3D")


def create_straight3D(matches):
    tempVectors = FindOrCreate_3D_vectors(matches)
    return Straight3D(tempVectors[0], tempVectors[1], tag="3D")


def create_area(matches):
    tempVectors = FindOrCreate_3D_vectors(matches)
    print(tempVectors)
    return Area(tempVectors[0], tempVectors[1], tempVectors[2], tag="3D")


def save_Vector2(name, value):
    if re.match(vector2_pattern, value):
        saved_objects_dic[name] = create_vector2(value)
    else:
        CM.WrongInput("keep in mind it has to be (number|number)")


def save_Straight2D(name, value):
    matches = re.findall(name_pattern + "|" + vector2_pattern, value)
    if len(matches) == 2:
        saved_objects_dic[name] = create_straight2D(matches)
    else:
        CM.WrongInput("Check your Inputs again")


def save_Vector3D(name, value):
    if re.match(vector3_pattern, value):
        saved_objects_dic[name] = create_vector3(value)
    else:
        CM.WrongInput("keep in mind it has to be (number|number|number)")


def save_Straight3D(name, value):
    matches = re.findall(name_pattern + "|" + vector3_pattern, value)
    if len(matches) == 2:
        saved_objects_dic[name] = create_straight3D(matches)
    else:
        CM.WrongInput("Check your Inputs again")


def save_Area(name, value):
    matches = re.findall(name_pattern + "|" + vector3_pattern, value)
    if len(matches) == 3 or len(matches) == 2:
        saved_objects_dic[name] = create_area(matches)
    else:
        CM.WrongInput("Check your Inputs again")
