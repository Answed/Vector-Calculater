from VectorClasses import *
import re

saved_vector2_dic = {}
saved_vector3_dic = {}
vector2_pattern = r"^\(\s*\d+\s*\|\s*\d+\s*\)$"
vector3_pattern = r"^\(\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\)$"

def  create_vector2(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector2(vector_values[0], vector_values[1])
def create_vector3(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector3(vector_values[0], vector_values[1], vector_values[2])

def save_Vector2(name, value):
    if re.match(vector2_pattern, value):
        saved_vector2_dic[name] = create_vector2(value)
    else: print("Something went wrong with your input")

def save_Vector3(name, value):
    if re.match(vector3_pattern, value):
        saved_vector3_dic[name] = create_vector3(value)
    else: print("Something went wrong with your input")
    

