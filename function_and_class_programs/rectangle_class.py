class Rectangle :
    def __init__(self, length , breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square(Rectangle) :
    def __init__(self,side):
        super().__init__(side, side)
    # The area is not been called here as the base class itself returns the area which is side * side
    # Here the Inheritance concept is used


class Trinagle(Rectangle) :
    def area(self):
        return (1/2) * super().area()


class Parallelogram(Rectangle) :
    pass

rectangle = Rectangle(2 , 3)
print(rectangle.area())

square = Square(2)
print(square.area())

triangle = Trinagle(2 , 3)
print(triangle.area())

parallelogram = Parallelogram(2 , 3)
print(parallelogram.area())