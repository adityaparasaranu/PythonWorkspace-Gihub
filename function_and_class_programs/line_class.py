class Line:
    def __init__(self, side, length_of_line):
        self.length_of_line = length_of_line
        self.side = side

    def get_perimeter(self):
        return self.side * self.length_of_line


class Square(Line):
    def finalOutput(self):
        print("The perimeter of Square is :", self.get_perimeter())


class Polygon(Line):
    def finalOutput(self):
        print("The perimeter of Polygon is :", self.get_perimeter())


class Triangle(Line) :
    def finalOutput(self):
        print("The perimeter of Triangle is :", self.get_perimeter())

square = Square(side= 4, length_of_line= 5)
square.finalOutput()

polygon = Polygon(side= 5, length_of_line= 10)
polygon.finalOutput()

trinagle = Triangle(side= 3, length_of_line= 10)
trinagle.finalOutput()