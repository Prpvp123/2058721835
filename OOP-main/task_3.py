import math


class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.hypotenuse = math.sqrt(a ** 2 + b ** 2)  # гипотенузa

    def area(self):
        area = 0.5 * self.a * self.b
        return area

    def perimeter(self):
        perimeter = self.a + self.b + self.hypotenuse
        return perimeter


tri = Triangle(3, 5)

area = tri.area()
perimeter = tri.perimeter()

print(f"Площадь треугольника: {area}\nПериметр треугольника: {perimeter}")
