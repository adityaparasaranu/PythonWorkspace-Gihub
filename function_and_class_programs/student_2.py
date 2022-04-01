class Student :
    def get_student(self):
        self.name = input("Name : ")
        self.sid = input("Student ID : ")


class Test(Student) :
    def get_marks(self):
        self.studentClass = input("Class : ")
        print("Enter the marks of the respective subjects")
        self.maths = int(input("Maths Marks : "))
        self.social = int(input("Social Marks : "))
        self.science = int(input("Science Marks : "))
        self.english = int(input("English Marks : "))
        self.tamil = int(input("Tamil Marks : "))


class Marks(Test) :
    def display(self):
        print("------------------------------------------")
        print("------------------------------------------")
        print("------------------------------------------")
        print("Name :", self.name)
        print("Student ID :", self.sid)
        print("Class :", self.studentClass)
        print("Toatal Marks :", self.maths + self.social +  self.science + self.english + self.tamil, "out of 80")


marks = Marks()
marks.get_student()
marks.get_marks()
marks.display()