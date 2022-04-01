class Human:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name+" is Walking")

    def chat(self):
        print(self.name+ " is Chatting")

aditya = Human("Aditya")
aditya.chat()
aravind = Human("Aravind")
aravind.walk()
