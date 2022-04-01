class Animal :
    def __init__(self , name):
        print(f"{name} has four legs")
        self.name = name

class Dog(Animal) :
    def bark(self) :
        print(f"{self.name} would bark")

class Cat(Animal) :
    def meow(self):
        print(f"{self.name} would meow")

dog = Dog("My Dog")
dog.bark()
cat = Cat("My Cat")
cat.meow()