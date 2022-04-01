class TwoWheeler :

    def __init__(self, name):
        self.name = name

    def tyre(self):
        print(f"My {self.name} has 2 tyres")

    def brake(self):
        print(f"My {self.name} has brakes")

    def sideMirriors(self):
        print(f"My {self.name} has 2 side mirrors")

    def speedometer(self):
        print(f"My {self.name} has a speedometer")


class Pept(TwoWheeler) :
    def smallFuelTank(self):
        print(f"My {self.name} has small fuel tank")

    def lessWeight(self):
        print(f"My {self.name} is about 70 kg weigth")


class Activa(TwoWheeler) :
    def largeFuelTank(self):
        print(f"My {self.name} has large fuel tank")

    def largeWeigth(self):
        print(f"My {self.name} is about 100kg weigth")

pept = Pept("Pept")

pept.tyre()
pept.brake()
pept.sideMirriors()
pept.speedometer()

pept.smallFuelTank()
pept.lessWeight()

activa = Activa("Activa")

activa.tyre()
activa.brake()
activa.sideMirriors()
activa.speedometer()

activa.largeFuelTank()
activa.largeWeigth()