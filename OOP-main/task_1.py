class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5, 6)
point3 = Point3D(7, 8, 9)

print("Point 1:", point1)
print("Point 2:", point2)
print("Point 3:", point3)

point1.z = 10

print("\nПосле изменения класса Point3D:")
print("Point 1:", point1)
print("Point 2:", point2)
print("Point 3:", point3)

point2.x = 100

print("\nПосле изменения экземпляра Point3D (point2):")
print("Point 1:", point1)
print("Point 2:", point2)
print("Point 3:", point3)
