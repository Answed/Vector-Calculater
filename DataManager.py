from VectorClasses import *
import re

saved_vector2_dic = {}
vector2_pattern = r"^\(\s*\d+\s*\|\s*\d+\s*\)$"

def  create_vector2(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector2(vector_values[0], vector_values[1])

def save_Vector2(name, value):
    print(value)
    if re.match(vector2_pattern, value):
        saved_vector2_dic[name] = create_vector2(value)
        print(saved_vector2_dic)
    else: print("Something went wrong with your input")
    

