class Square:
    def __init__(self, side):
        self.side = side

    def per(self, side):
        return side * 4

    def pl(self, side):
        return side ** 2


side = 5
square = Square(side)
area = square.pl(side)
perimetr = square.per(side)

print(area)
print(perimetr)
