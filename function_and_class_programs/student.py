class Student:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSchoolName(self, school_name):
        self.school_name = school_name

    def getSchoolName(self):
        return self.school_name

    def setClass(self, Class):
        self.Class = Class

    def getClass(self):
        return self.Class

    def setSection(self, section):
        self.section = section

    def getSection(self):
        return self.section

    def setRollNumber(self, roll_number):
        self.roll_number = roll_number

    def getRollNumber(self):
        return self.roll_number


student1 = Student()

student1.setName("Aditya")
student1.setSchoolName("Chimaya Vidyalaya")
student1.setClass("VII")
student1.setSection("D")
student1.setRollNumber("7147")

print(student1.getName())
print(student1.getSchoolName())
print(student1.getClass())
print(student1.getSection())
print(student1.getRollNumber())