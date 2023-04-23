import math as mt
import CalculatorMessages as CM
# Describes a vector with two dimensions.
class Vector2:
    def __init__(self, xValue, yValue) -> None:
        self.x = xValue
        self.y = yValue

    # Function overrides which are requierd for vector math operations
    def __add__(self, other): # Allows that two Vector2s can be added to each other. Resulting Vector is a new Vector2 to ensure that no data gets corupted and easy working with different Vectors multiple times.
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other): # Allows that two Vector2s can be subtracted from each other
        return Vector2(self.x - other.x, self.y - other.y) 
    def __mul__(self, other): # Allows to multiply a Vector2 with floats or intigers
        return Vector2(self.x * other, self.y * other)
    def __truediv__(self, other): # Allows to divide a Vector2 with floats or intigers
        return Vector2(self.x / other, self.y / other)
    def __str__(self):
        return "({} | {})".format(self.x, self.y)
    
    # Special cases from vecotors
    def length(self): # Magnitude/lenght of the vector
        return mt.sqrt(self.x**2 + self.y**2)
    def normalize(self): # Calculates the normalized version of a Vector2
        lenghtOfVector = self.length()
        return Vector2(self.x / lenghtOfVector, self.y / lenghtOfVector)
    
    # Calculations where another vector is required for 
    def scalar_product(self, other): # Allows to calculate the skalar from two vecotor2's
        return(self.x * other.y + self.y * other.y)
    def cross_product(self, other):
        return self.x * other.y - self.y - other.x
    def angle_between_vectors(self, other):
        scalar_product = self.scalar_product(other)
        try:
            angle = mt.acos(scalar_product/(self.length() * other.length()))
        except(ValueError):
            CM.WrongInput("The values from your inputs are to high.\n Try a smaller version of them!")
        return mt.degrees(angle)

class Vector3(Vector2):
    def __init__(self, xValue, yValue, zValue) -> None:
        self.x = xValue
        self.y = yValue
        self.z = zValue
    
    # Function overrides which are requierd for vector math operations
    def __add__(self, other): # Allows that two Vector3s can be added to each other. Resulting Vector is a new Vector3 to ensure that no data gets corupted and easy working with different Vectors multiple times.
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other): # Allows that two Vector2s can be subtracted from each other
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z) 
    def __mul__(self, other): # Allows to multiply a Vector3 with floats or intigers
        return Vector3(self.x * other, self.y * other, self.z * other)
    def __truediv__(self, other): # Allows to divide a Vector3 with floats or intigers
        return Vector3(self.x / other, self.y / other, self.z / other)
    def __str__(self):
        return "({} | {} | {})".format(self.x, self.y, self.z)

    # Special cases from vecotors
    def length(self): # Magnitude/lenght of the vector
        return mt.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normalize(self): # Calculates the normalized version of a Vector3
        lenghtOfVector = self.length()
        return Vector3(self.x / lenghtOfVector, self.y / lenghtOfVector, self.z / lenghtOfVector)
    
    # Calculations where another vector is required for 
    def scalar_product(self, other): # Allows to calculate the skalar from two vecotor3's 
        return((self.x * other.x)+ (self.y * other.y) + (self.z * other.z))
    
    def cross_product(self, other): # Creates a new Vector out of the old two. 
        new_x = self.y * other.z - self.z * other.y
        new_y = self.z * other.x - self.x * other.z
        new_z = self.x * other.y - self.y * other.x
        return Vector3(new_x, new_y, new_z)
    
class Straight2D:
    def __init__(self, base_point : Vector2, direction: Vector2) -> None:
        self.base_point = base_point
        self.direction = direction
        
    def point_on_straight(self, multiplier):
        temp_vector = self.direction * multiplier
        return self.base_point + temp_vector

    def point_is_on_straight(self, point: Vector2):
        x_row_multiplikator = (point.x-self.base_point.x)/self.direction.x
        y_row_multiplikator = (point.y-self.base_point.y)/self.direction.y
        if(x_row_multiplikator == y_row_multiplikator): return True
        else: return False

    def convert_straight_to_equation(self):
        x_equation = "{}+{}t".format(self.base_point.x, self.direction.x)
        y_equation = "{}+{}t".format(self.base_point.y, self.direction.y)

    def distance_between_straights(self, other):
        helparea = self.direction.scalar_product(other.base_point) # Calculates the normal vector of the helparea which is needed for the calculation of the point from the straight
        number_without_parameter = self.direction.scalar_product(self.base_point) # Calculation is divided in to parts to make the finding of the parameter a lot easier
        helparea -= number_without_parameter 
        number_with_parameter = self.direction.scalar_product(self.direction)
        parameter = helparea / number_with_parameter 
        distance_vector = self.point_on_straight(parameter) - other.base_point # Calculates the new point and subtracts the other point from it to find the new position vektors
        return distance_vector.length()
    
class Straight3D(Straight2D):
    def __init__(self, base_point : Vector3, direction: Vector3) -> None:
        self.base_point = base_point
        self.direction = direction
    
    def point_is_on_straight(self, point: Vector3):
        x_row_multiplikator = (point.x-self.base_point.x)/self.direction.x
        y_row_multiplikator = (point.y-self.base_point.y)/self.direction.y
        z_row_multiplikator = (point.z-self.base_point.z)/self.direction.z
        if(x_row_multiplikator == y_row_multiplikator == z_row_multiplikator): return True
        else: return False

    def convert_straight_to_equation(self):
        x_equation = "{}+{}t".format(self.base_point.x, self.direction.x)
        y_equation = "{}+{}t".format(self.base_point.y, self.direction.y)
        z_equation = "{}+{}t".format(self.base_point.z, self.direction.z)
        return [x_equation, y_equation, z_equation]

class Area:
    def __init__(self, base_point: Vector3, span_vector1: Vector3, span_vector2: Vector3) -> None:
        self.base_point = base_point
        self.span_vector1 = span_vector1
        self.span_vector2 = span_vector2
        self.normal_vector = self.span_vector1.cross_product(self.span_vector2)

    def point_is_on_area(self, point): # Basically is it the normal form from the area equation
        temp_point = point - self.base_point
        if (temp_point.scalar_product(self.normal_vector()) == 0):return True
        else: return False

    def coordinate_form(self): # Is used to calculate the value the equasion has to have in oder that the end result is right
        return self.normal_vector.scalar_product(self.base_point)
    
    def print_coordinate_form(self):
        check_value = self.coordinate_form()
        print("{}x + {}z + {}y = {}".format(self.normal_vector.x,self.normal_vector.y,self.normal_vector.z, check_value))
    
    def distance_to_point(self, point): # Based on the Hesse normal form
        check_value = self.coordinate_form()
        return abs((self.normal_vector.scalar_product(point) - check_value)/ self.normal_vector.length()) # Always returns the absolut Value so always returns the positiv value.