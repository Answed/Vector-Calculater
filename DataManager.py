from VectorClasses import *
import re
import CalculatorMessages as CM

saved_2D_dic = {}
saved_vector3_dic = {}
vector2_pattern = r"\(\s*\d+\s*\|\s*\d+\s*\)"
vector3_pattern = r"^\(\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\)$"
name_pattern = r"\b\w{2,}\b" #  Pattern to find a name in an Input

def  create_vector2(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector2(float(vector_values[0]), float(vector_values[1]))
def create_vector3(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector3(vector_values[0], vector_values[1], vector_values[2])

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

def save_Vector2(name, value):
    if re.match(vector2_pattern, value):
        saved_2D_dic[name] = create_vector2(value)
    else: CM.WrongInput("keep in mind it has to be (number|number)")

def save_Straight2D(name, value):
    matches = re.findall(name_pattern + "|" + vector2_pattern, value)
    if (len(matches) > 1 and len(matches) < 3):
        saved_2D_dic[name] = create_straight2D(matches)
    else: CM.WrongInput("Check your Inputs again")    

def save_Vector3(name, value):
    if re.match(vector3_pattern, value):
        saved_vector3_dic[name] = create_vector3(value)
    else: CM.WrongInput("keep in mind it has to be (number|number|number)")
    
def find_vector(kind_of_Vector, name_of_vector):
    try:
        match kind_of_Vector:
            case "Vector2":
               return saved_2D_dic[name_of_vector]
            case "Vector3":
               return saved_vector3_dic[name_of_vector]
    except KeyError:
        CM.WrongInput("That Vector does not exist")
    finally:
        return 0