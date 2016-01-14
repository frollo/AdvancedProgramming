from math import sqrt
from math import pi

class Shape (object):
    def calculate_perimeter (self):
        pass

    def calculate_area (self):
        pass

    def __eq__(self, other):
        return self.calculate_perimeter() == other.calculate_perimeter()

    def __lt__(self,other):
        return self.calculate_perimeter() < other.calculate_perimeter()

class Triangles (Shape):
    def __init__(self, side):
        self._side = side

    def calculate_area (self):
        return (sqrt(3)/4) * (self._side**2)

    def calculate_perimeter (self):
        return 3 * self._side

class Circles (Shape):
    def __init__ (self, radius):
        self._radius = radius

    def calculate_area(self):
        return pi * self._radius**2

    def calculate_perimeter(self):
        return 2 * pi * self._radius

class Rectangles (Shape):
    def __init__(self, side1, side2):
        self._side1 = side1
        self._side2 = side2

    def calculate_area(self):
        return self._side1 * self._side2

    def calculate_perimeter(self):
        return 2 * (self._side1 + self._side2)

class Squares (Rectangles):
    def __init__ (self, side):
        self._side1 = side
        self._side2 = side

class Pentagon (Shape):
    _nf = 0.688

    def __init__ (self, side):
        self._side = side

    def calculate_perimeter (self):
        return 5 * self._side

    def calculate_area (self):
        return (self._side * self._side * Pentagon._nf)/2

class Hexagon (Shape):
    _nf = (3*sqrt(3))/2
    def __init__ (self,side):
        self._side = side

    def calculate_perimeter(self):
        return self._side * 6

    def calculate_area(self):
        return Hexagon._nf * self._side**2

class SortedAreas:
    def __init__(self, ls):
        self._list = sorted(ls, key=lambda x: x.calculate_area())

    def __iter__(self):
        self._index = 0
        self._max = len(self._list)
        return self

    def __next__ (self):
        if self._index >= self._max: raise StopIteration
        cur = self._list[self._index]
        self._index += 1
        return cur
