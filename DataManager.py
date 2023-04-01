from VectorClasses import *
import re
import CalculatorMessages as CM

saved_vector2_dic = {}
saved_vector3_dic = {}
vector2_pattern = r"^\(\s*\d+\s*\|\s*\d+\s*\)$"
vector3_pattern = r"^\(\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\)$"

def  create_vector2(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector2(float(vector_values[0]), float(vector_values[1]))
def create_vector3(value: str):
    vector_values = re.findall(r"\d+", value)
    return Vector3(vector_values[0], vector_values[1], vector_values[2])

def save_Vector2(name, value):
    if re.match(vector2_pattern, value):
        saved_vector2_dic[name] = create_vector2(value)
        print(saved_vector2_dic)
    else: CM.WrongInput("Something went wrong with your input\n keep in mind it has to be (number|number)")

def save_Vector3(name, value):
    if re.match(vector3_pattern, value):
        saved_vector3_dic[name] = create_vector3(value)
    else: CM.WrongInput("Something went wrong with your input\n keep in mind it has to be (number|number|number)")
    
def find_vector(kind_of_Vector, name_of_vector):
    try:
        match kind_of_Vector:
            case "Vector2":
               return saved_vector2_dic[name_of_vector]
            case "Vector3":
               return saved_vector3_dic[name_of_vector]
    except KeyError:
        CM.WrongInput("That Vector does not exist")
    finally:
        return 0