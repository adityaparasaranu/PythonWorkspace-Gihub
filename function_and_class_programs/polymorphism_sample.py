class Shape :
    def __init__(self, length):
        self.length = length

    def area(self):
        area = self.length ** 2
        self.area = area

class Square(Shape) :
    def area(self):
        area = self.length * self.length
        return area


class Circle(Shape) :
    def area(self):
        area = (22/7) * self.length
        return area


square = Square(2)
print(square.area())

circle = Circle(7)
print(circle.area())