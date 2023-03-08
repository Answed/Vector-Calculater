import math as mt

# Describes a vector with two dimensions.
class Vector2:
    def __init__(self, xValue, yValue) -> None:
        self.x = xValue
        self.y = yValue
    def __add__(self, other): # Allows that two Vector2s can be added to each other. Resulting Vector is a new Vector2 to ensure that no data gets corupted and easy working with different Vectors multiple times.
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other): # Allows that two Vector2s can be subtracted from each other
        return Vector2(self.x - other.x, self.y - other.y) 
    def __mul__(self, other): # Allows to multiply a Vector2 with floats or intigers
        return Vector2(self.x * other, self.y * other)
    def __truediv__(self, other): # Allows to divide a Vector2 with floats or intigers
        return Vector2(self.x / other, self.y / other)

    def scalar_product(self, other): # Allows to calculate the skalar from two vecotor2's
        return(self.x * other.y + self.y * other.y)

    def length(self): 
        return mt.sqrt(self.x**2 + self.y**2)
    def normalize(self): # Calculates the normalized version of a Vector2
        lenghtOfVector = self.length()
        return Vector2(self.x / lenghtOfVector, self.y / lenghtOfVector)

class Vector3:
    def __init__(self, xValue, yValue, zValue) -> None:
        self.x = xValue
        self.y = yValue
        self.z = zValue
    def __add__(self, other): # Allows that two Vector3s can be added to each other. Resulting Vector is a new Vector3 to ensure that no data gets corupted and easy working with different Vectors multiple times.
        return Vector2(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other): # Allows that two Vector2s can be subtracted from each other
        return Vector2(self.x - other.x, self.y - other.y, self.z - other.z) 
    def __mul__(self, other): # Allows to multiply a Vector3 with floats or intigers
        return Vector2(self.x * other, self.y * other, self.z * other)
    def __truediv__(self, other): # Allows to divide a Vector3 with floats or intigers
        return Vector2(self.x / other, self.y / other, self.z / other)

    def scalar_product(self, other): # Allows to calculate the skalar from two vecotor3's 
        return(self.x * other.y + self.y * other.y + self.z * other.z)

    def length(self): 
        return mt.sqrt(self.x**2 + self.y**2 + self.z)
    def normalize(self): # Calculates the normalized version of a Vector3
        lenghtOfVector = self.length()
        return Vector2(self.x / lenghtOfVector, self.y / lenghtOfVector, self.z / lenghtOfVector)