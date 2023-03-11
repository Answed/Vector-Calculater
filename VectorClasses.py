import math as mt

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
        angle = mt.acos(scalar_product/(self.length() * other.length()))
        return mt.degrees(angle)
    

class Vector3(Vector2):
    def __init__(self, xValue, yValue, zValue) -> None:
        self.x = xValue
        self.y = yValue
        self.z = zValue
    
    # Function overrides which are requierd for vector math operations
    def __add__(self, other): # Allows that two Vector3s can be added to each other. Resulting Vector is a new Vector3 to ensure that no data gets corupted and easy working with different Vectors multiple times.
        return Vector2(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other): # Allows that two Vector2s can be subtracted from each other
        return Vector2(self.x - other.x, self.y - other.y, self.z - other.z) 
    def __mul__(self, other): # Allows to multiply a Vector3 with floats or intigers
        return Vector2(self.x * other, self.y * other, self.z * other)
    def __truediv__(self, other): # Allows to divide a Vector3 with floats or intigers
        return Vector2(self.x / other, self.y / other, self.z / other)
    def __str__(self):
        return "({} | {} | {})".format(self.x, self.y, self.z)

    # Special cases from vecotors
    def length(self): # Magnitude/lenght of the vector
        return mt.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normalize(self): # Calculates the normalized version of a Vector3
        lenghtOfVector = self.length()
        return Vector2(self.x / lenghtOfVector, self.y / lenghtOfVector, self.z / lenghtOfVector)
    
    # Calculations where another vector is required for 
    def scalar_product(self, other): # Allows to calculate the skalar from two vecotor3's 
        return((self.x * other.x )+ (self.y * other.y) + (self.z * other.z))
    
    def cross_product(self, other): # Creates a new Vector out of the old two. 
        new_x = self-y * other.z - self.z * other.y
        new_y = self.z * other.x - self.x * other.z
        new_z = self.x * other.y - self.y * other.x
        return Vector3(new_x, new_y, new_z)
    
    class Straight2D:
        def __init__(self, base_point, direction) -> None:
            self.base_point = base_point
            self.direction = direction
        
        def point_on_straight(self, multiplier):
            return Vector2(self.base_point + multiplier * self.direction)
        
        def convert_straight_to_equation(self):
            x_equation = "{}+{}x".format(self.base_point.x, self.direction.x)
            y_equation = "{}+{}x".format(self.base_point.y, self.direction.y)
            return [x_equation, y_equation]

        def distance_between_straights(self, other):
            helparea = self.direction.scalar_product(other.base_point) # Calculates the vale of the helparea which is needed for the calculation of the point from the straight
        

    
    class Straight3D(Straight2D):
                
        def point_on_straight(self, multiplier):
            return Vector3(self.base_point + multiplier * self.direction)
        
        def convert_straight_to_equation(self):
            x_equation = "{}+{}x".format(self.base_point.x, self.direction.x)
            y_equation = "{}+{}x".format(self.base_point.y, self.direction.y)
            z_equation = "{}+{}x".format(self.base_point.z, self.direction.z)
            return [x_equation, y_equation, z_equation]