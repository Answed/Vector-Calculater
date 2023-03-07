import math as mt

# Describes a vector with two dimensions.
class Vector2:
    def __init__(self, xValue, yValue) -> None:
        self._x = xValue
        self._y = yValue
    def __add__(self, other): # Allows that two Vector2s can be added to each other. Resulting Vector is a new Vector2 to ensure that no data gets corupted and easy working with different Vectors multiple times.
        return Vector2(self._x + other._x, self._y + other._y)
    def __sub__(self, other): # Allows that two Vector2s can be subtracted from each other
        return Vector2(self._x - other._x, self._y - other._y) 
    def __mul__(self, other): # Allows to multiply a Vector2 with floats or intigers
        return Vector2(self._x * other, self._y * other)
    def __truediv__(self, other): # Allows to divide a Vector2 with floats or intigers
        return Vector2(self._x / other, self._y / other)

    def length(self): 
        return mt.sqrt(self._x**2 + self._y**2)
    
    def normalize(self): # Calculates the normalized version of a Vector2
        lenghtOfVector = self.length()
        return Vector2(self._x / lenghtOfVector, self._y / lenghtOfVector)

class Vector3:
    def __init__(self, xValue, yValue, zValue) -> None:
        self._x = xValue
        self._y = yValue
        self._z = zValue
    def __add__(self, other): # Allows that two Vector3s can be added to each other. Resulting Vector is a new Vector3 to ensure that no data gets corupted and easy working with different Vectors multiple times.
        return Vector2(self._x + other._x, self._y + other._y, self._z + other._z)
    def __sub__(self, other): # Allows that two Vector2s can be subtracted from each other
        return Vector2(self._x - other._x, self._y - other._y, self._z - other._z) 
    def __mul__(self, other): # Allows to multiply a Vector3 with floats or intigers
        return Vector2(self._x * other, self._y * other, self._z * other)
    def __truediv__(self, other): # Allows to divide a Vector3 with floats or intigers
        return Vector2(self._x / other, self._y / other, self._z / other)

    def length(self): 
        return mt.sqrt(self._x**2 + self._y**2 + self._z)
    
    def normalize(self): # Calculates the normalized version of a Vector3
        lenghtOfVector = self.length()
        return Vector2(self._x / lenghtOfVector, self._y / lenghtOfVector, self._z / lenghtOfVector)