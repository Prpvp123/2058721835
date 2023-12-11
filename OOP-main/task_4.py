import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, coordinate):
        return math.sqrt(
            (self.x - coordinate.x) ** 2 + (self.y - coordinate.y) ** 2)


class Triangle:
    def __init__(self, coordinate_a, coordinate_b, coordinate_c):
        self.point_a = coordinate_a
        self.point_b = coordinate_b
        self.point_c = coordinate_c

    def perimeter(self):
        side_ab = self.point_a.distance(self.point_b)
        side_bc = self.point_b.distance(self.point_c)
        side_ca = self.point_c.distance(self.point_a)
        return side_ab + side_bc + side_ca


coordinate_a = Point(2, 4)
coordinate_b = Point(6, 9)
coordinate_c = Point(6, 0)

triangle = Triangle(coordinate_a, coordinate_b, coordinate_c)

perimeter = triangle.perimeter()
print("Периметр треугольника ABC:", perimeter)
